from mysql_class import Database

base = Database()

print("KURS NOMLARI:",'\n',base.kurslar_nomi())

print("Berilgan id dagi kurs ma'lumotlari: ",'\n',base.kurs_nomi(2))

print("O'qituvchilar ism familiyasi:",'\n',base.uqituvchilar_fio())

print("Berilgan so'z qatnashgan ismlar:",'\n',base.search_uquvchi("or"))

print("Berilgan kursga qatnashuvchi o'quvchilar ro'yxati:",'\n',base.count_kurs_uquvchilar("Kompyuter grafikasi"))

print("Berilgan o'qituvchining kurslari:","\n",base.uqituvchi_kurslari("Janar","Yusupova"))

print("Berilgan o'qituvchining o'quvchilari:","\n",base.uqituvchi_uquvchilari("Janar","Yusupova"))

print("Berilgan o'quvchining o'qituvchisi:",'\n',base.uquvchi_uqituvchisi("Umida","Tajiyeva"))

print("Berilgan id dagi kursning o'quvchilar soni:",'\n',base.kurs_uquvchilari(2))

print("Berilgan sanada amalga oshirilgan to'lovlar soni:",'\n',base.count_tulovlar("2023-12-05"))

print("Berilgan sanada amalga oshirilgan to'lovlar summasi:",'\n',base.sum_tulovlar("2024-01-04"))

print("Berilgan sanalar oralig'idagi to'lovlar summasi:",'\n',base.sum_sanalar_tulovi("2024-01-04","2024-01-10"))

print("Berilgan id dagi o'qituvchi uchun o'tkazilgan to'lovlar summasi:",'\n',base.sum_uqituvchi_tulovlari(8,"2023-12-05","2024-01-04"))

print("Berilgan sanada amalga oshirilgan to'lovlar soni:",'\n',base.sum_uquvchi_tulovlari(5))

base.kurs_narxini_oshirish(1,3,10)

base.insert_kurslar("Malumotlarbazasi",350000,"8 oy")

base.insert_uquvchilar("Shoxjaxon","Atabayev","2004-09-02","+998904313414")

base.insert_uqituvchilar("Atabayev","Shoxjaxon","Malumotlarbazasi","+998904313414")

base.insert_yulov("Umida","Tajiyeva",200000,"ingliz tili")

base.change_dars_vaqti("Janar","Yusupova","15:00:00")
