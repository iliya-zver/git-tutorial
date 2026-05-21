# user_name = input("Введите пользователя: ")
# file_name = input("Введите имя файла: ")
#
# path = "C:/{user}/docs/folder/{new_file}.txt".format(
#     user = user_name,
#     new_file = file_name
# )
#
# path_2 = "C:/{0}/docs/folder/{1}.txt".format(
#     user_name,
#     file_name
# )
#
# path_3 = f"C:/{user_name}/docs/folder/{file_name}.txt"
#
# print("Путь к файлу: ", path)

# while True:
#
#     grats_template = input("Введите шаблон поздравления, "
#                            "в шаблоне нужно использовать конструкцию {name}:")
#
#     if "{name}" in grats_template:
#         break
#     print("Ошибка: отсутствует конструкция {name}.")
#
# print("Введите список имен (заканчивается на end): ")
# names_list = []
# while True:
#     name = input("Имя: ")
#     if name != "end":
#         names_list.append(name)
#     else:
#         break
#
# for i_name in names_list:
#     print(grats_template.format(name = i_name))


# name = input("Введите имя: ")
# num_chek = int(input("Номер заказа: "))
#
# print("Здравствуйте, {name_user}! Ваш номер заказа: {num_new}. "
#       "Приятного дня!".format(name_user = name, num_new = num_chek))

# name = input("Введите имя: ")
# debt = int(input("Введите долг: "))
#
# print("{0}! {0}, привет! Как дела, {0}? Где мои {1} рублей? {0}!".format(name, debt))

# ip_address = "{0}.{1}.{2}.{3}"
# count = 0
# numbers = []
# while count < 4:
#     new_number = int(input("Введите число: "))
#     if 0 <= new_number <= 255:
#         numbers.append(new_number)
#         count += 1
#
# print(ip_address.format(*numbers))
# # * полезный инструмент, но и без него можно справиться, вручную прописав элементы по индексам
# print(ip_address.format(numbers[0], numbers[1], numbers[2], numbers[3]))

