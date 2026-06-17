import os
from os import chdir

current_dir = os.getcwd()
print(f"Сейчас я работаю в папке: {current_dir}")

os.chdir(r"C:\Users\I.Koval\Desktop")

print("Стало: ", os.getcwd())

content = os.listdir(r"C:\Users")

for i, v in enumerate(content):
    print(i,'-', v)
os.chdir(r"C:\Users\I.Koval\Desktop")
print(os.getcwd())
# os.mkdir("new_folder")
new_path = os.listdir(r"C:\Users\I.Koval\Desktop")
os.rmdir("new_folder")

for i in (new_path):
    print(i)