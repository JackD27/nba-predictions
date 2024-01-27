import datetime

class Settings:

    VERSION = 0.2

    YEAR = datetime.date.today().year
    APP_NAME = "NBA DK Basketball Lines"

    GITHUB_API_URL = "https://api.github.com/repos/JackD27/nba-predictions"
    GITHUB_URL = "https://github.com/JackD27/nba-predictions"
    GITHUB_URL_README = "https://github.com/JackD27/nba-predictions#readme"


    ABOUT_TEXT = "Version {}  © {}".format(VERSION, YEAR)

    WIDTH = 300  
    HEIGHT = 200

    MAX_WIDTH = 250  
    MAX_HEIGHT = 250