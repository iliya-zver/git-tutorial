# import os
# from os import chdir
#
# current_dir = os.getcwd()
# print(f"Сейчас я работаю в папке: {current_dir}")
#
# os.chdir(r"C:\Users\I.Koval\Desktop")
#
# print("Стало: ", os.getcwd())
#
# content = os.listdir(r"C:\Users")
#
# for i, v in enumerate(content):
#     print(i,'-', v)
# os.chdir(r"C:\Users\I.Koval\Desktop")
# print(os.getcwd())
# # os.mkdir("new_folder")
# new_path = os.listdir(r"C:\Users\I.Koval\Desktop")
# # os.rmdir("new_folder")
# os.makedirs("project/data/images", exist_ok=True)
#
#
# for i in (new_path):
#     print(i)

# import os
#
# for root, dirs, files in os.walk("."):
#     print(f"Сейчас проводник в папке: {root}")
#     print(f"Папки внутри: {dirs}")
#     print(f"файл внутри: {files}")
#     print("-" * 20)


import os
from os import chdir
current = os.getcwd()
print(f"Сейчас я работаю в папке: {current}")


os.chdir(r"C:\Users\I.Koval\Desktop")

print("Стало: ",os.getcwd())

content = os.listdir(".")

for i in content:
    print(i)

# os.mkdir("new_folder")
print(os.listdir("."))
os.makedirs("project/dataa/images", exist_ok=True)
print(os.listdir("."))


for root, dirs, files, in os.walk("."):
    print(f"Сейчас проводник в папке: {root}")
    print(f"Папка внутри:  {dirs}")
    print(f"Files in: {files}")
    print("-" * 20)
