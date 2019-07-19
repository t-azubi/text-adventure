import items, random


class Merchant:
    """A base class for the merchant"""

    def __init__(self):
        self.gold = items.Gold(100)
        self.items = []

    def gen_listofitems(self):
        quantity = random.randint(2, 5)
        list = []
        bool = False
        item = self.get_item()
        list.append(item)
        for x in range(1, quantity):
            item = self.get_item()
            bool = False
            for items in list:
                if items.name == item.name:
                    items.amount += item.amount
                    items.value = items.base * items.amount
                    bool = True
            if bool == False:
                list.append(item)

        return list

    def get_item(self):
        rand = random.randint(0, 8)
        if rand == 1:
            return items.Dagger(1)
        elif rand == 2:
            return items.Sword(1)
        elif rand == 3:
            return items.Bow(1)
        elif rand == 4:
            return items.Axe(1)
        elif rand == 5 :
            return items.Leather_ChestPlate(1)
        elif rand == 6:
            return items.Wooden_Shield(1)
        elif rand == 7:
            return items.Leather_Cap(1)
        else:
            return items.Dagger(1)

