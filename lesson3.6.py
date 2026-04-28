cards = int(input("Количество видеокарт: "))

list_card = []

for i_card in range(1, cards + 1):
    print("Видеокарта", i_card, ": ", end='')
    card = int(input())
    list_card.append(card)

old_cards = []

for i in list_card:
    if i != max(list_card):
        old_cards.append(i)

print(old_cards)