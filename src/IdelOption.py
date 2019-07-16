import random
import re

import items


class Option:

    def desciption(player):
        action = str(input(">Do you want to look around, walk out of this room or open you inventory? \n"))
        action = re.sub("\n", "", action)
        action = re.sub("\s", "", action)
        if action.upper() == "LOOK":
            Option.look_around(player)
            Option.desciption2(player)
        elif action.upper() == "WALK":
            Option.walk_around(player)
        elif action.upper() == "INVENTORY":
            player.print_inventory()
            Option.desciption(player)
        else:
            print(">Invalid Input! ")
            Option.desciption(player)

    def desciption2(player):
        action = str(input(">Do you want to walk out of this room or open you inventory? \n"))
        action = re.sub("\n", "", action)
        action = re.sub("\s", "", action)
        if action.upper() == "WALK":
            Option.walk_around(player)
        elif action.upper() == "INVENTORY":
            player.print_inventory()
            Option.desciption(player)
        else:
            print(">Invalid Input! ")
            Option.desciption(player)

    def look_around(player):
        quote = (">You look around,")
        rand = random.randint(1, 100)
        if rand > 70:
            quote += "but it's to dark to see anything"
            print(quote)
        else:
            quote += "it seems, that here could be some items"
            print(quote)
            Option.find_loot(Option, player)

    def walk_around(player):
        print(">You walk out of the Room.")

    def find_loot(self, player):
        rand = random.randint(1, 1000)
        if rand < 10:
            Option.modify_player(Option, player, items.Sword)
            print(">A shiny sword is behind a desk, you take it.")
        elif 10 < rand < 300:
            Option.modify_player(Option, player, items.Gold(5))
            print(">There are 5 golden Coins")
        elif 300 < rand < 500:
            Option.modify_player(Option, player, items.Gold(7))
            print(">A tiny bag of gold Coins")
        elif 500 < rand:
            print(">There is nothing here")

    def add_loot(self, the_player, item):
        bool = False
        for items in the_player.inventory:
            if items.name == item.name:
                items.amount += item.amount
                items.value = items.base * items.amount
                bool = True
        if bool == False:
            the_player.inventory.append(item)

    def modify_player(self, the_player, item):
        self.add_loot(self, the_player, item)
