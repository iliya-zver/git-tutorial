# user_name = input("Введите пользователя: ")
# file_name = input("Введите имя файла: ")
#
# path = "C:/{user}/docs/folder/{new_file}".format(
#     user = user_name,
#     new_file = file_name
# )
#
# if not path.endswith(".txt") :
#     print("Ошибка: неверное расширение файла")
# elif not path.startswith("C:/"):
#     print("Ошибка: неверно указан диск.")
#
# else:
#     print("Путь к файлу: ", path)

# word_list = []
#
# for i_num in range(3):
#     # print("Введите", i_num + 1, "слово:", end=' ')
#     word = input(f"Введите {i_num + 1} слово: ").lower()
#     word_list.append(word)
#
# text = input("Введите текст: ").lower().split()
#
# print("\nПодсчет слов в тексте")
# for index in range(3):
#     print(word_list[index], ":", text.count(word_list[index]))


# word = input("Введите строку: ")
# wor_1 = word.islower()
# print(wor_1)
#
# if word.islower() > word.isupper():
#     print(word.lower())
# else:
#     print(word.upper())

text = input("Введите текст: ")
lowers = len([letter for letter in text if letter.islower()])
uppers = len([letter for letter in text if letter.isupper()])

if lowers > uppers:
    print("Результат:", text.lower())
else:
    print("Результат:", text.upper())

print(lowers)