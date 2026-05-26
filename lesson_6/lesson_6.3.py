data = dict()
print(data.get("server"))
data["server"] = {
    "host": "127.0.0.1",
    "port": "10"
}
data["configuration"] = {
    "ssh": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}

print(data)

# print(data["server"]["port"])
# data["configuration"]["ssh"]["login"] = "Vova"
# print(data["configuration"]["ssh"]["login"])
# print()
# for i in data.values():
#     for j_key in i:
#         print(j_key, i[j_key])