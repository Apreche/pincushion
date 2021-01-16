import os
import dotenv
import pathlib

ENV_PATH = os.environ.get('PINCUSHION_ENV_FILE', None)

if ENV_PATH:
    dotenv.load_dotenv(
        dotenv_path=pathlib.Path(ENV_PATH)
    )

PICKLEDB_FILENAME = os.environ.get('PINCUSHION_DB_FILENAME', 'pincushion.db')

PINBOARD_USERNAME = os.environ.get('PINBOARD_USERNAME', '')
PINBOARD_API_TOKEN = os.environ.get('PINBOARD_API_TOKEN', '')

REDDIT_CLIENT_ID = os.environ.get('REDDIT_CLIENT_ID', '')
REDDIT_CLIENT_SECRET = os.environ.get('REDDIT_CLIENT_SECRET', '')
REDDIT_REFRESH_TOKEN = os.environ.get('REDDIT_REFRESH_TOKEN', '')
REDDIT_USER_AGENT = os.environ.get('REDDIT_USER_AGENT', 'pincushion script')
