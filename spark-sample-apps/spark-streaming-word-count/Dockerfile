ARG base_img=ghcr.io/axcelblaze003/qubership-spark-customized:main

FROM maven:3-eclipse-temurin-17-alpine AS unpacker

COPY --chmod=0777 src src
COPY --chmod=0777 pom.xml pom.xml

RUN mvn clean install && \
    apk add curl && \
    curl -k -L https://repo1.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/0.11.0/jmx_prometheus_javaagent-0.11.0.jar -o jmx_prometheus_javaagent-0.11.0.jar


FROM ghcr.io/axcelblaze003/qubership-spark-customized:main

ARG spark_uid=185
USER root

USER ${spark_uid}

COPY --from=unpacker --chmod=0777 jmx_prometheus_javaagent-0.11.0.jar target/spark-streaming-1.0-SNAPSHOT-jar-with-dependencies.jar /opt/spark/examples/




