import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "23863563"))
    API_HASH = os.environ.get("API_HASH", "2923da75525a566b9e9bc964642ff921")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6379844676:AAGUNAgJaC2gr6Fmmv68R_YIIheV_sJfcUc")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOJ8Buz8x0xP00M07Vsy-inXVkZeV-ArwbtwxiUtSkqIqc6Ff3d2Ivtszlf_H-UVUh3fL7UJ0BKOglYeR_yQ9O3JeSd3h_nyB1QKLBPGWTD1f6g2ZtEpKqLrf8d6B5Ekhh5v-8TAZ37NhKzIdW9AxHqTtRxiTq0i0_quxFXwY-_ROaTDIhS29Iizn8N6ad73io7JfU5bRQYp1Wg5qGlWd9YeNnkauoxkv71aTNPTfVCrePbf1Tuy_CyBUG37gFJ3SrKsIfUFxfLAAGxjVpr5SQFnqJe-rSAahuqOT1xBho67YE7fpRoHL-OUhIKXON79dsuEa5LJ_J8D727e3wfcO9DhDUBE=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Alia_MusicBot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://i.ibb.co/G94LHQG/photo-2023-07-18-19-39-53.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://i.ibb.co/PGFHWDr/MUSIC-BOT.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6343636554")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
