


class Merchant:
    """A base class for the merchant"""

    def __init__(self, name, gold, items):

        self.name = name
        self.gold = gold
        self.items = items

    def has_gold(self):
        return self.gold > 0


merchant_items = ["sword", "axe", "hammer"]




##player selling items

merchant_items = ["sword", "axe", "hammer"]
print(merchant_items)
merchant_items.append(input("Which items do you want to sell? "))


##player buying items
print(merchant_items)
merchant_items.remove(input("Which items do you want to buy? "))
