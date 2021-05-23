# Program Treasure Island - Day 03 of 100

print("\nWelcome to the Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("You\'re at crossroad, where you want to go ? Type 'left' or 'right'\n").lower()
if direction == "right":
    print("\nYou fell into Hole. GAME OVER")
elif direction == "left":
    direction1 = input("\nThere's a river if you want to swim or want to wait for a boat ? Write Swim or Wait\n").lower()
    if direction1 == "swim":
        print("\nYou were eaten by crocodile. GAME OVER")
    elif direction1 == "wait":
        door = input("\nThere are 3 doors out of which one does led to the treasure ? Red, Yellow or blue\n").lower()
        if door == "yellow":
            print("\nCongratulations! You found the Treasure")
            print('''
*******************************************************************************
|                   |                  |                     |
_________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
        |                `"=._o`"=._      _`"=._                     |
________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
        |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
            exit()
        elif door == "red":
            print("\nYou entered into Hell of Flames. GAME OVER")
        elif door == "blue":
            print("\nYou got eaten by sharks. GAME OVER")
print("You couldn't find the Treasure. Try Again....")