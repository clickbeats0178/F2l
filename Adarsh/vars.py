# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '29802408'))
    API_HASH = str(getenv('API_HASH', 'a6f4235751213eb700d6ef19be1a4135'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', '6811161053:AAEzhksqnL4iS_Q9-VDgbRKj2btYG_J6WQY'))
    name = str(getenv('name', 'cbftolinkbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1001989781600'))
    PORT = int(getenv('PORT', '8080'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "969099516").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'kumarvalimaibot'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', 'BIND_ADRESS:PORT')) if not ON_HEROKU or getenv('FQDN', '') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://daaaavudaaaa_info1:daaaavudaaaa_info1@cluster0.ookasqc.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'ClickBeatsBackup'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split()))      
    SHORTLINK_URL = getenv('SHORTLINK_URL', 'tnshort.net')
    SHORTLINK_API = getenv('SHORTLINK_API', '9e22f4ec501955eae01db2fe82e76e029b706467')
    TUTORIAL_URL = getenv('TUTORIAL_URL', 'https://t.me/ClickBeatsWatchingProcess')
