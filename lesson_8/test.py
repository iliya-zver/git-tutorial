from copy import deepcopy

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на телефон',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}


def replace_text(struct, old_text, new_text):
    for key, value in struct.items():

        if isinstance(value, dict):
            replace_text(value, old_text, new_text)

        elif isinstance(value, str):
            struct[key] = value.replace(old_text, new_text)


sites = []

count = int(input('Сколько сайтов: '))

for _ in range(count):
    product = input(
        'Введите название продукта для нового сайта: '
    )

    new_site = deepcopy(site)

    replace_text(new_site, 'телефон', product)

    sites.append(new_site)

    for index, current_site in enumerate(sites, 1):
        print(f'\nСайт №{index}')
        print(current_site)