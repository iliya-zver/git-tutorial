# # squares = []
# # for x in range(10):
# #     squares.append(x ** 2)
# squares = [x ** 2 for x in range(10)]
# print(squares)


price_now = [1.09, 23.56, 57.84, 4.56, 6.78]
first_percent = int(input("Повышение на первый год: "))
second_percent = int(input("Повышение на второй год: "))


prices_first = [get_higher_price(first_percent,i_price) for i_price in price_now]