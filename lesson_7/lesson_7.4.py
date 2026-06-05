# scores_dict = {
#     "Ваня" : 33,
#     "Петя" : 60,
#     "Лена" : 45
# }
#
#
# for i_name, i_score in scores_dict.items():
#     print(i_name,  i_score )


goods = {
    "Лампа" : "12345",
    "Стол" : "23456",
    "Диван" : "34567",
    "Стул" : "45678",
}

store = {
    "12345" : [
        {"quantity" : 27, "price" : 42},
    ],
    "23456" : [
        {"quantity" : 22, "price" : 510},
        {"quantity" : 32, "price" : 520},
    ],
    "34567" : [
        {"quantity" : 2, "price" : 1200},
        {"quantity" : 1, "price" : 1150},
    ],
    "45678": [
        {"quantity": 50, "price": 100},
        {"quantity": 12, "price": 95},
        {"quantity": 43, "price": 97},
    ],
}

# for i, c in store.items():
#     for f in c:
#         for g, d in f.items():
#             if g == "price":
#                 print(g, d)


for i_title, i_code in goods.items():
    total_quantity = 0
    total_cost = 0
    for j_good in store[i_code]:

