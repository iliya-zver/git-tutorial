# scores_dict = {
#     "Ваня" : 33,
#     "Петя" : 60,
#     "Лена" : 45
# }
#
#
# for i_name, i_score in scores_dict.items():
#     print(i_name,  i_score )

#
# goods = {
#     "Лампа" : "12345",
#     "Стол" : "23456",
#     "Диван" : "34567",
#     "Стул" : "45678",
# }
#
# store = {
#     "12345" : [
#         {"quantity" : 27, "price" : 42},
#     ],
#     "23456" : [
#         {"quantity" : 22, "price" : 510},
#         {"quantity" : 32, "price" : 520},
#     ],
#     "34567" : [
#         {"quantity" : 2, "price" : 1200},
#         {"quantity" : 1, "price" : 1150},
#     ],
#     "45678": [
#         {"quantity": 50, "price": 100},
#         {"quantity": 12, "price": 95},
#         {"quantity": 43, "price": 97},
#     ],
# }
#
# # for i, c in store.items():
# #     for f in c:
# #         for g, d in f.items():
# #             if g == "price":
# #                 print(g, d)
#
#
# for i_title, i_code in goods.items():
#     total_quantity = 0
#     total_cost = 0
#     for j_good in store[i_code]:
#         total_quantity += j_good["quantity"]
#         total_cost += j_good["price"] * j_good["quantity"]
#     print("{title} - {quantity} шт, стоимость {cost} руб.".format(
#         title = i_title,
#         quantity = total_quantity,
#         cost = total_cost
#     ))

# incomes = {
#     'apple': 5600.20,
#     'orange': 3500.45,
#     'banana': 5000.00,
#     'bergamot': 3700.56,
#     'durian': 5987.23,
#     'peach': 10000.50,
#     'pear': 1020.00,
#     'persimmon': 310.00,
# }
#
#
# for i_income, c_income in incomes.items():
#     print(i_income, "--", c_income)

# server_data = {
#     "server": {
#         "host": "127.0.0.1",
#         "port": "10"
#     },
#     "configuration": {
#         "access": "true",
#         "login": "Ivan",
#         "password": "qwerty"
#     }
#
# }
#
# for i , j in server_data.items():
#     print(i + ":", "\n")
#     for t, f in j.items():
#         print("\t" + t + ':' +f, "\n")

print([i_value for i_key, i_value in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19}.items() if i_key % 2 == 0])

