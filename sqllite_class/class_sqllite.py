import sqlite3

class Database_Sqlite:
    def __init__(self,path = "talaba.db"):
        self.path = path

    def ulanish(self):
        return sqlite3.connect(self.path)
    
    def ishlatish(self,sql,fetchone=False,fetchall=False,commit=False):
        db = self.ulanish()
        cursor  = db.cursor()
        cursor.execute(sql)
        data = None

        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        if commit:
            db.commit()
        db.close()
        return data
    
    def create_table(self, table_name, *ustun):
        a = ', '.join([f'{i[0]} {i[1]}' for i in ustun])
        sql = f"CREATE TABLE {table_name} ({a})"
        self.ishlatish(sql, commit=True)


    def Sql_To_Txt_Docx(self,table_name):
        sql = f"SELECT * FROM '{table_name}'"
        a = self.ishlatish(sql,fetchall=True)

        self.txt = File("text")
        self.txt.write_text(a)

        self.file = Docx("word")
        self.file.write_text(a)

    def uqish(self,table_name):
        sql = f"SELECT * FROM '{table_name}'"
        return self.ishlatish(sql,fetchall=True)
        


from docx import Document
class Docx:
    def __init__(self,name):
        self.name = name
        self.doc = Document()

    def write_text(self,a):
        for i in a:
            self.doc.add_paragraph(str(i))
        self.saqlash('word.docx')

    def saqlash(self,manzil):
        self.doc.save(manzil)


class File:
    def __init__(self,name):
        self.name = name
        with open(f"{self.name}","w"):
            pass
    
    def write_text(self,matn):
        with open(f"{self.name}","w") as f:
            f.write(str(matn))

