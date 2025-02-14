from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('TOKEN')
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
ME = os.getenv('ME')

DATABASE_URL = os.getenv('DATABASE_URL_POSTGRES')
# DATABASE_URL = os.getenv('DATABASE_URL_SQLITE')

BACKEND_PREFIX = 'api_v1_'
