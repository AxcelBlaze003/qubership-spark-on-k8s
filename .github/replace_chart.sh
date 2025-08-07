#!/bin/bash
set -euo pipefail
TAG="$1"
TRANSFER_IMAGE=ghcr.io/netcracker/qubership-spark-on-k8s-transfer:${TAG}
echo "Pulling image: $TRANSFER_IMAGE"
docker pull "${TRANSFER_IMAGE}"
echo "Creating container from image..."
docker run --name transfer "${TRANSFER_IMAGE}" /bin/true || true
echo "Replacing local ./chart with chart from image..."
rm -rf ./chart
docker cp transfer:chart ./chart
echo "Stopping and removing container..."
docker stop transfer >/dev/null
docker rm transfer >/dev/null
