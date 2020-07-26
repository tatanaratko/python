def choose_coffee(*beverages):
    global ingredients
    resurce = {'Эспрессо': (1, 0, 0),
               'Капучино': (1, 3, 0),
               'Маккиато': (2, 1, 0),
               'Кофе по-венски': (1, 0, 2),
               'Латте Маккиато': (1, 2, 1),
               'Кон Панна': (1, 0, 1)}
    for beverage in beverages:
        coffe_price, milk_price, cream_price = resurce[beverage]
        coffe, milk, cream = ingredients

        isEnoughCoffee = (coffe - coffe_price) >= 0
        isEnoughMilk = (milk - milk_price) >= 0
        isEnoughCream = (cream - cream_price) >= 0

        if isEnoughCoffee and isEnoughCream and isEnoughMilk:
            ingredients = [coffe - coffe_price,
                           milk - milk_price, cream - cream_price]
            return beverage
    return "К сожалению, не можем предложить Вам напиток"
