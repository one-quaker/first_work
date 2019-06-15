FROM onepycoder/python:3.7.2.25

ENV TZ=Europe/Kiev
ARG DEV_DIR=dev

USER $USER
WORKDIR $APP_DIR
COPY ./src/requirements.txt $APP_DIR
RUN $ENV_PIP_BIN install -U pip --no-cache-dir && $ENV_PIP_BIN install -r requirements.txt --no-cache-dir

# add entrypoint script
USER root
COPY $DEV_DIR/entrypoint.sh /entrypoint.sh
RUN chmod 755 /entrypoint.sh
USER $USER

ENTRYPOINT ["/bin/zsh", "/entrypoint.sh"]
