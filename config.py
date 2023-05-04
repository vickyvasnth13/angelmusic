from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/62bc6b35112b8e8bdfc19.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/d0cb7951df680d6e0a710.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/solotreee")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/solotreee")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1338408261").split()))


FAILED = "https://te.legra.ph/file/c9a49cb4fdc8a2296be72.jpg"
