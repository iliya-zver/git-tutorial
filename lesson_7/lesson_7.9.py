# students = {
#     1: {
#         'name': 'Bob',
#         'surname': 'Vazovski',
#         'age': 23,
#         'interests': ['biology, swimming']
#     },
#     2: {
#         'name': 'Rob',
#         'surname': 'Stepanov',
#         'age': 24,
#         'interests': ['math', 'computer games', 'running']
#     },
#     3: {
#         'name': 'Alexander',
#         'surname': 'Krug',
#         'age': 22,
#         'interests': ['languages', 'health food']
#     }
# }
#
# def f(dict):
#     lst = []
#     string = ''
#     for i in dict:
#         lst += (dict[i]['interests'])
#         string += dict[i]['surname']
#     cnt = 0
#     for s in string:
#         cnt += 1
#     return lst, cnt
#
# pairs = []
# for i in students:
#     pairs += (i, students[i]['age'])

# my_lst = f(students)[0]
# l = f(students)[1]
# print(my_lst, l)



def crypto(intern):
    for i_key, i_val in enumerate(intern):
        print(i_key)


print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))