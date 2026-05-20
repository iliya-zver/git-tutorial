def caesar_cipher(string, user_shift):
    char_list = [(alphabet[(alphabet.index(sym) + user_shift) % 33] if sym != " " else " ") for sym in string]
    new_str = " "
    for i_char in char_list:
        new_str += i_char
    return  new_str

alphabet =  "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
new_sim = input('Введите сообщение: ')
shift = int(input("Введите сдвиг:"))


output = caesar_cipher(new_sim, shift)

print("Зашифрованная строка:", output)