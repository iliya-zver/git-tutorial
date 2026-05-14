# nums = [x for x in range(1, 101) if x % 10 == 0]
# new_nums = nums[:]
# new_nums[3] = 0
#
# print(new_nums[2:8])
#
# import random
#
# original_prices = [random.randint(-100, 100) for i in range(10)]
#
# print(original_prices)
#
# new_prices = original_prices[::]
#
#
# for i in range(len(original_prices)):
#
#     if new_prices[i] < 0:
#
#         new_prices[i] = 0
#
# print("Мы потеряли: ",  abs(sum(original_prices) - sum(new_prices)))

# nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]
#
# new_nums = nums[:5]
# new_nums_1 = nums[:-2]
# new_nums_2 = nums[::2]
# new_nums_3 = nums[1::2]
# new_nums_4 = nums[::-1]
# new_nums_5 = nums[::-2]
#
#
# print(new_nums)
# print(new_nums_1)
# print(new_nums_2)
# print(new_nums_3)
# print(new_nums_4)
# print(new_nums_5)

import random
number = [random.randint(a = 1, b = 100) for i in range(10)]
a = int()
b = int()
new_number = number[a:]


print(number)

n = int(input("Введите количество чисел N: "))

numbers = [random.randint(-10, 10) for _ in range(n)]

a = random.randint(0, len(numbers) - 2)
b = random.randint(a + 1, len(numbers) - 1)
# Генерируем числа так, чтобы они не выходили за границу списка
print(numbers, a, b)
numbers = numbers[:a] + numbers[b + 1:]
print(numbers)



