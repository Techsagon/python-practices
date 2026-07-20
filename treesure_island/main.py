print('''
                                              ______________________________________________________________________________
                                                       |                   |                  |                     |
                                              _________|________________.=""_;=.______________|_____________________|_______
                                                                 |  ,-"_,=""     `"=.|                  |
                                              ___________________|__"=._o`"-._        `"=.______________|___________________
                                                       |                `"=._o`"=._      _`"=._                     |
                                              _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
                                                                 |    __.--" , ; `"=._o." ,-"""-._ ".   |
                                              ___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                                                       |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
                                              _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
                                                                 | |o;    `"-.o`"=._``  '` " ,__.--o;   |
                                              ___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
                                              ___/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
                                              ______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
                                              ___/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
                                              ______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
                                              ___/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
                                              ______/______/______/______/______/______/______/______/______/______/______/_
                                              
 __    __    ___  _        __   ___   ___ ___    ___      ______   ___       ______  ____     ___   ____  _____ __ __  ____     ___      ____ _____ _       ____  ____   ___   
|  |__|  |  /  _]| |      /  ] /   \ |   |   |  /  _]    |      | /   \     |      ||    \   /  _] /    |/ ___/|  |  ||    \   /  _]    |    / ___/| |     /    ||    \ |   \  
|  |  |  | /  [_ | |     /  / |     || _   _ | /  [_     |      ||     |    |      ||  D  ) /  [_ |  o  (   \_ |  |  ||  D  ) /  [_      |  (   \_ | |    |  o  ||  _  ||    \ 
|  |  |  ||    _]| |___ /  /  |  O  ||  \_/  ||    _]    |_|  |_||  O  |    |_|  |_||    / |    _]|     |\__  ||  |  ||    / |    _]     |  |\__  || |___ |     ||  |  ||  D  |
|  `  '  ||   [_ |     /   \_ |     ||   |   ||   [_       |  |  |     |      |  |  |    \ |   [_ |  _  |/  \ ||  :  ||    \ |   [_      |  |/  \ ||     ||  _  ||  |  ||     |
 \      / |     ||     \     ||     ||   |   ||     |      |  |  |     |      |  |  |  .  \|     ||  |  |\    ||     ||  .  \|     |     |  |\    ||     ||  |  ||  |  ||     |
  \_/\_/  |_____||_____|\____| \___/ |___|___||_____|      |__|   \___/       |__|  |__|\_||_____||__|__| \___| \__,_||__|\_||_____|    |____|\___||_____||__|__||__|__||_____|
                                                                                                                                                                               ''')
print("You are at the great city of booze! Its winter and the roads are frozen. do you wait till summer or hit the road right away?\n")
opt_1 = str(input("Type \"Wait\" or type \"Road\" to continue: "))
if opt_1 == "Wait" or opt_1 == "wait":
    print("\nYou stay at the city, meeting the woman of your dreams and live to see your grandkids! you forget about the treasure altogether...")
    print('''
  ____   ____  ___ ___    ___       ___   __ __    ___  ____   __ 
 /    | /    ||   |   |  /  _]     /   \ |  |  |  /  _]|    \ |  |
|   __||  o  || _   _ | /  [_     |     ||  |  | /  [_ |  D  )|  |
|  |  ||     ||  \_/  ||    _]    |  O  ||  |  ||    _]|    / |__|
|  |_ ||  _  ||   |   ||   [_     |     ||  :  ||   [_ |    \  __ 
|     ||  |  ||   |   ||     |    |     | \   / |     ||  .  \|  |
|___,_||__|__||___|___||_____|     \___/   \_/  |_____||__|\_||__|''')

