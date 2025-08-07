from ruamel.yaml import YAML
import re
import sys
import os

yaml = YAML()
yaml.preserve_quotes = True
yaml.indent(mapping=2, sequence=4, offset=2)

yaml.representer.add_representer(
    type(None), lambda self, _: self.represent_scalar('tag:yaml.org,2002:null', '~')
)

def parse_release_images_yaml(file_path):
    with open(file_path) as f:
        data = yaml.load(f)

    image_versions = {}
    for _, image_full in data.items():
        match = re.match(r"(.+):([\w.-]+)", image_full)
        if match:
            image_name, tag = match.groups()
            image_versions[image_name] = tag
    return image_versions

def update_node(node, image_versions):
    if isinstance(node, dict):
        if "registry" in node and "tag" in node and "repository" not in node:
            repo = node["registry"]
            old_tag = node["tag"]
            if repo in image_versions:
                new_tag = image_versions[repo]
                if new_tag != old_tag:
                    print(f"Updating tag for {repo}: {old_tag} → {new_tag}")
                    node["tag"] = new_tag
                else:
                    print(f"No change needed for {repo}: already {new_tag}")

        if "registry" in node and "repository" in node and "tag" in node:
            full_image = f"{node['registry'].rstrip('/')}/{node['repository'].lstrip('/')}"
            old_tag = node["tag"]
            if full_image in image_versions:
                new_tag = image_versions[full_image]
                if new_tag != old_tag:
                    print(f"Updating tag for {full_image}: {old_tag} → {new_tag}")
                    node["tag"] = new_tag
                else:
                    print(f"No change needed for {full_image}: already {new_tag}")

        if "repository" in node and "tag" in node:
            full_image = node["repository"]
            old_tag = node["tag"]
            if full_image in image_versions:
                new_tag = image_versions[full_image]
                if new_tag != old_tag:
                    print(f"Updating tag for {full_image}: {old_tag} → {new_tag}")
                    node["tag"] = new_tag
                else:
                    print(f"No change needed for {full_image}: already {new_tag}")            

        for key, value in node.items():
            node[key] = update_node(value, image_versions)

    elif isinstance(node, list):
        return [update_node(item, image_versions) for item in node]

    elif isinstance(node, str):
        match = re.match(r"^(.+):([\w.-]+)$", node)
        if match:
            image_name, current_tag = match.groups()
            if image_name in image_versions:
                new_tag = image_versions[image_name]
                if new_tag != current_tag:
                    print(f"Updating image: {node} → {image_name}:{new_tag}")
                    return f"{image_name}:{new_tag}"
        return node

    return node

def update_values_yaml(values_path, image_versions):
    if not os.path.exists(values_path):
        print(f"File not found: {values_path}")
        return

    with open(values_path) as f:
        values = yaml.load(f)

    updated = update_node(values, image_versions)

    with open(values_path, "w") as f:
        yaml.dump(updated, f)

def replace_values_yaml(values_file, releases_file, image_key):
    if not os.path.exists(values_file):
        print(f"File not found: {values_file}")
        return

    with open(values_file) as f:
        values = yaml.load(f)

    with open(releases_file) as f:
        data = yaml.load(f)

    image_versions = {}
    for key, full_image in data.items():
        if ":" not in full_image:
            continue
        image_part, tag = full_image.rsplit(":", 1)

        parts = image_part.split("/")
        if len(parts) >= 2:
            registry = parts[0]
            repository = "/".join(parts[1:])
        else:
            registry = ""
            repository = parts[0]

        image_versions[key] = {
            "registry": registry,
            "repository": repository,
            "tag": tag,
        }

    if image_key not in image_versions:
        print(f"No image found for key '{image_key}' in release-images.yaml")
        return

    new_image = image_versions[image_key]

    image_block = values.get("image", {})
    old_registry = image_block.get("registry", "")
    old_repository = image_block.get("repository", "")
    old_tag = image_block.get("tag", "")

    updated = False
    if old_registry != new_image["registry"]:
        print(f"Updating registry: {old_registry} → {new_image['registry']}")
        image_block["registry"] = new_image["registry"]
        updated = True

    if old_repository != new_image["repository"]:
        print(f"Updating repository: {old_repository} → {new_image['repository']}")
        image_block["repository"] = new_image["repository"]
        updated = True

    if old_tag != new_image["tag"]:
        print(f"Updating tag: {old_tag} → {new_image['tag']}")
        image_block["tag"] = new_image["tag"]
        updated = True

    if updated:
        values["image"] = image_block
        with open(values_file, "w") as f:
            yaml.dump(values, f)
        print("values.yaml updated successfully.")
    else:
        print("No changes made. Image values are already up to date.")


if __name__ == "__main__":
   
    # Modes: images, qubership-spark-operator

    mode = sys.argv[1]

    if mode == "images":
        releases_file = sys.argv[2]
        values_file = sys.argv[3]
        image_versions = parse_release_images_yaml(releases_file)
        update_values_yaml(values_file, image_versions)

    elif mode == "qubership-spark-operator":
        releases_file = sys.argv[2]
        values_file = sys.argv[3]
        image_key = mode  # qubership-spark-operator
        replace_values_yaml(values_file, releases_file, image_key)

    else:
        print("Invalid mode")
