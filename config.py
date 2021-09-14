from os import path, getenv
from dotenv import load_dotenv

if path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
BOT_TOKEN = getenv("BOT_TOKEN", None)
API_ID = int(getenv("API_ID", "6"))
API_HASH = getenv("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
SESSION_NAME = getenv("SESSION_NAME", None)
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
DB_URL = getenv("DB_URL", None)
DB_NAME = getenv("DB_NAME", "my")
BOT_USERNAME = getenv("BOT_USERNAME", "your username")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
