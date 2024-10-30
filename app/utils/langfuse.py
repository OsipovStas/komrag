from langfuse.callback import CallbackHandler


def langfuse_handler(config):
    return CallbackHandler(
        public_key=config.pk,
        secret_key=config.sk,
        host=config.host
    )

