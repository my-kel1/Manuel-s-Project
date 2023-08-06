import sqlite3


class mainDb:

    list_info = []
    list_medication_incomplete = []
    list_medication_complete = []

    list_time = []

    list_inProgress = 0
    list_completed = 0
    list_notTaken = 0

    progress = []

    value = ''

    medName = ''
    prog = ''
    time = ''
    r = ''
    a = ''

    def __init__(self):

        self.conn = sqlite3.connect('information.db')
        self.cursor = self.conn.cursor()

    def create_table_info(self):

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS info(
                            medicine_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            Medicine TEXT,
                            Days_Intake TEXT,
                            Time_Intake TEXT,
                            Days_Remaining TEXT,
                            Progress TEXT)''')

        self.conn.commit()

    def insert_data_info(self, data):

        data_list = [None]

        remD = ''
        progress = ''

        for a in data:
            for b in a:
                data_list.append(b)

        remD = data_list[2]
        data_list.append(remD)

        if int(remD) > 0:
            progress = 'Incomplete'
        else:
            progress = 'Complete'

        data_list.append(progress)
        addData = [tuple(data_list)]
        print(addData)

        self.cursor.executemany('INSERT INTO info (medicine_id, Medicine, Days_Intake, Time_Intake, Days_Remaining, Progress) VALUES (?,?,?,?,?,?)', addData)
        self.conn.commit()

    def fetch_data_info(self):

        try:
            mainDb.list_medication_complete.clear()
            mainDb.list_medication_incomplete.clear()

            data = self.cursor.execute("SELECT rowid, * FROM info")
            get = data.fetchall()

            for info in get:
                if info[6] == "Incomplete":
                    mainDb.list_medication_incomplete.append(str(info[2]).capitalize())
                else:
                    mainDb.list_medication_complete.append(str(info[2]).capitalize())

            self.conn.commit()
        except:
            pass

    def fetch_time(self):

        data = self.cursor.execute("SELECT rowid, * FROM info")
        get = data.fetchall()

        t = ''

        for info in get:
            if info[5] != 1:
                t += info[4]

        l = t.split(';')
        mainDb.list_time += l

        self.conn.commit()

    def pullData(self):

        data = self.cursor.execute("SELECT rowid, * FROM info")
        get = data.fetchall()

        for x in get:
            if mainDb.value == x[2]:
                mainDb.medName = str(x[2]).upper()
                mainDb.prog = str(x[6]).capitalize()
                mainDb.time = str(x[4])
                mainDb.r = str(x[5])
                mainDb.a = str(x[3])
            else:
                pass

            self.conn.commit()

    def close_conn_info(self):

        self.conn.close()


'''p = addData()
p.fetch_time()
print(p.list_time)'''
