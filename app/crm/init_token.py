import os

from amocrm.v2 import tokens
from dotenv import load_dotenv

from app.crm.setup_amocrm import setup_amocrm


def init_token() -> None:
    load_dotenv()
    code = os.getenv("AMOCRM_CODE")
    if not code:
        raise ValueError("AMOCRM_CODE environment variable is not set")
    setup_amocrm()
    tokens.default_token_manager.init(code=code, skip_error=False)


if __name__ == '__main__':
    init_token()
