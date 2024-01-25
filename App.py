import tkinter
import tkinter.messagebox
import requests
import webbrowser
import sys
from DK import DraftKingsWebsite
from settings import Settings

class GUI(tkinter.Tk):
    def __init__(self):
        dk = DraftKingsWebsite()
        tkinter.Tk.__init__(self)
        self.title(Settings.APP_NAME)
        self.resizable(True, True)
        self.minsize(Settings.WIDTH, Settings.HEIGHT)
        self.maxsize(Settings.MAX_WIDTH, Settings.MAX_HEIGHT)
        self.updateLabel()
        tkinter.Button(self, text="Download DraftKings Lines", command=dk.get_dataframe).pack(pady=40)
        tkinter.Label(self, text=Settings.ABOUT_TEXT).pack(side="bottom")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def check_for_updates(self):
        try:
            response = requests.get(Settings.GITHUB_API_URL + "/releases/latest")
            latest_version = response.json()["tag_name"]
            if float(latest_version) > Settings.VERSION:
                return True
            else:
                return False
        except Exception as err:
            sys.stderr.write(str(err) + "/n")
            return
    
    def updateLabel(self):
        if self.check_for_updates():
            tkinter.Label(self, text="Update Available").pack(side="top", anchor="w")
        else:
            return
        
    def on_close(self):
        if self.check_for_updates():
            answer = tkinter.messagebox.askyesno(title=Settings.APP_NAME,message= "A new version of this app is available. \n\n" + "Do you want to download it?")
            if answer is True:
                webbrowser.open(Settings.GITHUB_URL + "/releases/latest")
                self.destroy()
            else:
                self.destroy()
        else:   
            self.destroy()
