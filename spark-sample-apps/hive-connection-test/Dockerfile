ARG base_img_py=ghcr.io/axcelblaze003/qubership-spark-customized-py:main

FROM maven:3-eclipse-temurin-17-alpine AS unpacker
ENV MAVEN_REPO=https://repo1.maven.org/maven2
RUN apk add --no-cache curl=8.12.1-r1

# hadolint ignore=DL3003
RUN mkdir -p /opt/spark/hivejars && \
    cd /opt/spark/hivejars && \
    curl -k -LO $MAVEN_REPO/org/apache/hive/hive-metastore/3.1.3/hive-metastore-3.1.3.jar  && \
    curl -k -LO $MAVEN_REPO/org/apache/hive/hive-service/3.1.3/hive-service-3.1.3.jar  && \
    curl -k -LO $MAVEN_REPO/org/apache/hive/hive-jdbc/3.1.3/hive-jdbc-3.1.3.jar  && \
    curl -k -LO $MAVEN_REPO/org/apache/hadoop/hadoop-common/3.2.2/hadoop-common-3.2.2.jar  && \
	curl -k -LO $MAVEN_REPO/org/apache/hive/hive-common/3.1.3/hive-common-3.1.3.jar  && \
    curl -k -LO $MAVEN_REPO/org/apache/logging/log4j/log4j-api/2.10.0/log4j-api-2.10.0.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/derby/derby/10.14.1.0/derby-10.14.1.0.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/hive/hive-exec/3.1.3/hive-exec-3.1.3.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/hive/hive-serde/3.1.3/hive-serde-3.1.3.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/hadoop/hadoop-client-api/3.3.4/hadoop-client-api-3.3.4.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/hadoop/hadoop-client-runtime/3.3.4/hadoop-client-runtime-3.3.4.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/hive/hive-shims/3.1.3/hive-shims-3.1.3.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/hive/hive-standalone-metastore/3.1.3/hive-standalone-metastore-3.1.3.jar && \
    curl -k -LO $MAVEN_REPO/javolution/javolution/5.5.1/javolution-5.5.1.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/hbase/hbase-client/2.0.0-alpha4/hbase-client-2.0.0-alpha4.jar && \
    curl -k -LO $MAVEN_REPO/com/jolbox/bonecp/0.8.0.RELEASE/bonecp-0.8.0.RELEASE.jar && \
    curl -k -LO $MAVEN_REPO/com/zaxxer/HikariCP/2.6.1/HikariCP-2.6.1.jar && \
    curl -k -LO $MAVEN_REPO/commons-cli/commons-cli/1.2/commons-cli-1.2.jar && \
    curl -k -LO $MAVEN_REPO/commons-lang/commons-lang/2.6/commons-lang-2.6.jar && \
    curl -k -LO $MAVEN_REPO/commons-pool/commons-pool/1.5.4/commons-pool-1.5.4.jar && \
    curl -k -LO $MAVEN_REPO/commons-dbcp/commons-dbcp/1.4/commons-dbcp-1.4.jar && \
    curl -k -LO $MAVEN_REPO/javax/jdo/jdo-api/3.0.1/jdo-api-3.0.1.jar && \
    curl -k -LO $MAVEN_REPO/org/antlr/antlr-runtime/3.5.2/antlr-runtime-3.5.2.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/thrift/libfb303/0.9.3/libfb303-0.9.3.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/thrift/libthrift/0.9.3/libthrift-0.9.3.jar && \
    curl -k -LO $MAVEN_REPO/co/cask/tephra/tephra-api/0.6.0/tephra-api-0.6.0.jar && \
    curl -k -LO $MAVEN_REPO/co/cask/tephra/tephra-core/0.6.0/tephra-core-0.6.0.jar && \
    curl -k -LO $MAVEN_REPO/co/cask/tephra/tephra-hbase-compat-1.0/0.6.0/tephra-hbase-compat-1.0-0.6.0.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/hive/hive-upgrade-acid/3.1.3/hive-upgrade-acid-3.1.3.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/hive/hive-service-rpc/3.1.3/hive-service-rpc-3.1.3.jar && \
    curl -k -LO $MAVEN_REPO/commons-codec/commons-codec/1.15/commons-codec-1.15.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/arrow/arrow-vector/0.8.0/arrow-vector-0.8.0.jar && \
    curl -k -LO $MAVEN_REPO/com/carrotsearch/hppc/0.7.2/hppc-0.7.2.jar && \
    curl -k -LO $MAVEN_REPO/com/vlkan/flatbuffers/1.2.0-3f79e055/flatbuffers-1.2.0-3f79e055.jar && \
    curl -k -LO $MAVEN_REPO/net/sf/opencsv/opencsv/2.3/opencsv-2.3.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/parquet/parquet-hadoop-bundle/1.10.0/parquet-hadoop-bundle-1.10.0.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/hive/hive-classification/3.1.3/hive-classification-3.1.3.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/hive/hive-storage-api/2.7.0/hive-storage-api-2.7.0.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/commons/commons-lang3/3.9/commons-lang3-3.9.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/orc/orc-core/1.5.8/orc-core-1.5.8.jar && \
    curl -k -LO $MAVEN_REPO/jline/jline/2.12/jline-2.12.jar && \
    curl -k -LO $MAVEN_REPO/javax/servlet/javax.servlet-api/3.1.0/javax.servlet-api-3.1.0.jar && \
    curl -k -LO $MAVEN_REPO/org/eclipse/jetty/jetty-http/9.3.20.v20170531/jetty-http-9.3.20.v20170531.jar && \
    curl -k -LO $MAVEN_REPO/org/eclipse/jetty/jetty-rewrite/9.3.20.v20170531/jetty-rewrite-9.3.20.v20170531.jar && \
    curl -k -LO $MAVEN_REPO/org/eclipse/jetty/jetty-server/9.3.20.v20170531/jetty-server-9.3.20.v20170531.jar && \
    curl -k -LO $MAVEN_REPO/org/eclipse/jetty/jetty-servlet/9.3.20.v20170531/jetty-servlet-9.3.20.v20170531.jar && \
    curl -k -LO $MAVEN_REPO/org/eclipse/jetty/jetty-webapp/9.3.20.v20170531/jetty-webapp-9.3.20.v20170531.jar && \
    curl -k -LO $MAVEN_REPO/joda-time/joda-time/2.9.9/joda-time-2.9.9.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/logging/log4j/log4j-1.2-api/2.17.1/log4j-1.2-api-2.17.1.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/logging/log4j/log4j-web/2.17.1/log4j-web-2.17.1.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/logging/log4j/log4j-slf4j-impl/2.17.1/log4j-slf4j-impl-2.17.1.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/commons/commons-compress/1.19/commons-compress-1.19.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/ant/ant/1.9.1/ant-1.9.1.jar && \
    curl -k -LO $MAVEN_REPO/net/sf/jpam/jpam/1.1/jpam-1.1.jar && \
    curl -k -LO $MAVEN_REPO/com/tdunning/json/1.8/json-1.8.jar && \
    curl -k -LO $MAVEN_REPO/io/dropwizard/metrics/metrics-jvm/3.1.0/metrics-jvm-3.1.0.jar && \
    curl -k -LO $MAVEN_REPO/io/dropwizard/metrics/metrics-json/3.1.0/metrics-json-3.1.0.jar && \
    curl -k -LO $MAVEN_REPO/com/fasterxml/jackson/core/jackson-databind/2.12.0/jackson-databind-2.12.0.jar && \
    curl -k -LO $MAVEN_REPO/com/github/joshelser/dropwizard-metrics-hadoop-metrics2-reporter/0.1.2/dropwizard-metrics-hadoop-metrics2-reporter-0.1.2.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/hive/shims/hive-shims-common/3.1.3/hive-shims-common-3.1.3.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/zookeeper/zookeeper/3.4.6/zookeeper-3.4.6.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/httpcomponents/httpclient/4.5.13/httpclient-4.5.13.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/httpcomponents/httpcore/4.4.13/httpcore-4.4.13.jar && \
    curl -k -LO $MAVEN_REPO/commons-logging/commons-logging/1.2/commons-logging-1.2.jar && \
    curl -k -LO $MAVEN_REPO/org/slf4j/slf4j-log4j12/1.6.1/slf4j-log4j12-1.6.1.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/hive/shims/hive-shims-0.23/3.1.3/hive-shims-0.23-3.1.3.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/hive/shims/hive-shims-scheduler/3.1.3/hive-shims-scheduler-3.1.3.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/logging/log4j/log4j-core/2.17.1/log4j-core-2.17.1.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/hadoop/hadoop-yarn-server-resourcemanager/3.1.0/hadoop-yarn-server-resourcemanager-3.1.0.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/hadoop/hadoop-annotations/3.1.0/hadoop-annotations-3.1.0.jar && \
    curl -k -LO $MAVEN_REPO/com/google/inject/extensions/guice-servlet/4.0/guice-servlet-4.0.jar && \
    curl -k -LO $MAVEN_REPO/com/google/protobuf/protobuf-java/2.5.0/protobuf-java-2.5.0.jar && \
    curl -k -LO $MAVEN_REPO/commons-io/commons-io/2.6/commons-io-2.6.jar && \
    curl -k -LO $MAVEN_REPO/com/google/inject/guice/4.0/guice-4.0.jar && \
    curl -k -LO $MAVEN_REPO/com/sun/jersey/jersey-json/1.19/jersey-json-1.19.jar && \
    curl -k -LO $MAVEN_REPO/com/sun/jersey/contribs/jersey-guice/1.19/jersey-guice-1.19.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/hadoop/hadoop-yarn-common/3.1.0/hadoop-yarn-common-3.1.0.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/hadoop/hadoop-yarn-api/3.1.0/hadoop-yarn-api-3.1.0.jar && \
    curl -k -LO $MAVEN_REPO/javax/xml/bind/jaxb-api/2.2.11/jaxb-api-2.2.11.jar && \
    curl -k -LO $MAVEN_REPO/org/codehaus/jettison/jettison/1.1/jettison-1.1.jar && \
    curl -k -LO $MAVEN_REPO/com/sun/jersey/jersey-core/1.19/jersey-core-1.19.jar && \
    curl -k -LO $MAVEN_REPO/com/sun/jersey/jersey-client/1.19/jersey-client-1.19.jar && \
    curl -k -LO $MAVEN_REPO/org/eclipse/jetty/jetty-util/9.3.19.v20170502/jetty-util-9.3.19.v20170502.jar && \
    curl -k -LO $MAVEN_REPO/org/eclipse/jetty/jetty-util-ajax/9.3.19.v20170502/jetty-util-ajax-9.3.19.v20170502.jar && \
    curl -k -LO $MAVEN_REPO/log4j/log4j/1.2.17/log4j-1.2.17.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/hadoop/hadoop-yarn-server-common/3.1.0/hadoop-yarn-server-common-3.1.0.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/hadoop/hadoop-yarn-server-applicationhistoryservice/3.1.0/hadoop-yarn-server-applicationhistoryservice-3.1.0.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/hadoop/hadoop-yarn-server-web-proxy/3.1.0/hadoop-yarn-server-web-proxy-3.1.0.jar && \
    curl -k -LO $MAVEN_REPO/org/fusesource/leveldbjni/leveldbjni-all/1.8/leveldbjni-all-1.8.jar && \
    curl -k -LO $MAVEN_REPO/javax/inject/javax.inject/1/javax.inject-1.jar && \
    curl -k -LO $MAVEN_REPO/aopalliance/aopalliance/1.0/aopalliance-1.0.jar && \
    curl -k -LO $MAVEN_REPO/com/sun/xml/bind/jaxb-impl/2.2.3-1/jaxb-impl-2.2.3-1.jar && \
    curl -k -LO $MAVEN_REPO/org/codehaus/jackson/jackson-core-asl/1.9.13/jackson-core-asl-1.9.13.jar && \
    curl -k -LO $MAVEN_REPO/org/codehaus/jackson/jackson-jaxrs/1.9.13/jackson-jaxrs-1.9.13.jar && \
    curl -k -LO $MAVEN_REPO/org/codehaus/jackson/jackson-xc/1.9.13/jackson-xc-1.9.13.jar && \
    curl -k -LO $MAVEN_REPO/javax/ws/rs/jsr311-api/1.1.1/jsr311-api-1.1.1.jar && \
    curl -k -LO $MAVEN_REPO/com/sun/jersey/jersey-servlet/1.19/jersey-servlet-1.19.jar && \
    curl -k -LO $MAVEN_REPO/com/sun/jersey/jersey-server/1.19/jersey-server-1.19.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/hadoop/hadoop-auth/3.1.0/hadoop-auth-3.1.0.jar && \
    curl -k -LO $MAVEN_REPO/com/fasterxml/jackson/core/jackson-core/2.12.0/jackson-core-2.12.0.jar && \
    curl -k -LO $MAVEN_REPO/com/fasterxml/jackson/module/jackson-module-jaxb-annotations/2.12.0/jackson-module-jaxb-annotations-2.12.0.jar && \
    curl -k -LO $MAVEN_REPO/com/fasterxml/jackson/jaxrs/jackson-jaxrs-json-provider/2.12.0/jackson-jaxrs-json-provider-2.12.0.jar && \
    curl -k -LO $MAVEN_REPO/com/fasterxml/jackson/core/jackson-annotations/2.12.0/jackson-annotations-2.12.0.jar && \
    curl -k -LO $MAVEN_REPO/com/nimbusds/nimbus-jose-jwt/4.41.1/nimbus-jose-jwt-4.41.1.jar && \
    curl -k -LO $MAVEN_REPO/net/minidev/json-smart/2.3/json-smart-2.3.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/kerby/kerb-simplekdc/1.0.1/kerb-simplekdc-1.0.1.jar && \
    curl -k -LO $MAVEN_REPO/com/github/stephenc/jcip/jcip-annotations/1.0-1/jcip-annotations-1.0-1.jar && \
    curl -k -LO $MAVEN_REPO/net/minidev/accessors-smart/1.2/accessors-smart-1.2.jar && \
    curl -k -LO $MAVEN_REPO/org/ow2/asm/asm/5.0.4/asm-5.0.4.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/kerby/kerb-client/1.0.1/kerb-client-1.0.1.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/kerby/kerb-admin/1.0.1/kerb-admin-1.0.1.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/kerby/kerby-config/1.0.1/kerby-config-1.0.1.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/kerby/kerb-core/1.0.1/kerb-core-1.0.1.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/kerby/kerb-common/1.0.1/kerb-common-1.0.1.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/kerby/kerb-util/1.0.1/kerb-util-1.0.1.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/kerby/token-provider/1.0.1/token-provider-1.0.1.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/kerby/kerby-pkix/1.0.1/kerby-pkix-1.0.1.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/kerby/kerby-asn1/1.0.1/kerby-asn1-1.0.1.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/kerby/kerby-util/1.0.1/kerby-util-1.0.1.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/kerby/kerb-crypto/1.0.1/kerb-crypto-1.0.1.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/kerby/kerb-server/1.0.1/kerb-server-1.0.1.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/kerby/kerby-xdr/1.0.1/kerby-xdr-1.0.1.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/kerby/kerb-identity/1.0.1/kerb-identity-1.0.1.jar && \
    curl -k -LO $MAVEN_REPO/jakarta/xml/bind/jakarta.xml.bind-api/2.3.2/jakarta.xml.bind-api-2.3.2.jar && \
    curl -k -LO $MAVEN_REPO/jakarta/activation/jakarta.activation-api/1.2.1/jakarta.activation-api-1.2.1.jar && \
    curl -k -LO $MAVEN_REPO/com/fasterxml/jackson/jaxrs/jackson-jaxrs-base/2.12.0/jackson-jaxrs-base-2.12.0.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/hadoop/hadoop-yarn-registry/3.1.0/hadoop-yarn-registry-3.1.0.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/geronimo/specs/geronimo-jcache_1.0_spec/1.0-alpha-1/geronimo-jcache_1.0_spec-1.0-alpha-1.jar && \
    curl -k -LO $MAVEN_REPO/org/ehcache/ehcache/3.3.1/ehcache-3.3.1.jar && \
    curl -k -LO $MAVEN_REPO/com/zaxxer/HikariCP-java7/2.4.12/HikariCP-java7-2.4.12.jar && \
    curl -k -LO $MAVEN_REPO/commons-daemon/commons-daemon/1.0.13/commons-daemon-1.0.13.jar && \
    curl -k -LO $MAVEN_REPO/commons-net/commons-net/3.6/commons-net-3.6.jar && \
    curl -k -LO $MAVEN_REPO/dnsjava/dnsjava/2.1.7/dnsjava-2.1.7.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/commons/commons-math3/3.1.1/commons-math3-3.1.1.jar && \
    curl -k -LO $MAVEN_REPO/commons-collections/commons-collections/3.2.2/commons-collections-3.2.2.jar && \
    curl -k -LO $MAVEN_REPO/commons-beanutils/commons-beanutils/1.9.3/commons-beanutils-1.9.3.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/commons/commons-configuration2/2.1.1/commons-configuration2-2.1.1.jar && \
    curl -k -LO $MAVEN_REPO/com/google/re2j/re2j/1.1/re2j-1.1.jar && \
    curl -k -LO $MAVEN_REPO/com/google/code/gson/gson/2.2.4/gson-2.2.4.jar && \
    curl -k -LO $MAVEN_REPO/com/jcraft/jsch/0.1.54/jsch-0.1.54.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/htrace/htrace-core4/4.1.0-incubating/htrace-core4-4.1.0-incubating.jar && \
    curl -k -LO $MAVEN_REPO/org/codehaus/woodstox/stax2-api/3.1.4/stax2-api-3.1.4.jar && \
    curl -k -LO $MAVEN_REPO/com/fasterxml/woodstox/woodstox-core/5.0.3/woodstox-core-5.0.3.jar && \
    curl -k -LO $MAVEN_REPO/org/eclipse/jetty/jetty-io/9.3.20.v20170531/jetty-io-9.3.20.v20170531.jar && \
    curl -k -LO $MAVEN_REPO/org/eclipse/jetty/jetty-security/9.3.20.v20170531/jetty-security-9.3.20.v20170531.jar && \
    curl -k -LO $MAVEN_REPO/org/eclipse/jetty/jetty-xml/9.3.20.v20170531/jetty-xml-9.3.20.v20170531.jar && \
    curl -k -LO $MAVEN_REPO/com/thoughtworks/paranamer/paranamer/2.7/paranamer-2.7.jar && \
    curl -k -LO $MAVEN_REPO/org/tukaani/xz/1.5/xz-1.5.jar && \
    curl -k -LO $MAVEN_REPO/de/ruedigermoeller/fst/2.50/fst-2.50.jar && \
    curl -k -LO $MAVEN_REPO/com/cedarsoftware/java-util/1.9.0/java-util-1.9.0.jar && \
    curl -k -LO $MAVEN_REPO/com/cedarsoftware/json-io/2.5.1/json-io-2.5.1.jar && \
    curl -k -LO $MAVEN_REPO/com/microsoft/sqlserver/mssql-jdbc/6.2.1.jre7/mssql-jdbc-6.2.1.jre7.jar && \
    curl -k -LO $MAVEN_REPO/javax/servlet/jsp/jsp-api/2.1/jsp-api-2.1.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/orc/orc-shims/1.5.8/orc-shims-1.5.8.jar && \
    curl -k -LO $MAVEN_REPO/io/airlift/aircompressor/0.10/aircompressor-0.10.jar && \
    curl -k -LO $MAVEN_REPO/org/eclipse/jetty/jetty-client/9.3.20.v20170531/jetty-client-9.3.20.v20170531.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/ant/ant-launcher/1.9.1/ant-launcher-1.9.1.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/arrow/arrow-format/0.8.0/arrow-format-0.8.0.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/arrow/arrow-memory/0.8.0/arrow-memory-0.8.0.jar && \
    curl -k -LO $MAVEN_REPO/org/datanucleus/datanucleus-api-jdo/4.2.4/datanucleus-api-jdo-4.2.4.jar && \
    curl -k -LO $MAVEN_REPO/org/datanucleus/datanucleus-core/4.1.17/datanucleus-core-4.1.17.jar && \
    curl -k -LO $MAVEN_REPO/org/datanucleus/datanucleus-rdbms/4.1.19/datanucleus-rdbms-4.1.19.jar && \
    curl -k -LO $MAVEN_REPO/org/datanucleus/javax.jdo/3.2.0-m3/javax.jdo-3.2.0-m3.jar && \
    curl -k -LO $MAVEN_REPO/sqlline/sqlline/1.3.0/sqlline-1.3.0.jar && \
    curl -k -LO $MAVEN_REPO/javax/transaction/transaction-api/1.1/transaction-api-1.1.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/hbase/thirdparty/hbase-shaded-protobuf/1.0.1/hbase-shaded-protobuf-1.0.1.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/hbase/hbase-protocol-shaded/2.0.0-alpha4/hbase-protocol-shaded-2.0.0-alpha4.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/hbase/hbase-protocol/2.0.0-alpha4/hbase-protocol-2.0.0-alpha4.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/hbase/thirdparty/hbase-shaded-miscellaneous/1.0.1/hbase-shaded-miscellaneous-1.0.1.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/hbase/thirdparty/hbase-shaded-netty/1.0.1/hbase-shaded-netty-1.0.1.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/htrace/htrace-core/3.2.0-incubating/htrace-core-3.2.0-incubating.jar && \
    curl -k -LO $MAVEN_REPO/org/jruby/jcodings/jcodings/1.0.18/jcodings-1.0.18.jar && \
    curl -k -LO $MAVEN_REPO/org/jruby/joni/joni/2.1.11/joni-2.1.11.jar && \
    curl -k -LO $MAVEN_REPO/io/dropwizard/metrics/metrics-core/3.2.1/metrics-core-3.2.1.jar && \
    curl -k -LO $MAVEN_REPO/junit/junit/4.11/junit-4.11.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/commons/commons-crypto/1.0.0/commons-crypto-1.0.0.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/yetus/audience-annotations/0.5.0/audience-annotations-0.5.0.jar && \
    curl -k -LO $MAVEN_REPO/org/hamcrest/hamcrest-core/1.3/hamcrest-core-1.3.jar && \
    curl -k -LO $MAVEN_REPO/javax/transaction/jta/1.1/jta-1.1.jar && \
    curl -k -LO $MAVEN_REPO/com/google/inject/extensions/guice-assistedinject/3.0/guice-assistedinject-3.0.jar && \
    curl -k -LO $MAVEN_REPO/it/unimi/dsi/fastutil/6.5.6/fastutil-6.5.6.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/twill/twill-common/0.6.0-incubating/twill-common-0.6.0-incubating.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/twill/twill-core/0.6.0-incubating/twill-core-0.6.0-incubating.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/twill/twill-discovery-api/0.6.0-incubating/twill-discovery-api-0.6.0-incubating.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/twill/twill-discovery-core/0.6.0-incubating/twill-discovery-core-0.6.0-incubating.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/twill/twill-zookeeper/0.6.0-incubating/twill-zookeeper-0.6.0-incubating.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/twill/twill-api/0.6.0-incubating/twill-api-0.6.0-incubating.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/hive/hive-llap-tez/3.1.3/hive-llap-tez-3.1.3.jar && \
    curl -k -LO $MAVEN_REPO/org/antlr/ST4/4.0.4/ST4-4.0.4.jar && \
    curl -k -LO $MAVEN_REPO/org/codehaus/groovy/groovy-all/2.4.11/groovy-all-2.4.11.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/calcite/calcite-core/1.16.0/calcite-core-1.16.0.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/calcite/avatica/avatica/1.11.0/avatica-1.11.0.jar && \
    curl -k -LO $MAVEN_REPO/stax/stax-api/1.0.1/stax-api-1.0.1.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/hive/hive-llap-client/3.1.3/hive-llap-client-3.1.3.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/hive/hive-llap-common/3.1.3/hive-llap-common-3.1.3.jar && \
    curl -k -LO $MAVEN_REPO/org/apache/calcite/calcite-linq4j/1.16.0/calcite-linq4j-1.16.0.jar && \
    curl -k -LO $MAVEN_REPO/com/esri/geometry/esri-geometry-api/2.0.0/esri-geometry-api-2.0.0.jar && \
    curl -k -LO $MAVEN_REPO/com/google/code/findbugs/jsr305/3.0.1/jsr305-3.0.1.jar && \
    curl -k -LO $MAVEN_REPO/com/yahoo/datasketches/sketches-core/0.9.0/sketches-core-0.9.0.jar && \
    curl -k -LO $MAVEN_REPO/org/codehaus/janino/janino/2.7.6/janino-2.7.6.jar && \
    curl -k -LO $MAVEN_REPO/org/codehaus/janino/commons-compiler/2.7.6/commons-compiler-2.7.6.jar && \
    curl -k -LO $MAVEN_REPO/com/yahoo/datasketches/memory/0.9.0/memory-0.9.0.jar && \
    curl -k -LO $MAVEN_REPO/org/xerial/snappy/snappy-java/1.1.8.2/snappy-java-1.1.8.2.jar && \
    curl -k -LO $MAVEN_REPO/org/slf4j/slf4j-api/1.7.36/slf4j-api-1.7.36.jar

# hadolint ignore=DL3006
FROM $base_img_py

USER root

WORKDIR /opt/spark/examples/

COPY --chmod=0777 spark_hive_test.py /opt/spark/examples/

COPY --chmod=0777 delete_s3.py /opt/spark/examples/

COPY --from=unpacker --chmod=0777 /opt/spark/hivejars /opt/spark/hivejars

RUN python3 -m pip install --no-cache-dir boto3==1.39.3

USER spark