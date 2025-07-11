from dotenv import load_dotenv
import os

# Carga variables del archivo .env
load_dotenv()
class Config:
    SECRET_KEY = 'CLAVE'
    MYSQL_HOST = os.getenv('MYSQL_HOST')
    MYSQL_USER = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
    MYSQL_DB = os.getenv('MYSQL_DB')
    MYSQL_PORT = int(os.getenv('MYSQL_PORT'))
    SESSION_COOKIE_SECURE: False
    