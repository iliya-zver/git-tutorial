# phonebook_list = [
#     ["Ваня", 88006663636],
#     ["Петя", 88005553535],
#     ["Лена", 88007773737]
# ]

# name = input("Введите имя: ")
#
# is_exist = False
# for i_person in phonebook_list:
#     if i_person[0] == name:
#         is_exist = True
#         print(i_person[1])
#         break
#
# if not is_exist:
#     print("Ошибка: человек с именем {0} не найден".format(name))

# phonebook_dict = {
#     "Ваня": 88006663636,
#     "Петя": 88005553535,
#     "Лена": 88007773737
# }
#
# name = input("Введите имя: ")
# if name in phonebook_dict:
#     print(phonebook_dict[name])
# else:
#     print("Ошибка: человек с таким именем {0} не найден".format(name))


# student_str = input("Введите информацию о студенте через пробел\n"
#                     "(имя, фамилия, город, место учебы, оценки):"
# )
#
# student_info = student_str.split()
#
# student = dict()
# student["Имя"] = student_info[0]
# student["Фамилия"] = student_info[1]
# student["Город"] = student_info[2]
# student["Место учебы"] = student_info[3]
# student["Оценки"] = []
# for i_grade in student_info[4:]:
#     student["Оценки"].append(int(i_grade))
#
#
# for i_info in student:
#     print(i_info, "-", student[i_info])

num = int(input("Введите число: "))

num_dic = dict()

for i_num in range(1, num + 1):
    num_dic[i_num] = i_num ** 2

print(num_dic)