elif opt_1 == "Road" or opt_1 == "road":
    print("\nYou gather your courage and start your journey, the winter was harsh but the blazing fire in your heart kept you warm!")
    print("eventually you manage to get across the country to the southern cities and reach the docks, but you don't have enough money to get on a ship!")
    print("do you sneak into one of the ships at night or ask one of the captains to take you to your destination in return for you working for them?\n")
    opt_2 = str(input("Type \"Steal\" or type \"Ask\" to continue: "))

    if opt_2 == "Steal" or opt_2 == "steal":
        print("\n You try to steal the money from a man in the street but he sees you and stabs you in the heart!")
        print('''
          ____   ____  ___ ___    ___       ___   __ __    ___  ____   __ 
         /    | /    ||   |   |  /  _]     /   \ |  |  |  /  _]|    \ |  |
        |   __||  o  || _   _ | /  [_     |     ||  |  | /  [_ |  D  )|  |
        |  |  ||     ||  \_/  ||    _]    |  O  ||  |  ||    _]|    / |__|
        |  |_ ||  _  ||   |   ||   [_     |     ||  :  ||   [_ |    \  __ 
        |     ||  |  ||   |   ||     |    |     | \   / |     ||  .  \|  |
        |___,_||__|__||___|___||_____|     \___/   \_/  |_____||__|\_||__|''')

    elif opt_2 == "Ask" or opt_2 == "ask":
        print("\nThe captain agrees to let you on the ship in exchange for you doing chores.")
        print("after 3 weeks of sailing the endless seas you finally arrive at your destination, after thanking the captain you jump in the water and swim to the island.")
        print("as you are approaching the island you notice 2 pirates carrying a chest to their boat. is that your treasure?? do you try to take it from them?\n")
        opt_3 = str(input("Type \"Yes\" or \"No\" to continue: "))
        if opt_3 == "Yes" or opt_3 == "yes":
            print("\nAfter a gruesome fight you manage to kill them both and take the chest! Hooray!!")
            print("after opening the chest you take the treasure out and look at it...")
            print('''
            ________________________________________________
            ||||||||||||||||||||||||||||||||||||||||||||||||
            |. . . . . . . .|||. . . . . ||| . . . . . . . |
            | . . . . . . . ||| . . . . .|||. . . . . . . .|
            |._._._. . . . .|||. . . . . ||| . .. . . ._._.|
            |/     \. . . . /// . . . . . \\\ . . . ./    \|
            |       |. . . /// . . . . . . \\\ . . .|      |
            |        \. . /// . . . . . . . \\\ . ./       |
             \        |. /// . . . . . . . . \\\ .|        /
              |        \/// . . . . . . . . . \\\/        |
               \        \/ . . . . . . . . . . \/        /
                |        |. . . . . . . . . . .|        |
                 \        \. . . . . . . . . ./        /
                  |        \. . . . . . . . ./        |
                   \        \. . . . . . . ./        /
                    \        |- - - - - - -|        /
                     `-.____/_______________\____.-' ''')
        elif opt_3 == "No" or opt_3 == "no":
            print("\nThe treasure is lost just like your hopes and dreams, you lay on the beach listening to the sound of waves hitting the shore")
            print("\"You Died 3 Days Later From Dehydration\"")
            print('''
                      ____   ____  ___ ___    ___       ___   __ __    ___  ____   __ 
                     /    | /    ||   |   |  /  _]     /   \ |  |  |  /  _]|    \ |  |
                    |   __||  o  || _   _ | /  [_     |     ||  |  | /  [_ |  D  )|  |
                    |  |  ||     ||  \_/  ||    _]    |  O  ||  |  ||    _]|    / |__|
                    |  |_ ||  _  ||   |   ||   [_     |     ||  :  ||   [_ |    \  __ 
                    |     ||  |  ||   |   ||     |    |     | \   / |     ||  .  \|  |
                    |___,_||__|__||___|___||_____|     \___/   \_/  |_____||__|\_||__|''')
        else:
            print("Your answer was invalid! Start again.")
    else:
        print("Your answer was invalid! Start again.")
else:
    print("Your answer was invalid! Start again.")
