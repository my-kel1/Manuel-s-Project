import sqlite3


class notification:

    notif_list = []

    def __init__(self):
        self.conn = sqlite3.connect('notifs.db')
        self.cursor = self.conn.cursor()

    def create_table_notifs(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS notifs(
                                    notifs_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    notification TEXT,
                                    date TEXT)''')
        self.conn.commit()

    def insert_notif(self, data):

        data_list = [None]

        for a in data:
            for b in a:
                data_list.append(b)

        addData = [tuple(data_list)]

        self.cursor.executemany('INSERT INTO notifs (notifs_id, notification, date) VALUES (?,?,?)', addData)
        self.conn.commit()

    def pull_notif(self):

        notification.notif_list.clear()

        data = self.cursor.execute("SELECT rowid, * FROM notifs")
        get = data.fetchall()

        for notif in get:
            notification.notif_list.append(notif[2] + " " + f'({notif[3]})')

    def close_conn_notif(self):

        self.conn.close()

'''p = notification()

p.create_table_notifs()

now = datetime.datetime.now()

data = [('Biogesic has been taken!', now)]
p.insert_notif(data)'''
