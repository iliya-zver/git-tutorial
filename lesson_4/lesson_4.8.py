from itertools import count

# sym = input("Введите текст: ")
#
# vowel = "аеёиоуыэюя"
#
# list_vowel = [i for i in sym if i in vowel]
#
# print('Список гласных букв: ',list_vowel)
# print("Длина списка: ",len(list_vowel))

# number = int(input("Введите длину списка: "))
# num_list = [ 1 if i % 2  == 0  else i % 5 for i in range(number)]
#
# print(num_list)


# import random
#
# list_1 = [round(random.uniform(5, 10), 2)for _ in range(20)]
# list_2 = [round(random.uniform(5, 10), 2)for _ in range(20)]
#
# list_3 = []
#
# for i in range(20):
#     list_3.append(max(list_1[i], list_2[i]))
#
#
# print(list_1)
# print(list_2)
# print(list_3)

# alphabet = 'abcdefg'
#
# print("1:",alphabet[::])
# print("2:",alphabet[::-1])
# print("3:",alphabet[::2])
# print("4:",alphabet[1::2])
# print("5:",alphabet[:1:])
# print("7:",alphabet[3:4:])
# print("8:",alphabet[-3:] )
# print("9:",alphabet[3:5:] )
# print("10:",alphabet[4:2:-1] )


# text = input("Введите строку: ")
#
# first_h = text.index('h')
# last_h = text.rindex('h')
#
# # Извлекаем фрагмент между первым и последним h, разворачиваем его и выводим
# middle_part = text[first_h + 1:last_h]
# reversed_part = middle_part[::-1]
#
# print("Развёрнутая последовательность между первым и последним h:", reversed_part)

# result = [[ j for j in range(i, 13, 4)] for i in range(1, 5)]
# print(result)

# nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
#
# new_list = [o for i in nice_list for l in i for o in l]
#
# print(new_list)





