FROM ghcr.io/netcracker/qubership-docker-integration-tests:0.2.2

ENV ROBOT_OUTPUT=/opt/robot/output

RUN mkdir -p ${ROBOT_OUTPUT}


COPY spark-service-integration-tests/docker/requirements.txt ${ROBOT_HOME}/requirements.txt
COPY spark-service-integration-tests/robot ${ROBOT_HOME}

# ToDo add other apps
COPY docs/public/examples/app-crs/spark-py-pi.yaml  ${ROBOT_HOME}/tests/test-app
COPY docs/public/examples/app-crs/spark-pi.yaml  ${ROBOT_HOME}/tests/test-app
COPY docs/public/examples/app-crs/spark-pi-long-run.yaml  ${ROBOT_HOME}/tests/test-app
COPY docs/public/examples/app-crs/spark-pi-event-logs-s3.yaml  ${ROBOT_HOME}/tests/test-app

# ToDo add examples copy

RUN set -x \
    && pip3 install --no-cache-dir -r ${ROBOT_HOME}/requirements.txt \
    && rm -rf /var/cache/apk/*

USER 1000:0

EXPOSE 8080
VOLUME ["${ROBOT_OUTPUT}"]
