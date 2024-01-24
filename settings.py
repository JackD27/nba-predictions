import datetime

class Settings:
    VERSION = "0.1"
    YEAR = datetime.date.today().year
    APP_NAME = "NBA DK Basketball Lines"

    GITHUB_API_URL = "?"
    GITHUB_URL = "?"
    GITHUB_URL_README = "?"


    ABOUT_TEXT = "Version {}  © {}".format(VERSION, YEAR)

    WIDTH = 300  
    HEIGHT = 200

    MAX_WIDTH = 600  
    MAX_HEIGHT = 500