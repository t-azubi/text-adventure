import random
import re

import items


class Option:

    def desciption(player):
        action = str(input(">Do you want to look around, walk out of this room, view your stats, heal you  or open you inventory? \n"))
        action = re.sub("\n", "", action)
        action = re.sub("\s", "", action)
        if action.upper() == "LOOK":
            Option.look_around(player)
            Option.desciption2(player)
        elif action.upper() == "WALK":
            Option.walk_around(player)
            return player
        elif action.upper() == "HEAL":
            Option.use_potion(player)
            Option.desciption(player)
        elif action.upper() == "STATS":
            player.print_stats()
            Option.desciption(player)
        elif action.upper() == "INVENTORY":
            player.print_inventory()
            Option.desciption(player)
        else:
            print(">Invalid Input! ")
            Option.desciption(player)

    def desciption2(player):
        action = str(input(">Do you want to walk out of this room, view your stats, heal you  or open you inventory? \n"))
        action = re.sub("\n", "", action)
        action = re.sub("\s", "", action)
        if action.upper() == "WALK":
            Option.walk_around(player)
            return player
        elif action.upper() == "HEAL":
            Option.use_potion(player)
            Option.desciption2(player)
        elif action.upper() == "STATS":
            player.print_stats()
            Option.desciption2(player)
        elif action.upper() == "INVENTORY":
            player.print_inventory()
            Option.desciption2(player)
        else:
            print(">Invalid Input! ")
            Option.desciption2(player)

    def use_potion(player):
        if player.hp == player.hpmax:
            print(">You have maximum Hp! No need to use a potion")
            return player
        else:
            for i in player.inventory:
                if isinstance(i, items.Potion):
                    print("\n Name: {}, Description {}".format(i.name, i.description))
            potion = input(str("> You have {} from {} HP, which potion do you want to use?\n".format(round(player.hp,1), player.hpmax)))
            for i in player.inventory:
                if isinstance(i, items.Potion) and i.name.lower() == potion.name.lower():
                    player.hp += i.heal
                    if player.hp > player.hpmax:
                        player.hp = player.hpmax
        return player


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
        if 1 < rand < 10:
            Option.modify_player(Option, player, items.Sword(1))
            print(">A shiny sword is behind a desk, you take it.")
        elif rand == 1:
            Option.modify_player(Option, player, items.Axe(1))
            print(">You found a Axe hanging from the wall.")
        elif 10 < rand < 100:
            Option.modify_player(Option, player, items.Gold(5))
            print(">There are 5 golden Coins")
        elif 300 < rand < 400:
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
