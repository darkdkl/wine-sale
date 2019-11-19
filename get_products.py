import re


def open_file():
    with open('./action.txt', 'r', encoding='utf-8-sig') as target:
        return target.read()


def get_products():
    text = open_file()

    category_names = list(re.findall(r"#.*$", text, re.M))
    cleared_category_names = [(item.replace("#", "").strip())
                              for item in category_names]

    items = text.split('\n\n\n')

    for name in category_names:
        items.remove(name)

    production = {}

    for index, items_in_category in enumerate(items):
        products = []
        for item in items_in_category.split('\n\n'):

            characteristics = {}

            for characteristic in item.split('\n'):

                splitted_characteristic = characteristic.split(':')
                if len(splitted_characteristic) == 2:
                    key, value = splitted_characteristic

                elif 'Выгодное предложение' in splitted_characteristic:

                    key = 'proposition'
                    value = splitted_characteristic[0]

                characteristics[key] = value
            products.append(characteristics)
        production[cleared_category_names[index]] = products

    return production


if __name__ == "__main__":
    print(get_products())
