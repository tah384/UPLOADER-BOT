import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7355006985:AAEY8ijg4CP-8GgcliRGJja87Tby78QT7To")
    # The Telegram API things
    API_ID = int(os.environ.get("API_ID", "29426486"))
    API_HASH = os.environ.get("d71ad4ec048ab41677a1a439b21ff0c9")
    # Get these values from my.telegram.org
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 4194304000 #2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(128)
    # default thumbnail to be used in the videos
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ""
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # your telegram id
    OWNER_ID = int(os.environ.get("OWNER_ID", "5976437467"))
    SESSION_NAME = "Itxmety73_bot"
    # database uri (mongodb)
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://taha16511:4uPo1wMZxKzrqobP@cluster0.dvlwfxx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    MAX_RESULTS = "50"
    PREMIUM_USER = os.environ.get("5976437467")
