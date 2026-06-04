# def add_num(seq, number):
#     seq = list(seq)
#     for i_num in range(len(seq)):
#         seq[i_num] += number
#     return seq
#
# origin_tuple = (3, 1, 4, 1, 5)
# change_list = add_num(origin_tuple, 5)
#
# print(origin_tuple)
# print(change_list)

# import random
#
# new_list = [random.randint(0, 5) for i in range(10)]
# new_list_2 = [random.randint(-5, 0) for i in range(10)]
#
#
# new_tuple = tuple(new_list)
# new_tuple_2 = tuple(new_list_2)
# new_tuple_3 = new_tuple + new_tuple_2
# nul = new_tuple_3.count(0)
#
# print(new_tuple_3)
# print(nul)
# import math
#
# def side(radios, h):
#     si = 2 * math.pi * radios * h
#     s = math.pi * radios ** 2
#     full = si + 2 * s
#     return round(si, 2),round(full, 2)
#
# h = float(input())
# r = float(input())
#
# new = side(h,r)
#
# print(new)

# import random
#
# def change(nums):
#     index = random.randint(0, 5)
#     value = random.randint(100, 1000)
#     nums[index] = value
#     return nums, value
#
# my_nums = 1, 2, 3, 4, 5
#
# new_nums, rand_val = change(my_nums)
# print(new_nums, rand_val)
# new_nums = change(new_nums)
# rand_val += change(new_nums)
# print(new_nums, rand_val)

import random


def change(nums):
    index = random.randint(0, 5) % len(nums)
    value = random.randint(100, 1000)
    nums = list(nums)
    nums[index] = value
    return tuple(nums), value


my_nums = 1, 2, 3, 4, 5

new_nums, rand_val = change(my_nums)
print(new_nums, rand_val)
new_nums_2, rand_val_2 = change(new_nums)
rand_val += rand_val_2
print(new_nums_2, rand_val)