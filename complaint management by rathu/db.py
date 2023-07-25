import sqlite3

class Project:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
            CREATE TABLE IF NOT EXISTS complaint (
            id Integer Primary key AUTOINCREMENT,
            name varchar ,
            gender varchar ,
            comment varchar 
        )
        """
        self.cur.execute(sql)
        self.con.commit()

        #insert
    def insert(self, name, gender, comment):
        self.cur.execute("insert into  complaint(name, gender, comment) values(?,?,?)",
                             (name, gender, comment))
        self.con.commit()

    def fetch(self):
        self.cur.execute("select * from complaint")
        rows=self.cur.fetchall()
        return rows


