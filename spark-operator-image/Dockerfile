FROM alpine:latest AS unpacker
ENV HADOOP_VERSION=3.3.4
ENV SPARK_JARS_DIR=/opt/spark/jars
ENV MAVEN_REPO=https://repo1.maven.org/maven2
RUN apk add curl
RUN mkdir -p /opt/spark/jars/ && \
    #curl -k https://dlcdn.apache.org/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz | tar xvz -C /opt && \
    curl -k -L $MAVEN_REPO/com/amazonaws/aws-java-sdk-bundle/1.12.782/aws-java-sdk-bundle-1.12.782.jar --output $SPARK_JARS_DIR/aws-java-sdk-bundle-1.12.782.jar && \
    curl -k -L $MAVEN_REPO/org/apache/hadoop/hadoop-aws/$HADOOP_VERSION/hadoop-aws-$HADOOP_VERSION.jar --output $SPARK_JARS_DIR/hadoop-aws-$HADOOP_VERSION.jar && \
    curl -k -L https://repository.cloudera.com/repository/cloudera-repos/org/codehaus/jackson/jackson-mapper-asl/1.9.13-cloudera.4/jackson-mapper-asl-1.9.13-cloudera.4.jar --output $SPARK_JARS_DIR/jackson-mapper-asl-1.9.13-cloudera.4.jar && \
    curl -k -L $MAVEN_REPO/org/apache/ivy/ivy/2.5.2/ivy-2.5.2.jar --output $SPARK_JARS_DIR/ivy-2.5.2.jar && \
    curl -k -L $MAVEN_REPO/com/google/guava/guava/32.0.1-jre/guava-32.0.1-jre.jar --output $SPARK_JARS_DIR/guava-32.0.1-jre.jar && \
    curl -k -L $MAVEN_REPO/io/netty/netty-all/4.1.118.Final/netty-all-4.1.118.Final.jar --output $SPARK_JARS_DIR/netty-all-4.1.118.Final.jar && \
    curl -k -L $MAVEN_REPO/io/netty/netty-buffer/4.1.118.Final/netty-buffer-4.1.118.Final.jar --output $SPARK_JARS_DIR/netty-buffer-4.1.118.Final.jar && \
    curl -k -L $MAVEN_REPO/io/netty/netty-codec/4.1.118.Final/netty-codec-4.1.118.Final.jar --output $SPARK_JARS_DIR/netty-codec-4.1.118.Final.jar && \
    curl -k -L $MAVEN_REPO/io/netty/netty-codec-http2/4.1.118.Final/netty-codec-http2-4.1.118.Final.jar --output $SPARK_JARS_DIR/netty-codec-http2-4.1.118.Final.jar && \
    curl -k -L $MAVEN_REPO/io/netty/netty-codec-http/4.1.118.Final/netty-codec-http-4.1.118.Final.jar --output $SPARK_JARS_DIR/netty-codec-http-4.1.118.Final.jar && \
    curl -k -L $MAVEN_REPO/io/netty/netty-codec-socks/4.1.118.Final/netty-codec-socks-4.1.118.Final.jar --output $SPARK_JARS_DIR/netty-codec-socks-4.1.118.Final.jar && \
    curl -k -L $MAVEN_REPO/io/netty/netty-common/4.1.118.Final/netty-common-4.1.118.Final.jar --output $SPARK_JARS_DIR/netty-common-4.1.118.Final.jar && \
    curl -k -L $MAVEN_REPO/io/netty/netty-handler/4.1.118.Final/netty-handler-4.1.118.Final.jar --output $SPARK_JARS_DIR/netty-handler-4.1.118.Final.jar && \
    curl -k -L $MAVEN_REPO/io/netty/netty-handler-proxy/4.1.118.Final/netty-handler-proxy-4.1.118.Final.jar --output $SPARK_JARS_DIR/netty-handler-proxy-4.1.118.Final.jar && \
    curl -k -L $MAVEN_REPO/io/netty/netty-resolver/4.1.118.Final/netty-resolver-4.1.118.Final.jar --output $SPARK_JARS_DIR/netty-resolver-4.1.118.Final.jar && \
    curl -k -L $MAVEN_REPO/io/netty/netty-transport/4.1.118.Final/netty-transport-4.1.118.Final.jar --output $SPARK_JARS_DIR/netty-transport-4.1.118.Final.jar && \
    curl -k -L $MAVEN_REPO/io/netty/netty-transport-classes-epoll/4.1.118.Final/netty-transport-classes-epoll-4.1.118.Final.jar --output $SPARK_JARS_DIR/netty-transport-classes-epoll-4.1.118.Final.jar && \
    curl -k -L $MAVEN_REPO/io/netty/netty-transport-classes-kqueue/4.1.118.Final/netty-transport-classes-kqueue-4.1.118.Final.jar --output $SPARK_JARS_DIR/netty-transport-classes-kqueue-4.1.118.Final.jar && \
    curl -k -L $MAVEN_REPO/io/netty/netty-transport-native-epoll/4.1.118.Final/netty-transport-native-epoll-4.1.118.Final-linux-aarch_64.jar --output $SPARK_JARS_DIR/netty-transport-native-epoll-4.1.118.Final-linux-aarch_64.jar && \
    curl -k -L $MAVEN_REPO/io/netty/netty-transport-native-epoll/4.1.118.Final/netty-transport-native-epoll-4.1.118.Final-linux-x86_64.jar --output $SPARK_JARS_DIR/netty-transport-native-epoll-4.1.118.Final-linux-x86_64.jar && \
    curl -k -L $MAVEN_REPO/io/netty/netty-transport-native-kqueue/4.1.118.Final/netty-transport-native-kqueue-4.1.118.Final-osx-aarch_64.jar --output $SPARK_JARS_DIR/netty-transport-native-kqueue-4.1.118.Final-osx-aarch_64.jar && \
    curl -k -L $MAVEN_REPO/io/netty/netty-transport-native-kqueue/4.1.118.Final/netty-transport-native-kqueue-4.1.118.Final-osx-x86_64.jar --output $SPARK_JARS_DIR/netty-transport-native-kqueue-4.1.118.Final-osx-x86_64.jar && \
    curl -k -L $MAVEN_REPO/io/netty/netty-transport-native-unix-common/4.1.118.Final/netty-transport-native-unix-common-4.1.118.Final.jar --output $SPARK_JARS_DIR/netty-transport-native-unix-common-4.1.118.Final.jar


