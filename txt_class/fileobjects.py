from fileclass import File

file = File("text.txt")
print(file.read_text())

file.write_text("""salom dunyo!
hello world!
privet!
qwerty
Merhaba!""")
print(file.read_text())

file2 = File("new_file.txt")
file.new_file(1,3)
file2.read_text()

print('\n'+ file.first_row())

file.add_text(" shoxjaxon")
print(file.read_text())
print()

print(file.massiv())
print()

file.del_abzas()
print(file.read_text())
print()

print(file)
print()

print(file[3])
print()

file[1] = "O'zgartiririldi"
print(file[1])
print()

print(file.upper_word())
print()

file.upper_row()
print(file.read_text())

file.del_row(2)
print(file.read_text())

print("berilgan qator: ",file.get_row(2))
print()

file.del_rows(4,5)
print(file.read_text())

file.get_rows(2,4)
print(file.read_text())



file.padding_left(4)
print(file.read_text())