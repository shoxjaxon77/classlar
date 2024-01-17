from wordclass import Word

file = Word("word")

file.add_text("Shoxjaxon")
file.add_text("Atabayev")

file.add_heading("HEADING")
file.add_text("Qudratovich")

print("Ma'lumotlar: ",file.read_text(),'\n')

print("Birinchi paragraf: ",file.first_paragraph(),'\n')

print("Massiv: ",file.massiv(),'\n')

print("Nomi: ",file,'\n')
print("n-chi paragraf: ",file(2),'\n')

file.save('word.docx')