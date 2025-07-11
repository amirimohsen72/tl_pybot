import sqlite3

MAIN_DB = sqlite3.connect('test_db.db',check_same_thread=False)
MAIN_CURSOR = MAIN_DB.cursor()




MAIN_CURSOR.execute(
    '''CREATE TABLE table_name (
    chatid varchar(255),
    amount int(20),
    status varchar(255)
);'''
)


MAIN_DB.commit()