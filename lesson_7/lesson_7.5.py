
data = {
    (5000, 123456): ('Иванов', 'Василий'),
    (6000, 111111): ('Иванов', 'Петр'),
    (7000, 222222): ('Медведев', 'Алексей'),
    (8000, 333333): ('Алексеев', 'Георгий'),
    (9000, 444444): ('Георгиева', 'Мария')
}

number = int(input("Введите номер паспорта: "))
series = int(input("Введите серию паспорта: "))

number_and_series = (number, series)

if number_and_series in data:
    print(data[number_and_series])
else:
    print("Такого человека нет")

contacts = {}

while True:
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    name_n_surname = (name, surname)
    if name_n_surname not in contacts:
        contacts[name_n_surname] = int(input("Введите номер телефона: "))
    else:
        print("Такой контакт уже есть!")
    print(contacts)