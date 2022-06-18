from sqlite3 import connect
from os import path, getcwd


class ConnectDataBase:
    connection = None

    def __init__(self, db_fine=None):
        if db_fine is not None:
            self.connection = connect(db_fine)
        else:
            self.connection = connect(path.join(getcwd(), 'DataBase/math-show.db'))
        self.cur = self.connection.cursor()
        self.criarTabelas()

    def criarTabelas(self):
        query_create_tables = \
            """
                CREATE TABLE IF NOT EXISTS user (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCAHR(60),
                    age INT,
                    selected INT
                );
                
                CREATE TABLE IF NOT EXISTS mode (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name INT
                );
                
                CREATE TABLE IF NOT EXISTS setting (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INT,
                    mode_id INTEGER,
                    language_id INTEGER,
                    speed INT
                    
                    CONSTRAINT FK_setting_user,
                    FOREIGN KEY (user_id)
                    REFERENCES user (id)
                    
                    CONSTRAINT FK_setting_language
                    FOREIGN KEY (language_id)
                    REFERENCES lamguage (id)
                    
                    CONSTRAINT FK_setting_mode
                    FOREIGN KEY (mode_id)
                    REFERENCES mode (id)
                );
                """
        self.cur.execute(query_create_tables)
        self.cur.close()
