from os import environ 

class Config:
    API_ID = environ.get("API_ID", "13780671")
    API_HASH = environ.get("API_HASH", "4fabad9cfab232845ad54d16e5b312d4")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7070039100:AAG5ijx1I2bcR7_bRsIEWod1EyO1xBJgr3A") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://Spyder67:Spyder67@cluster0.smd22ya.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '2112247533').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
