import os

from amocrm.v2 import tokens


def setup_amocrm() -> None:
    client_id = os.getenv("AMOCRM_CLIENT_ID")
    if not client_id:
        raise ValueError("AMOCRM_CLIENT_ID environment variable is not set")

    client_secret = os.getenv("AMOCRM_CLIENT_SECRET")
    if not client_secret:
        raise ValueError("AMOCRM_CLIENT_SECRET environment variable is not set")

    subdomain = os.getenv("AMOCRM_SUBDOMAIN")
    if not subdomain:
        raise ValueError("AMOCRM_SUBDOMAIN environment variable is not set")

    redirect_url = os.getenv("AMOCRM_REDIRECT_URL")
    if not redirect_url:
        raise ValueError("AMOCRM_REDIRECT_URL environment variable is not set")
    src_dir = os.path.normpath(os.path.join(__file__, os.path.pardir))

    tokens.default_token_manager(
        client_id=client_id,
        client_secret=client_secret,
        subdomain=subdomain,
        redirect_url=redirect_url,
        storage=tokens.FileTokensStorage(src_dir)
    )

