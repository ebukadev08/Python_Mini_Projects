name = input("What is your name: ")
print("Welcome", name, "to this adventure")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left and right. which way would like to go?.: ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim to accross: ").lower()

    if answer == "swim":
        print("You swam accross and were eaten by an alligator")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and lost the game")
    else:
        print("Not a valid option, you lose.")

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)?.:  ").lower()

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger, Do you talk to them (yes/no)?: ").lower()

        if answer == "yes":
            print("You talk to a stranger and they give you gold. You WIN!")

        elif answer == "no":
            print("You ignore the stranger and you they got offended and you lose.")

        else:
            print("invalid option. You lose")

    else:
        print("Not a valid option, you lose.")
    print("Thank you for trying", name)
