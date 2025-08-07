**This guide should be read after [spark-operator overview](https://www.kubeflow.org/docs/components/spark-operator/overview/), [architecture.md](/docs/public/architecture.md) and [installation.md](/docs/public/installation.md)**

## Repository structure

* `.github/workflows` - folder related to spark-on-k8s images pipeline config.
* `chart` - helm charts. It includes charts for monitoring of [spark-operator](https://github.com/kubeflow/spark-operator), spark applications and chart for [status-provisioner](https://github.com/Netcracker/qubership-deployment-status-provisioner).
* `docs` - Documentation and some examples.
* `docker-transfer` - Docker image with comlete spark-on-k8s chart. The chart in the image includes [spark-operator-chart](https://github.com/kubeflow/spark-operator/tree/master/charts/spark-operator-chart) as a subchart.
* `spark-customized` - contains files for spark image building and spark-py image building.
* `spark-history-server` - contains chart for spark history server.
* `spark-operator-image` - contains files for spark operator image building. It is based on [spark-operator](https://github.com/kubeflow/spark-operator) image with some minor tweaks.
* `spark-sample-apps` - contains files for building, deploying and running spark operator sample applications.
* `spark-service-integration-tests` contains integration tests.
* `spark-thrift-server` - contains chart for spark thrift server.

## How to start

Main components of spark-on-k8s distribution are:

* [Spark-operator](https://github.com/kubeflow/spark-operator). Consists of controller and webhook. For more information refer to https://www.kubeflow.org/docs/components/spark-operator/getting-started/.
* `Spark-history-server` - Spark tool that can be used to view logs of spark applications. For more information refer to https://spark.apache.org/docs/3.5.5/monitoring.html .
* `Spark-thrift-server` - Spark tool to execute SQL queries. For more information refer to https://spark.apache.org/docs/3.5.5/sql-distributed-sql-engine.html .

Spark-on-k8s distribution includes the following images:

* [Qubership spark image](/spark-customized/Dockerfile): image based on [official spark-java 17 image](https://github.com/apache/spark-docker/tree/master/3.5.5/scala2.12-java17-ubuntu) with patch version updates of some jars to reduce vulnerabilities. Includes some additional jars, for example, to work with S3 and [profiler Jars](https://github.com/Netcracker/qubership-profiler-agent). Additionally contains modified entrypoint to support working with certificates and with [qubership profilier](https://github.com/Netcracker/qubership-profiler-agent). Also includes custom entrypoint for spark-thrift service. The image is used in spark-history-server, spark-thrift-server and can be used to create custom spark applications(also can be used to run example spark applications).
* [Qubership spark python image](/spark-customized/py/Dockerfile): image based on spark image that adds python into the image. The image is used custom python spark applications. Can be used to run python example spark applications.
* [Qubership spark operator image](/spark-operator-image/Dockerfile): image based on the [official spark operator image](https://hub.docker.com/r/kubeflow/spark-operator/). Includes custom entrypoint based on spark image to be able to run the image under any user. Note, that official spark operator image is based on [official spark-java 11 image](https://github.com/apache/spark-docker/tree/master/3.5.5/scala2.12-java11-ubuntu) .
* [integration tests image](/spark-service-integration-tests/docker/Dockerfile): image used to run qubership spark-on-k8s integration tests. It is based on qubership [integration tests image](https://github.com/Netcracker/qubership-docker-integration-tests)
* [Oauth2 proxy image](https://github.com/oauth2-proxy/oauth2-proxy/blob/master/Dockerfile): image used to set up a proxy with authentication for spark history sever.
* [Status provisioner image](https://github.com/Netcracker/qubership-deployment-status-provisioner): Qubership status provisioner image that is used to report deploy status for application deployer.



### Build

Build pipeline is configured in [/.github/workflows](/.github/workflows). It is used to build images for qubership-spark-on-k8s.


### Deploy to k8s

See [installation.md](/docs/public/installation.md)

### How to debug and troubleshoot

#### Spark operator deploy problems
The resulting chart should be extracted from docker-transfer image. When facing problems with spark-on-k8s deploy, firstly it is necessary to check installation parameters. If there are problems with pod starting, it is necessary to check events in the namespace. Often the problems are caused by security context or incorrectly mounted volumes.

#### Problems with submitting and running spark applications

If the application can't be submitted at all, it is necessary to check application CR. If application can be submitted the following things can be checked:

* Application CR status.
* Spark operator logs.
* Namespace events.
* Application pod logs .
* Volcano pod logs if volcano integration is enabled.

**Note** It is also might be useful to check pod resources, especially spark-operator controller pod. While written in Go, spark-operator controller pod runs java process for every submitted spark application.

If it doesn't help, it is also might be useful to check application spark image dockerfile and application code.

#### Issues with spark operator pods

Check latest community commits if there were any potential problematic changes. Check if Qubership changes in docker image conflict with new changes with spark operator

#### History server TLS issues 

When unsure if the issue is related to incorrect certificates, it is possible to disable certificate validation. See [installation.md](/docs/public/installation.md) on how to disable certificate validation for postgres and s3.

#### Oauth 2 proxy issues

When troubleshooting issues related to Oauth2proxy/keycloak it is necessary to make sure that all parameters are correct(including various URLs) both on oauth2proxy side and on keycloak side. Also it is necessary to check keycloak and oauth2proxy logs.

#### Problems with image size

Spark images are pretty large and include pretty big JARs. To avoid unnecessary image size increases it is necessary to follow dockerfile best practices, for example: do not change file permissions in separate RUN steps or do not download and unpack archive in different RUN commands. If the issue is with custom application image, it is also necessary to check custom application dockerfile for the same issues or if they upload the same jars that are already present in the image.

## Evergreen strategy

1) Check if new community spark-operator image is available. If it is, update [qubership spark-operator image dockerfile](/spark-operator-image/Dockerfile) to this new version. **Note**: if newer version of spark operaor is not available, or does not include newer spark version, it might be required to build spark-operator image completely form scratch.
2) Update [spark operator chart](/docker-transfer/Dockerfile) based on community chart latest release.
3) Update the chart-version in the pipeline .github/workflows/helm-charts-release.yaml when the chart is upgraded.
4) Based on spark version, update base spark docker image for [qubership spark image](/spark-customized/Dockerfile).
5) Check updated jar list in [qubership spark image](/spark-customized/Dockerfile) and in [qubership spark-operator image dockerfile](/spark-operator-image/Dockerfile). Need to check, if these jars versions changed in new spark release compared to current spark release. If jar version is changed, but it still not as new as in Dockerfile, it is necessary to modify dockerfiles to remove jar with the version from new spark release. If the jar versions in new spark release are newer than in Dockerfile, it is necessary to remove the logic with this jar both from dockerfile.
6) Check vulnerabilities for updated Qubership spark image. If there are some java libraries vulnerabilities, that can be fixed by patch version update, it is necessary to do a manual update of this jar, old version should be replaced with the new one. Dockerfile should be modified both for spark-operator and spark images in this case. As an example, refer to jackson-mapper-asl that is updated from version 1.9.13 to version 1.9.13-cloudera.4.
7) Check additional jars that are added in spark image: aws-java-sdk-bundle , hadoop-aws, delta-storage and delta-spark. If compatible with updated spark version, these jars should be updated too.
8) Update spark version in documentations, spark applications and spark application dependencies.
9) Check that spark-operator(and volcano integration) still works. Check that history server and thrift server work. Check that spark operator applications with new images and spark version can be executed.
10) Check for new [oauth2-proxy releases](https://github.com/oauth2-proxy/oauth2-proxy/releases) and update oauth2-proxy image in [oauth2-proxy helm chart values override](/spark-history-server/chart/helm/spark-history-server/values.yaml) accordingly
11) Oauth2-proxy container in [spark-history-server deployment](/spark-history-server/chart/helm/spark-history-server/templates/deployment.yaml) and [oauth2proxy folder](/spark-history-server/chart/helm/spark-history-server/templates/oauth2Proxy/) must be updated. It is based on [oauth2 proxy official chart](https://github.com/oauth2-proxy/manifests/tree/main/helm/oauth2-proxy). These files and [spark history server values.yaml](/spark-history-server/chart/helm/spark-history-server/values.yaml) must be updated based on base chart changes.
12) Check that oauth2proxy integration with keycloak still works
13) Update [base tests image](/spark-service-integration-tests/docker/Dockerfile) based on the [latest Qubership release](https://github.com/Netcracker/qubership-docker-integration-tests).
14) Update status provisioner in [values](/chart/helm/spark-on-k8s/values.yaml) based on the [latest Qubership release](https://github.com/Netcracker/qubership-deployment-status-provisioner/releases).
15) Check that tests still run with status provisioner.

