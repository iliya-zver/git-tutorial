# import random
#
# number_list = [random.randint(1, 4) for _ in range(10)]
#
# # new_list = []
# #
# # for i_num in number_list:
# #     if i_num not in new_list:
# #         new_list.append(i_num)
# #
# # print(number_list)
# # print(new_list)
# unique = set(number_list)
# print(unique)

# text = input("Введите строку: ")
# sym = {".", ",", ":", ";", "!", "?"}
#
# new_sym = set(text)
#
# sym_end = new_sym.intersection(sym)
# count = 0
# print("\nРазличные знаки пунктуации: ",end= '')
# for i_sym in sym_end:
#     count += 1
#     print(i_sym, end='')
# print()
# print("Количество различных знаков пунктуации: ", count)

import random

nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]

nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]
# Напишите программу,
# 1) которая преобразует списки во множества и убирает повторяющиеся элементы.

nums_set_1 = set(nums_1)
nums_set_2 = set(nums_2)
print(nums_set_1, nums_set_2)
# 2) Затем удаляет минимальный элемент из каждого множества

nums_set_1.discard(min(nums_set_1))
nums_set_2.discard(min(nums_set_2))
print(nums_set_1, nums_set_2)

# 3) и добавляет туда случайное число в диапазоне от 100 до 200.
nums_set_1.add(random.randint(100, 200))
nums_set_2.add(random.randint(100, 200))
print(nums_set_1, nums_set_2)

# Затем выполните
# следующие действия со множествами:
#
# 4) Вывести все элементы множеств (объединение).
print(nums_set_1 | nums_set_2)
# 5) Вывести только общие элементы (пересечение).
print(nums_set_1 & nums_set_2)
# 6) Вывести элементы, входящие в nums_2, но не входящие в nums_1.
print(nums_set_2 - nums_set_1)


text = input("Введите строку: ")
text_unique = set(text)
result = text_unique & set("0123456789")
# При помощи множества выделим из строки только общие элементы (цифры) и посчитаем длину множества
print(''.join(result))

# Решение через цикл и сравнение:
new_result = set()
for symbol in text:
    if '0' <= symbol <= '9':
        new_result.add(symbol)

print(''.join(new_result))