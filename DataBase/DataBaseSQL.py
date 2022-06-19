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

    def save(self):
        self.connection.commit()

    def __del__(self):
        self.connection.close()

    def create_table(self):
        create_user_tb = \
            """
                CREATE TABLE IF NOT EXISTS user (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    selected BOOLEAN DEFAULT (1) NOT NULL
);
            """
        create_mode_tb = \
            """
                CREATE TABLE IF NOT EXISTS mode (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT
                );
            """
        create_language_tb = \
            """
                CREATE TABLE IF NOT EXISTS language (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                );
            """
        create_setting_tb = \
            """
                CREATE TABLE IF NOT EXISTS setting (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    mode_id INTEGER,
                    language_id INTEGER,
                    speed INT
                    
                    CONSTRAINT FK_setting_user,
                    FOREIGN KEY (user_id)
                    REFERENCES user (id)
                    
                    CONSTRAINT FK_setting_language
                    FOREIGN KEY (language_id)
                    REFERENCES language (id)
                    
                    CONSTRAINT FK_setting_mode
                    FOREIGN KEY (mode_id)
                    REFERENCES mode (id)
                );
            """
        create_screen_tb = \
            """
                CREATE TABLE IF NOT EXISTS screen (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT	
                );
            """

        create_object_screen_tb = \
            """
                CREATE TABLE IF NOT EXISTS object_screen (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    text_object TEXT,
                    name TEXT,
                    language_id,
                    screen_id,
                    
                    CONSTRAINT FK_object_screen_language
                    FOREIGN KEY (language_id)
                    REFERENCES language (id)
                    
                    CONSTRAINT FK_object_screen_screen
                    FOREIGN KEY (screen_id)
                    REFERENCES screen (id)
                    
                );
            """
        create_trigger = \
            """
                --CREATE TRIGGER FOR INSERTED USER
                CREATE TRIGGER tg_user_inserted
                         BEFORE INSERT
                            ON user
                      FOR EACH ROW
                BEGIN
                    UPDATE user SET selected = 0;
                END;
                
                --CREATE TRIGGER FOR UPDATE USER
                CREATE TRIGGER tg_user_updated
                         BEFORE UPDATE OF selected
                            ON user
                      FOR EACH ROW
                WHEN NEW.selected = 1
                BEGIN
                    UPDATE user
                       SET selected = 0;
                END;	
                
                --CREATE TRIGGER FOR DELETE USER
                CREATE TRIGGER tg_user_deleted
                         AFTER DELETE
                            ON user
                      FOR EACH ROW
                WHEN OLD.selected = 1
                BEGIN
                    UPDATE user
                       SET selected = 1
                    WHERE id = (SELECT id FROM user LIMIT 1); 
                END; 
                
                --CREATE TRIGGER FOR DELETE LEST USER
                CREATE TRIGGER tg_user_deleted_lest
                         BEFORE DELETE
                            ON user
                      FOR EACH ROW
                WHEN ((SELECT COUNT(*) FROM user) = 1)
                BEGIN
                    SELECT RAISE(ABORT, 'This is  the unique registered user. You can''t remove!');
                END;
            """
        try:
            self.connection.execute(create_user_tb)
            self.connection.execute(create_mode_tb)
            self.connection.execute(create_language_tb)
            self.connection.execute(create_setting_tb)
            self.connection.execute(create_screen_tb)
            self.connection.execute(create_object_screen_tb)
            self.connection.executescript(create_trigger)
            self.save()
        except Exception as error:
            return f'An error occurred while creating the table: {error}'
        return True

