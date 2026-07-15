# import os
#
# folder_name = "project"
# file_name = "my_file.txt"
#
# path = "docs/{folder}/{file}".format(
#     folder=folder_name,
#     file=file_name
# )
#
# print(path)
#
# rel_path = os.path.join("doc", folder_name, file_name)
#
# print(rel_path)
#
# abs_path = os.path.abspath(file_name)
#
# print(abs_path)
# import os.path
#
# def print_dirs(project):
#     print("\nСодержимое директории", project)
#     for i_elem in os.listdir(project):
#         path = os.path.join(project,i_elem)
#         print("   ", path)
#
#
# projects_list = ["git-tutorial"]
#
# for i_project in projects_list:
#     path_to_project = os.path.abspath(os.path.join("..","..", i_project))
#     print_dirs(path_to_project)

import os

path = os.path.join("Skillbox", "access", "admin.bat")
abs_path = os.path.abspath(path)

print("Абсолютный путь: ", abs_path, "\n")
print("Относительный путь: ", path)

for path in os.listdir(".."):
    print(os.path.join(os.path.abspath(".."), path))

q = os.listdir("..")
print(q)

print("Корень диска: ", os.path.abspath(os.sep).split(os.sep)[0])
