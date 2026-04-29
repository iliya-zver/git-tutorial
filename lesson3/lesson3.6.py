# cards = int(input("Количество видеокарт: "))
#
# list_card = []
#
# for i_card in range(1, cards + 1):
#     print("Видеокарта", i_card, ": ", end='')
# #     card = int(input())
# #     list_card.append(card)
# #
# # old_cards = []
# #
# # for i in list_card:
# #     if i != max(list_card):
# #         old_cards.append(i)
# #
# # print(old_cards)

films = ["Крепкий орешек", "Назад в будущее", "Таксист",
    "Леон", "Богемская рапсодия", "Город грехов",
    "Мементо", "Отступники", "Деревня"]

name = int(input("Сколько фильмов хотите добавить? "))

new_films = []

for i in range(name):
    print("Введите название фильма: ", end='')
    film = input()
    if film in films:
        new_films.append(film)
    else:
        print("Ошибка: фильма", film, "у нас нет.")

print("Ваш список любимых фильмов: ", end=' ')
for i in new_films:
    print(i, end=", ")

