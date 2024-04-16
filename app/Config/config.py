from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("secret")
ALGORITHM = os.getenv("algorithm")
API_TOKEN = os.getenv("API_TOKEN")
