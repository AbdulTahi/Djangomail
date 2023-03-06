import os
from dotenv import load_dotenv

# without environment variables -> this is very unsafe!
GMAIL_EMAIL = 'aattahir4@gmail.com'
GMAIL_PASSWORD = 'shadow134'

# with environment variables   -> this is much safer!
path_to_env_file = './.env'
load_dotenv(path_to_env_file)   # or just load_dotenv() if .env is in the same folder

GMAIL_EMAIL = os.getenv('GMAIL_USER_EMAIL')
GMAIL_PASSWORD = os.getenv('GMAIL_USER_PASSWORD')