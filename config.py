import dotenv
import os

dotenv.load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_LOGIN = os.getenv('DB_LOGIN')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
BOT_TOKEN = os.getenv('BOT_TOKEN')