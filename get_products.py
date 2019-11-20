import re


def get_products(text_file):

    category_names = list(re.findall(r"#.*$", text_file, re.M))
    cleared_category_names = [(item.replace("#", "").strip())
                              for item in category_names]

    items = text_file.split('\n\n\n')

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
