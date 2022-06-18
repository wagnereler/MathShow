/* logical: */

CREATE TABLE setting (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INT,
    mode_id INTEGER,
    language_id INTEGER,
    speed INT
);

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCAHR(60),
    age INT,
    selected INT
);

CREATE TABLE mode (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name INT
);

CREATE TABLE lamguage (
    id INTEGER PRIMARY KEYAUTOINCREMENT,
    language VARCHAR(40)
);
 
ALTER TABLE setting ADD CONSTRAINT FK_setting_user
    FOREIGN KEY (fk_user_id, user_id)
    REFERENCES user (id, id);
 
ALTER TABLE setting ADD CONSTRAINT FK_setting_language
    FOREIGN KEY (language_id)
    REFERENCES lamguage (id);
 
ALTER TABLE setting ADD CONSTRAINT FK_setting_mode
    FOREIGN KEY (mode_id)
    REFERENCES mode (id);