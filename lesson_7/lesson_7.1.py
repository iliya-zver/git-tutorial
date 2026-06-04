def is_poly(string):
    char_dic = {}
    for i_sym in string:
        char_dic[i_sym] = char_dic.get(i_sym, 0) + 1

    odd_count = 0
    for i_value in char_dic.values():
        if i_value % 2 != 0:
            odd_count += 1

    return odd_count <= 1


my_string = input("Введите строку: ")
if is_poly(my_string):
    print("Можно сделать палиндром")
else:
    print("Нельзя сделать палиндром")