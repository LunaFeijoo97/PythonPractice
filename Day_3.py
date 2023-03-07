print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice_1 = input('You are at a cross road.\nWhere do you want to go? Type "Left" or "Right" to choose.\n').lower()

if choice_1 == "left":
  choice_2 = input('You\'ve come to a lake. There is an island in the middle of the lake.\nType "Wait" to wait for a boat or type "Swim" to swim across it\n').lower()

  if choice_2 == "wait":
    choice_3 = input('You\'ve arrived at the island unharmed after sailing the boat!\nThere is a house with 3 doors. One is red, one is yellow and the other one is blue.\nWhich door do you go through?\n').lower()
    
    if choice_3 == "yellow":
      print("You've found the treasure! You won the game!\nCongratulations!")
    elif choice_3 == "red":
      print("Oh no, the room sets on fire as soon as you step in!\nGame over!")
    elif choice_3 == "blue":
      print("Everything seems fine, until some beasts star eating you!\nGame Over")
    else:
      print("That's not a valid door buddy.\nGame Over!")
      
  else:
    print("Oh no! You've got attacked by an angry trout!\nGame Over!")
    
else:
  print("You've fallen into a hole, oops!\nGame Over!")