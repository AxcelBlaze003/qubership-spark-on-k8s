ARG base_img=ghcr.io/axcelblaze003/qubership-spark-customized:main

FROM maven:3-eclipse-temurin-17-alpine AS unpacker

COPY --chmod=0777 src src
COPY --chmod=0777 pom.xml pom.xml

RUN mvn clean install

FROM ghcr.io/axcelblaze003/qubership-spark-customized:main

USER 185

COPY --from=unpacker --chmod=0777 target/word-count-spark-app-1.0-SNAPSHOT.jar /opt/spark/examples/
