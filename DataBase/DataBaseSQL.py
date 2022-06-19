from sqlite3 import Connection, connect
from os import path, getcwd


class ConnectDataBase(Connection):
    connection = None
    DB_FILE = path.join(getcwd(), 'DataBase/math-show.db')

    def __init__(self, db_fine=None):
        if db_fine is not None:
            self.connection = connect(db_fine)
        else:
            self.connection = connect(self.DB_FILE)
        cur = self.connection.cursor()

    def save(self):
        self.connection.commit()

    def __del__(self):
        self.connection.close()

    def create_table(self):
        create_user_tb = \
            """
                CREATE TABLE IF NOT EXISTS user (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCAHR(60),
                    age INT,
                    selected INT
                );
            """
        create_mode_tb = \
            """
                CREATE TABLE IF NOT EXISTS mode (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name INT
                );
            """

        create_setting_tb = \
            """
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
        try:
            self.cur.execute(create_user_tb, create_mode_tb, create_setting_tb)
            self.save()
        except Exception as error:
            return f'Erro ao criar tabela => {error}'

        return True
