# data = dict()
# print(data.get("server"))
# data["server"] = {
#     "host": "127.0.0.1",
#     "port": "10"
# }
#
# if data.get("configuration", {}).get("ssh", {}).get("login", {}):
#     print("В структуре уже есть логин")
# print(data.get("configuration", {}).get("ssh", {}).get("login", {}))
#
# data["configuration"] = {
#     "ssh": {
#         "access": "true",
#         "login": "Ivan",
#         "password": "qwerty"
#     }
# }
#
#
# print(data)

# print(data["server"]["port"])
# data["configuration"]["ssh"]["login"] = "Vova"
# print(data["configuration"]["ssh"]["login"])
# print()
# for i in data.values():
#     for j_key in i:
#         print(j_key, i[j_key])


# players_dict = {
#     1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
#     2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
#     3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
#     4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
#     5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
#     6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
#     7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
#     8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
# }
#
# team_a_members = [
#     player["name"]
#     for player in  players_dict.values()
#     if player["team"] == "A" and player["status"] == "Rest"
# ]
#
# print(team_a_members)


order = {
    'apple': 2,
    'banana': 3,
    'pear': 1,
    'watermelon': 10,
    'chocolate': 5
}


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

result_sum = 0

for fruit_name in order:
    cost = incomes.get(fruit_name, 0) * order[fruit_name]
    print(cost)
    result_sum += cost

print("Итоговая стоимость из заказа составляет: ", result_sum)



