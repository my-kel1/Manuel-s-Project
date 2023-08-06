import sqlite3


class prog:

    taken = 0
    notTaken = 0

    def __init__(self):

        self.conn = sqlite3.connect('progress.db')
        self.cursor = self.conn.cursor()

    def create_table_progress(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS progress(progress TEXT)''')
        self.conn.commit()

    def insert_progress(self, data):

        self.cursor.execute('INSERT INTO progress (progress) VALUES (?)', data)
        self.conn.commit()

    def fetch_progress(self):

        data = self.cursor.execute("SELECT rowid, * FROM progress")
        get = data.fetchall()

        for x in get:
            if x[1] == 'taken':
                prog.taken += 1
            elif x[1] == 'notTaken':
                prog.notTaken += 1
            else:
                pass

        self.conn.commit()

    def close_conn_info(self):
        self.conn.close()


'''a = prog()
a.fetch_progress()'''