# def ask_user(question,
#              complaint = "Неверный ввод. Пожалуйста, введите да или нет",
#              retries = 4):
#     while True:
#         answer = input(question).lower()
#         if answer == "да":
#             return 1
#         if answer == "нет":
#             return 0
#         retries -= 1
#         if retries == 0:
#             print("Количество попыток истекло.")
#             break
#         print(complaint)
#         print("Осталось попыток: ", retries)
#
# ask_user("Вы действительно хотите выйти?")
#
# ask_user("Удалить файл?", "Так удалить или нет")
#
# ask_user("Записать файл?", retries= 2)

# def lst_num(num, lst = None):
#     lst = lst or []
#     if not lst:
#         lst = []
#     lst.append(num)
#     print(lst)
#
#
# lst_num(5)
#
# lst_num(10)
#
# lst_num(15)


def create_dict(data, template=None):
    if isinstance(data, dict):
        return data
    elif isinstance(data, (int,float, str)):
        template = template or dict()
        template[data] = data
        return template
    else:
        return None


def data_preparation(old_list):
    new_list = []
    for i_element in old_list:
        new_list.append(create_dict(i_element))

    return new_list


data = ["sad", {"sds": 23}, {43}, [12, 42, 1], 2323]

data = data_preparation(data)

print(data)