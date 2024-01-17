from excelclass import Excel

file = Excel("fayl.xlsx")

file.write_cell('A1',"salom")
file.write_cell('A3',"Shoxjaxon")
file.read_text()
print()

file.add(1,2,3,4,5)
file.read_text()
print()

file.qushish("A1","A3","C2")
file.read_text()
print()

file.massiv('A3','C4')
print()

file.del_cell('A1')
file.read_text()
print()

print("Nomi: ",file)

print("Berilgan adressdagi ma'lumot: ",file('A4'))

file.saqlash("fayl.xlsx")