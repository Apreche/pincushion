import os

PICKLEDB_FILENAME = os.environ.get('PINCUSHION_DB_FILENAME', 'pincushion.db')

PINBOARD_USERNAME = os.environ.get('PINBOARD_USERNAME', '')
PINBOARD_API_TOKEN = os.environ.get('PINBOARD_API_TOKEN', '')

REDDIT_CLIENT_ID = os.environ.get('REDDIT_CLIENT_ID', '')
REDDIT_CLIENT_SECRET = os.environ.get('REDDIT_CLIENT_SECRET', '')
REDDIT_REFRESH_TOKEN = os.environ.get('REDDIT_REFRESH_TOKEN', '')
REDDIT_USER_AGENT = os.environ.get('REDDIT_USER_AGENT', 'pincushion script')
