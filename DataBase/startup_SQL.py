from DataBase.database_SQL import ConnectDataBase
from DataBase.setting_screen_SQL import CreateScreenSettings


class Startup:
    def __init__(self):
        start_connection = ConnectDataBase()
        start_connection.create_table()
        start_connection.inserting_user_default()

        start_screen_settings = CreateScreenSettings()
        start_screen_settings.inserting_screen()