## Useful links

* https://github.com/kubeflow/spark-operator kubeflow spark operator github repository
* https://github.com/kubeflow/spark-operator/tree/master/charts/spark-operator-chart spark operator community chart
* https://www.kubeflow.org/docs/components/spark-operator/ spark operator kubeflow docs
* https://hub.docker.com/r/kubeflow/spark-operator/tags spark operator docker image
* https://github.com/apache/spark spark repository
* https://github.com/apache/spark-docker spark docker repository
* https://hub.docker.com/r/apache/spark spark docker image
* https://spark.apache.org/documentation.html spark documentation
* https://spark.apache.org/docs/3.5.5/monitoring.html#spark-history-server-configuration-options spark history documentation
* https://spark.apache.org/docs/3.5.5/sql-distributed-sql-engine.html spark thrift server documentation
* https://issues.apache.org/jira/projects/SPARK/issues apache spark jira
* https://github.com/oauth2-proxy/oauth2-proxy oauth2 proxy repository
* https://github.com/oauth2-proxy/manifests/tree/main/helm/oauth2-proxy oauth2 proxy chart
* https://quay.io/repository/oauth2-proxy/oauth2-proxy oauth2-proxy docker
* https://github.com/Netcracker/qubership-docker-integration-tests- integration tests repository
* https://github.com/Netcracker/qubership-deployment-status-provisioner status provisioner repository