FROM ghcr.io/kubeflow/spark-operator/controller:2.2.1
ENV SPARK_JARS_DIR=/opt/spark/jars

RUN rm $SPARK_JARS_DIR/jackson-mapper-asl-1.9.13.jar $SPARK_JARS_DIR/ivy-2.5.1.jar $SPARK_JARS_DIR/guava-14.0.1.jar $SPARK_JARS_DIR/netty-all-4.1.96.Final.jar $SPARK_JARS_DIR/netty-buffer-4.1.96.Final.jar $SPARK_JARS_DIR/netty-codec-4.1.96.Final.jar $SPARK_JARS_DIR/netty-codec-http2-4.1.96.Final.jar $SPARK_JARS_DIR/netty-codec-http-4.1.96.Final.jar $SPARK_JARS_DIR/netty-codec-socks-4.1.96.Final.jar $SPARK_JARS_DIR/netty-common-4.1.96.Final.jar $SPARK_JARS_DIR/netty-handler-4.1.96.Final.jar $SPARK_JARS_DIR/netty-handler-proxy-4.1.96.Final.jar $SPARK_JARS_DIR/netty-resolver-4.1.96.Final.jar $SPARK_JARS_DIR/netty-transport-4.1.96.Final.jar $SPARK_JARS_DIR/netty-transport-classes-epoll-4.1.96.Final.jar $SPARK_JARS_DIR/netty-transport-classes-kqueue-4.1.96.Final.jar $SPARK_JARS_DIR/netty-transport-native-epoll-4.1.96.Final-linux-aarch_64.jar $SPARK_JARS_DIR/netty-transport-native-epoll-4.1.96.Final-linux-x86_64.jar $SPARK_JARS_DIR/netty-transport-native-kqueue-4.1.96.Final-osx-aarch_64.jar $SPARK_JARS_DIR/netty-transport-native-kqueue-4.1.96.Final-osx-x86_64.jar $SPARK_JARS_DIR/netty-transport-native-unix-common-4.1.96.Final.jar

COPY --from=unpacker --chmod=0777 $SPARK_JARS_DIR/ $SPARK_JARS_DIR/
