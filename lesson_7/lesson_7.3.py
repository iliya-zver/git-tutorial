# scores = [54, 67, 99, 27]
# for i_player, i_score in enumerate(scores):
#     scores[i_player] += 10
#     print(i_player, i_score)
#
# print(scores)

# new_string = input("Строка: ")
#
# for index, i_score  in enumerate(new_string):
#     if i_score == "~":
#         print(index, end=' ')


# def get_indexes(where_to_search, what_to_search):
#     return [str(index) for index, letter in enumerate(where_to_search) if letter == what_to_search]
#
#
# text = input("Введите текст: ")
# print("Ответ:", " ".join(get_indexes(text, "~")))

import random

def get_random_letter(n):
    return random.choices([chr(i) for i in range(ord("а"), ord("я"))], k=n)


first_letters = get_random_letter(10)
second_letters = get_random_letter(10)
print(first_letters)
print(second_letters)

first_dictionary = dict(enumerate(first_letters))
second_dictionary = dict(enumerate(second_letters))
print(first_dictionary)
print(second_dictionary)


def return_even_elements(data):
    result = []
    if isinstance(data, dict):
        data = data.values()
    for index, value in enumerate(data):
        if index % 2 == 0:
            result.append(value)
    return result


print(return_even_elements('О Дивный Новый мир!'))
print(return_even_elements([100, 200, 300, 'буква', 0, 2, 'а']))
print(return_even_elements({0: 'е', 1: 'о', 2: 'ч', 3: 'ы', 4: 'в', 5: 'н', 6: 'д', 7: 'а', 8: 'ш', 9: 'ц'}))