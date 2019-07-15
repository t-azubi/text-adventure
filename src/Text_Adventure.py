# name: Richard
# date: 08-07-2019
# description: text-based adventure game
import sys

import IdelOption
import Room
from Classes import Quotes, GenPaths
from Player import Character


############### Changes to be made ###############
#
# input auf (done)
#
#
#
#
#
#
#
#
##################################################


def displayIntro():
    print("#############################################")
    print("##                                         ##")
    print("##                WELCOME                  ##")
    print("##          TO THE ADVENTURES OF           ##")
    print("##          GERWALD OF WALDSTETT           ##")
    print("##                                         ##")
    print("##          Type: START to start           ##")
    print("##       Type: HELP to receive help        ##")
    print("##       Type: QUIT to quit the game       ##")
    print("##  Type: LANGUAGE to change the language  ##")
    print("##                                         ##")
    print("#############################################")


def IntroQuestion(intro):
    if intro.upper() == "START":
        print("\n> Alright, so let us start the adventure of Gerwald of Waldstett!")
        # time.sleep(1.5)
        Story(intro)
    elif intro.upper() == "HELP":
        print("\nINSTRUCTIONS, just follow along the questions and just input the things you are allowed to!!!")
        # time.sleep(1.5)
        Help(intro)
    elif intro.upper() == "QUIT":
        print("\n#######################################")
        print("##                                   ##")
        print("##  Thank you for playing the game.  ##")
        print("##                                   ##")
        print("#######################################")
        sys.exit()
    else:
        intro = str(input("\nPlease enter one of the commands above: "))
        IntroQuestion(intro)


def Story(intro):
    if intro.upper() == "START":
        # time.sleep(1.5)
        print("\n> I hope you brought enough time and i hope you have fun playing.")
    else:
        intro = str(input("\n" + Quotes.invalid_input()))
        IntroQuestion(intro)


def Help(intro):
    if intro.upper() == "HELP":
        intro = input("\nIf you are ready to start the game, enter the START command! ")
        IntroQuestion(intro)
    else:
        intro = str(input("\n" + Quotes.invalid_input()))
        IntroQuestion(intro)


displayIntro()
intro = str(input("\n> Please state what you want to do! \n"))
IntroQuestion(intro)

# time.sleep(1.5)
print(
    "\n> And so the tale begins. Years ago in the land of Ghrezok, there lived a man named Gerwald in a city called Waldstett.")
# time.sleep(1.5)


player = Character()
Room.StartingRoom.intro_text(self=Room.Gen_Current_Room.gen())
print("> You look around an find some items")
Character.print_inventory(player)
option = IdelOption.Option
GenPaths.path_gen()
room = Room.Gen_Current_Room.gen()
print(room.intro_text(room))
if room == Room.EnemyRoom:
    room.modify_player(room, player)
while player.is_alive() and not player.victory:
    option.desciption(player)
    GenPaths.path_gen()
    room = Room.Gen_Current_Room.gen()
    print(room.intro_text(room))
    if room == Room.EnemyRoom:
        room.modify_player(room, player)
