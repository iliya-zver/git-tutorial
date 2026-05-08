# # squares = []
# # for x in range(10):
# #     squares.append(x ** 2)
# squares = [x ** 2 for x in range(10)]
# print(squares)
# def get_higher_price(percent,price):
#     return round(price * (1 + percent / 100) ,2)
#
# price_now = [1.09, 23.56, 57.84, 4.56, 6.78]
# first_percent = int(input("Повышение на первый год: "))
# second_percent = int(input("Повышение на второй год: "))
#
#
# prices_first = [get_higher_price(first_percent,i_price) for i_price in price_now]
# prices_second = [get_higher_price(second_percent,i_price) for i_price in prices_first]
#
#
# print("Сумма цен за каждый год: ", sum(price_now), sum(prices_first), sum(prices_second))


# num_1 = int(input("Левая граница: "))
# num_2 = int(input("Правая граница: "))
#
# lis_1 = [number ** 3 for number in range(num_1, num_2 + 1)]
#
# print(f"Список кубов чисел в диапазоне от {num_1} до {num_2}:", lis_1 )


word = input("Введите строку: ")
sym = input("Введите дополнительный символ: ")

word_sym = [sym * 2 for sym in word]
word_sym_1 = [sym_2 + sym for sym_2 in word_sym]

print(word_sym)
print(word_sym_1)