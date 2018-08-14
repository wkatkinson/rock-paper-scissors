import random

rps = ["rock", "paper", "scissors"]

comp_choice = rps[random.randint(0, 2)]

name = input("What is your name?\n")

play_game = True

comp_score = "0"

player_score = "0"

while play_game == True:
    print("Hi %s. Ready to play some 'rock, paper,scissors'? \n" % name)
    player_choice = input("\nType 1 for Rock, 2 for Paper, and 3 for Scissors.")

    player_choice = rps[int(player_choice) - 1]

    print("\nComputer throws %s. \n" % comp_choice)
    print("%s throws %s \n" % (name, player_choice))

    if comp_choice == "rock":
        if player_choice == "rock":
            print("It's a Tie. Throw again.")
        elif player_choice == "scissors":
            print("Computer wins.")
            comp_score = int(comp_score) + 1
            print("Computer: %i | %s: %i" % (int(comp_score), name, int(player_score)))
        else:
            print("%s wins." % name)
            player_score = int(player_score) + 1
            print("Computer: %i | %s: %i" % (int(comp_score), name, int(player_score)))

    if comp_choice == "paper":
        if player_choice == "paper":
            print("It's a tie. Throw again.")
        elif player_choice == "rock":
            print("Computer wins.")
            comp_score = int(comp_score) + 1
            print("Computer: %i | %s: %i" % (int(comp_score), name, int(player_score)))
        else:
            print("%s wins." % name)
            player_score = int(player_score) + 1
            print("Computer: %i | %s: %i" % (int(comp_score), name, int(player_score)))

    if comp_choice == "scissors":
        if player_choice == "scissors":
            print("It's a Tie. Throw again.")
        elif player_choice == "paper":
            print("Computer wins.")
            comp_score = int(comp_score) + 1
            print("Computer: %i | %s: %i" % (int(comp_score), name, int(player_score)))
        else:
            print("%s wins." % name)
            player_score = int(player_score) + 1
            print("Computer: %i | %s: %i" % (int(comp_score), name, int(player_score)))

    again = input("Would you like to play again? (Y/N)")

    if again == "Y":
        play_game = True
    else:
        comp_score = "0"
        player_score = "0"
        play_game = False

    while play_game == False:

        restart = input("Press 1 to play again...")

        if restart == "1":
            name_reset = input("Are you a new player? (Y/N)")

            if name_reset == "Y":
                name = input("What is your name?")
                play_game = True

            elif name_reset == "N":
                print("Hi again %s!" % name)
                play_game = True

        else:
            print("You must type 'Start Over' to play again.")
            restart
