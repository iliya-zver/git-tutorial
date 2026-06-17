# def number(num):
#         if num < 1:
#             return
#         number(num -1)
#         print(num)
#
#
# new_number = int(input("Введите num: "))
#
# number(new_number)
# import copy
#
# site = {
#     'html': {
#         'head': {
#             'title': 'Мой сайт'
#         },
#         'body': {
#             'h2': 'Здесь будет мой заголовок',
#             'div': 'Тут, наверное, какой-то блок',
#             'p': 'А вот здесь новый абзац'
#         }
#     }
# }
#
#
# def new_site(site, key):
#     for i_key, i_value in site.items():
#         if i_key == key:
#             return i_value
#
#         if isinstance(i_value, dict):
#             result = new_site(i_value, key)
#             if result is not None:
#                 return result
#
#     return None
#
#
# key = input("Введите искомый ключ: ")
# result = new_site(site, key)
#
# if result is not None:
#     print("Значение:", result)
# else:
#     print("Ключ не найден")



from copy import deepcopy

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}



def site_copy(list_site,old_name, rename):
    for i_key, i_value in list_site.items():
        if isinstance(i_value, dict):
            site_copy(i_value, old_name, rename)

        elif isinstance(i_value, str):
            list_site[i_key] = i_value.replace(old_name, rename)


count_site = int(input("Сколько сайтов: "))

for i_name in range(count_site):
    new_name = input("Введите название продукта для нового сайта: ")

    new_site = deepcopy(site)

    site_copy(new_site, "телефон", new_name)




