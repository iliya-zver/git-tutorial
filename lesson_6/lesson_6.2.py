# def histogram(string):
#     sym_dict = dict()
#     for sym in string:
#         if sym in sym_dict:
#             sym_dict[sym] += 1
#         else:
#             sym_dict[sym] = 1
#     return sym_dict
#
# text = input("Введите текст: ").lower()
# hist = histogram(text)
#
# for i_sym in sorted(hist.keys()):
#     print(i_sym, ":", hist[i_sym])
#
# print("Максимальная частота: ", max(hist.values()))
#
# phonebook = {
#     "Ваня": 100,
#     "Петя": 200,
#     "Алиса": 300
# }
#
# other_phonebook = {
#     "Игорь": 1000,
#     "Петя": 800,
#     "Алена": 2000
# }
#
# phonebook.update(other_phonebook)
# phonebook["Гоша"] = phonebook.pop("Игорь")
# print(phonebook)
# print(phonebook.get("Степан"))


# small_storage = {
#     'гвозди': 5000,
#     'шурупы': 3040,
#     'саморезы': 2000
# }
#
# big_storage = {
#     'доски': 1000,
#     'балки': 150,
#     'рейки': 600
# }
#
# big_storage.update(small_storage)
#
#
# for i in big_storage:
#     print(i.title(), "-", big_storage[i])
#
# name = input("Введите название товара: ")
#
# if name in big_storage:
#     print(big_storage[name])
# else:
#     print(f"Ошибка товара {name.lower()} на складе нет: ",big_storage.get(name))


incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}
# count = 0
# # for i in incomes:
# #     count += incomes[i]
#
# print("Общий доход за год составил",count, "рублей")
print("Общий доход за год составил",sum(incomes.values()), "рублей")

print("Самый маленький доход {0}" )

