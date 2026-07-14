import os
from os import chdir


path = os.getcwd()
os.chdir(r"C:\Users\I.Koval\Desktop")
print(os.getcwd())


full_path = os.path.join("project", "data", "user.text")
print("Созданный путь: ", full_path)

if os.path.exists(full_path):
    print("Файл найден!")
else:
    print("Файла нет")

files = os.listdir(".")

for n, v in enumerate(files):
    print(n, "-", v)

rel_path = "Казахский.docx"
absolute_path = os.path.abspath(rel_path)
print(absolute_path)

if os.path.exists(absolute_path):
    size_in_bate = os.path.getsize(absolute_path)
    size_in_mb = size_in_bate / 1024 / 1024
    print(f"Размер файла: {size_in_mb:.2f} МБ")


