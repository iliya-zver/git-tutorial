# def factorial(num):
#     if num == 1:
#         return 1
#     fact_m_minus = factorial(num - 1)
#     return num * fact_m_minus
#
#
# num_fact = factorial(5)
# print(num_fact)



# site = {
#
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
# def find_key(struct, key):
#     if key in struct:
#         return struct[key]
#
#     for sub_struct in struct.values():
#         if isinstance(sub_struct, dict):
#             result = find_key(sub_struct, key)
#             if result:
#                 break
#     else:
#         result = None
#     return result
#
#
# user_key = input("Какой ключ ищем?")
# value = find_key(site, user_key)
#
# if value:
#     print(value)
# else:
#     print('Такого ключа в структуре сайта нет.')

# import math
#
#
# def rec_factorial(number):
#     if number <= 1:
#         return 1
#     else:
#         return number * rec_factorial(number - 1)
#
#
# n = 10
# print(rec_factorial(n), math.factorial(n), rec_factorial(n) == math.factorial(n))

def power(a, n):
    if n <= 0:
        return 1
    return a * power(a, n - 1)


float_num = float(input('Введите вещественное число: '))

int_num = int(input('Введите степень числа: '))

print(float_num, '**', int_num, '=', power(float_num, int_num))