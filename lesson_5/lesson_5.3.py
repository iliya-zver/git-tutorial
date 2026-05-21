# text = input("Содержимое файла: ")
# words_list = text.split()
#
# print(words_list)
#
#
# new_text = "---".join(words_list)
# print(new_text)

# while True:
#
#     grats_template = input("Введите шаблон поздравления, "
#                            "в шаблоне нужно использовать конструкцию "
#                            "{name}  и {age}:")
#
#     if "{name}" in grats_template and "{age}" in grats_template:
#         break
#     print("Ошибка: отсутствует одна или две конструкции.")
#
# names_list = input("Список людей через запятую: ").split(", ")
# ages_str = input("Возраст людей через пробел: ")
# ages = [int(i_number) for i_number in ages_str.split()]
#
# for i_man in range(len(names_list)):
#     print(grats_template.format(name=names_list[i_man], age=ages[i_man]))
#
# people = [
#     " ".join([names_list[i_man], str(ages[i_man])])
#     for i_man in range(len(names_list))
# ]
#
# people_str  = ", ".join(people)
# print("\nИменинники: ", people_str)

words = input("Введите три слова: ")
text = input("Введите текст: ")
list_word = words.split(", ")

for word in list_word:
    count = text.count(word)
    print(word, "-", count)


print(list_word)