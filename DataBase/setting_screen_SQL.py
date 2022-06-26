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
VALUES ('Mode', 'label_mode', 1, 1),
       ('Modo', 'label_mode', 2, 1),
       ('Modo', 'label_mode', 3, 1),
       ('Mode selected:', 'label_info_mode', 1, 1),
       ('Modo selecionado:', 'label_info_mode', 2, 1),
       ('Modo seleccionado:', 'label_info_mode', 3, 1),
       ('Select or create user', 'label_create_user', 1, 1),
       ('Selecione ou crie usuário', 'label_create_user', 2, 1),
       ('Seleccionar o crear usuario:', 'label_create_user', 3, 1),
       ('Choice the speed', 'label_choice_speed', 1, 1),
       ('Escolha a velocidade', 'label_choice_speed', 2, 1),
       ('Elige la velocidad', 'label_choice_speed', 3, 1),
       ('Speed selected', 'label_info_speed', 1, 1),
       ('Velocidade selecionada', 'label_info_speed', 2, 1),
       ('Velocidad seleccionada:', 'label_info_speed', 3, 1),
       ('Choice the language', 'label_choice_language', 1, 1),
       ('Escolha o idioma', 'label_choice_language', 2, 1),
       ('Elección del idioma', 'label_choice_language', 3, 1)
;"""
        if self.check_initial_load('object_screen', 'WHERE id_screen = 1'):
            try:
                self.cur.execute(insert_user_default)
                self.save()
            except Exception as error:
                return f'An error occurred while inserting in table: {error}'
            self.initial_load = False
            return True
