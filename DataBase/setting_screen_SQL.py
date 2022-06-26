from DataBase.database_SQL import ConnectDataBase


class CreateScreenSettings(ConnectDataBase):
    def inserting_screen(self):
        insert_user_default = "INSERT INTO screen (name) VALUES ('settings');"
        if self.check_initial_load('screen', 'WHERE id = 1'):
            try:
                self.cur.execute(insert_user_default)
                self.save()
            except Exception as error:
                return f'An error occurred while inserting in table: {error}'
            self.initial_load = False
            return True

    def inserting_object_screen(self):
        insert_user_default = """INSERT INTO object_screen (text_object, name, language_id, screen_id)
VALUES (
     ('Mode', 'mode', 1, 1)  
);"""
        if self.check_initial_load('object_screen', 'WHERE id_screen = 1'):
            try:
                self.cur.execute(insert_user_default)
                self.save()
            except Exception as error:
                return f'An error occurred while inserting in table: {error}'
            self.initial_load = False
            return True
