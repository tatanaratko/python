check_count = 0
total = 0
item_count = 0
items = []


def add_item(itemName, itemCost):
    global item_count, items, total
    item = itemName + ' - ' + str(itemCost)
    items.append(item)
    item_count += 1
    total += itemCost


def print_receipt():
    global check_count, item_count, total, items
    if items == []:
        pass
    else:
        check_count += 1
        check_count_print = 'Чек ' + str(check_count)
        item_count_print = '. Всего предметов: ' + str(item_count)
        print(check_count_print + item_count_print)
        for item in range(len(items)):
            print(items[item])
        print('Итого: ' + str(total))
        print('-----')
    total = 0
    item_count = 0
    items = []
