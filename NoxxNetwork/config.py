import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config(object):
    LOGGER = True

    OWNER_ID = os.getenv("7850114307")
    sudo_users = os.getenv("SUDO_USERS").split(",")  # Convert CSV to list
    GROUP_ID = int(os.getenv("waifissupprt1v"))
    TOKEN = os.getenv("8356850655:AAFgnKPlT6HECSYTaoAFSXRtTCnG4-YAg0A")
    mongo_url = os.getenv("mongodb+srv://sk5400552:shjjkytdcghhudd@cluster0g.kbllv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0g")
    PHOTO_URL = os.getenv("PHOTO_URL").split(",")  # Convert CSV to list
    SUPPORT_CHAT = os.getenv("waifussupports")
    UPDATE_CHAT = os.getenv("waifussupports")
    BOT_USERNAME = os.getenv("Ejejjeejjeierbot")
    CHARA_CHANNEL_ID = int(os.getenv("-1002943967320"))
    api_id = int(os.getenv("24411134"))
    api_hash = os.getenv("da78963da6eaaf521133e00628434271")


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
