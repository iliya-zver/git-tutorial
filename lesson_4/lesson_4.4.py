# squares = []
# for x in range(10):
#     if x % 2 != 0:
#         squares.append(x ** 2)
#
import random

# squares_odds = [x ** 2 for x in range(10) if x % 2 != 0]
# squares_cub = [(x ** 2 if x % 2 != 0 else x ** 3) for x in range(10) ]
#
# print(squares_odds)
# print(squares_cub)

# import random
#
# squad_1 = [random.randint(50, 80) for _ in range(10)]
# squad_2 = [random.randint(30, 60) for _ in range(10)]
# squad_3 = [("Погиб" if squad_1[i_damage] + squad_2[i_damage] > 100
#             else "Выжил")
#            for i_damage in range(10)]
#
# print("Урон первого отряда: ", squad_1)
# print("Урон второго отряда: ", squad_2)
# print("Состояние третьего отряда: ", squad_3)

# a = int(input())
# b = int(input())
#
# num = [random.randint(a, b) for _ in range(4)]

# print(num)

original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]

num_1  =  [x if x > 0 else 0  for x in original_prices]

print(num_1)