cards = int(input("Количество видеокарт: "))

list_card = []

for i_card in range(1, cards + 1):
    print("Видеокарта", i_card, ": ")
    card = int(input())
    list_card.append(card)

print(list_card)