import re


def prepared_products_data():
    with open('./action.txt', 'r', encoding='utf-8-sig') as target:
        all_data = target.read()

    category_names = list(re.findall(r"#.*$", all_data, re.M))
    category_names_clear = [(i.replace("#", "").strip())
                            for i in category_names]

    items_data = all_data.split('\n\n\n')

    for name in category_names:
        items_data.remove(name)

    products_data = {}

    for index, items_in_category in enumerate(items_data):
        products = []
        for characteristics in items_in_category.split('\n\n'):
            characteristics_data = {}

            for characteristic in characteristics.split('\n'):

                splited_characteristic = characteristic.split(':')
                if len(splited_characteristic) == 2:
                    k, v = splited_characteristic
                else:
                    splited_characteristic.append('proposition')
                    v, k = splited_characteristic
                characteristics_data[k] = v
            products.append(characteristics_data)
        products_data[category_names_clear[index]] = products

    return products_data


if __name__ == "__main__":
    print(prepared_products_data())
