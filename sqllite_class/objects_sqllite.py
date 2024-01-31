from class_sqllite import Database_Sqlite
base = Database_Sqlite()

# base.create_table("uquvchilar",("id","INTEGER"),("ism","TEXT"),("familiya","TEXT"))

# base.insert_uquvchi(1,"Shoxjaxon","Atabayev")

base.Sql_To_Txt_Docx("uquvchilar")

# print(base.uqish("uquvchilar"))