from gameComponents import gameVars


def winorlose(status):
    if status == "won":
        pre_message = "You win! "
    else:
        pre_message = "You lose! "

    print(pre_message + 'Play again?)')

    choice = False

    while choice == False:
        choice = input("Y / N? ")

        if choice == "Y" or choice == "y":
            gameVars.player_lives = gameVars.total_lives
            gameVars.computer_lives = gameVars.total_lives
            gameVars.player_choice = False
        elif choice == "N" or choice == "n":
            print("You chose to quit.")
            exit()
        else:
            print("Make a valid choice - Y or N")
            choice = False