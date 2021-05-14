print("Welcome to Treasure Island! Your mission is to find the treasure.")
stage_one_choice = input("You're at a cross road. Where do you to go? Type 'left' or 'right': ")
if stage_one_choice == "left":
    stage_two_choice = input("You come to a lake. There is an island across the water. Do you want to wait for a boat "
                             "or swim across? Type 'wait' or 'swim': ")
    if stage_two_choice == "wait":
        stage_three_choice = input("You arrive at the island unharmed. there is a house with 3 doors. One red, "
                                   "one yellow and one blue. Which colour do you choose? Type 'red', 'yellow' or 'blue'")
        if stage_three_choice == "yellow":
            print("You found the treasure!")
        else:
            print("You died!")
    else:
        print("You died!")
else:
    print("You died!")
