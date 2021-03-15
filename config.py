import os
# TODO: Add env vars depending on the env
DEBUG = os.environ.get('DEBUG') or True
SECRET_KEY = os.environ.get('SECRET_KEY') or 'development key'

VONAGE_KEY = os.environ.get('VONAGE_KEY')
VONAGE_SECRET = os.environ.get('VONAGE_SECRET')
NOTIFICATIONS_ENABLED = os.environ.get('NOTIFICATIONS_ENABLED') or False
