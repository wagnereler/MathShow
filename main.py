import os
from kivymd.app import MDApp
from kaki.app import App
from kivy.factory import Factory
from DataBase.startup_SQL import Startup

Startup()



# main app class for kaki app with kivymd modules
class MathShow(MDApp, App):
    """ Hi Windows users """

    DEBUG = 1 # set this to 0 make live app not working

    # *.kv files to watch
    KV_FILES = {
        os.path.join(os.getcwd(), "View/screen_manager.kv"),
        os.path.join(os.getcwd(), "View/user/user_screen.kv"),
    }

    # class to watch from *.py files
    CLASSES = {
        "MainScreenManager": "View.screen_manager",
        "UserScreen": "View.user.user_screen",
    }

    # auto reload path
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]


    def build_app(self):
        return Factory.MainScreenManager()


#start = ConnectDataBase()

# finally, run the app
if __name__ == "__main__":
    MathShow().run()

