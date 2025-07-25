ARG base_img=ghcr.io/axcelblaze003/qubership-spark-customized:main

FROM $base_img

USER root

RUN set -ex; \
    apt-get update; \
    mkdir tempdebs; \
    cd tempdebs; \
    curl -sLO https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu/pool/main/p/python3.11/libpython3.11-minimal_3.11.13-1+jammy1_amd64.deb; \
    curl -sLO https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu/pool/main/p/python3.11/libpython3.11-stdlib_3.11.13-1+jammy1_amd64.deb; \
    curl -sLO https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu/pool/main/p/python3.11/python3.11_3.11.13-1+jammy1_amd64.deb; \
    curl -sLO https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu/pool/main/p/python3.11/python3.11-minimal_3.11.13-1+jammy1_amd64.deb; \
    cd ..; \
    apt-get install -y mailcap mime-support; \
    dpkg -R --install tempdebs/; \
    rm -r tempdebs; \
    apt-get install -y python3-pip; \
    rm -rf /var/lib/apt/lists/*; \
    ln -sf python3.11 /usr/bin/python3

USER spark
