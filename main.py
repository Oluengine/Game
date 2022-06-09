import random

while True:
    print('''Welcome to this game! Kindly familiarize yourself 
with the instructions of this game: This game is called
Rock - Paper - Scissors
"R" for "rock",
"P" for "paper",
"S" for "scissors"
Rock breaks Scissors
Paper covers Rock
Scissors cuts Paper
''')

    selection = ['R', 'P', 'S']
    computer_player = random.choice(selection)
    physical_player = "none"
    while physical_player not in selection:
        physical_player = input("Select any of the choices to play ['R', 'P', 'S']: ").upper()
    print("You have selected", physical_player)
    print("Computer has selected", computer_player)
    if physical_player == computer_player:
        print("You have made the same choice with computer. This game is a draw!")
    elif physical_player == "R":
        if computer_player == "S":
            print("Rock breaks the Scissors! You have won this game!")
        else:
            print("Paper covers the Rock! You have lost this game!")
    elif physical_player == "S":
        if computer_player == "P":
            print("Scissors cuts the Paper! You have won this game!")
        else:
            print("Rock breaks the Scissors! You have lost this game!")
    elif physical_player == "P":
        if computer_player == "R":
            print("Paper covers the Rock! You have won this game!")
        else:
            print("Scissors cuts the Paper! You have lost this game!")


    play_again = input("Would you like to play again? Press 'Y' for Yes or 'N' for No: ")
    if play_again.upper() != "Y":
        break
print("Thank you for playing this game! Good bye!")


