"""
Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
"""
goods = []

goodsParams = ["Name", "Price", "Quantity", "Units"]
goodsItem = ()


def fill_and_get_params_map(goods_params):
    tmp_params_map = {}
    for param in goods_params:
        input_param = input("Please enter " + param + " of good ")
        # fill the goods dict by key (["Name", "Price", "Quantity", "Units"])
        # and input value
        tmp_params_map.update({param: input_param})
    return tmp_params_map


continueFlag = True
while continueFlag:
    item = 1
    # form a row of good's list from row number and dictionary
    goodsItem = (item, fill_and_get_params_map(goodsParams))
    goods.append(goodsItem)
    item += item
    isExitFlag = input("For exit please enter 'Q' or enter to continue input ")
    if isExitFlag.upper() == "Q":
        continueFlag = False


print(f"Print List Of Goods: {goods}")

print("Generating of Analytics")

"""
Необходимо собрать аналитику о товарах. Реализовать словарь, 
в котором каждый ключ — характеристика товара, 
например название, а значение — список значений-характеристик, 
например список названий товаров.

{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""


def get_list_of_values_by_key(parm, list_of_goods):
    good_params_list = []
    for item in list_of_goods:
        item_params = item[1]  # 0 - number of item, 1 - is params
        value = item_params.get(parm)
        if value not in good_params_list:
            good_params_list.append(value)
    return good_params_list


analytic_map = {}

# get value form dict in good's list by key (["Name", "Price", "Quantity", "Units"]).
for param in goodsParams:
    analytic_map.update({param: get_list_of_values_by_key(param, goods)})

print(f"Print Analytics: {analytic_map}")
