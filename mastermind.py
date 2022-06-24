# Program a game; Mastermind
import sys
import random
import time


# Start game
def game():

    # The computer's code
    com_colors = []

    # The user's answer
    user_guess = []

    # Countdown from 10 to 1
    def countdown():
        count = 10
        print('\tGame starts in: ', end='')
        while count > 0:
            print(count, end='. ')
            count -= 1
            # Countdown timing with each number per second to display
            time.sleep(1)
        print()
        print('=======================================================')

    # User starts the game
    def game_start():

        # Additional computer's code for checking
        check_Code = []

        # How many chances the user has
        chance = 11

        # Current user round
        game_round = 0

        # Check answer: win or lose
        def check_ans(player_chance, player_round):
            if user_guess == com_colors:
                print('\t\tCongratulations, you won!')
                print('\t\tYou took ', player_round, ' guesses to complete.')
                print('=======================================================')
                input('Press ENTER to continue >> ')
                print('=======================================================')
                print('\n\n')

                # Function: go back to the main menu
                game()

            else:
                user_guess.clear()
                guess_input(player_chance, player_round)

        # Input user answer
        def guess_input(x, y):
            user_chance = x
            user_round = y
            # Decrement the chance of user
            # Increment the round of the user
            user_chance -= 1
            user_round += 1

            # Display how many chances the user has left
            print('\t\t--', user_chance, ' GUESSES LEFT --' + '\n')

            # Providing places to each color
            color_num = ['1st', '2nd', '3rd', '4th']
            # While loop: user input four color to guess the code
            i = 0
            while i < 4:
                print('\t\t', color_num[i], ' color: ', end='')
                user_ans = input('')
                if user_ans == 'r' or user_ans == 'R':
                    user_guess.append('red')
                elif user_ans == 'b' or user_ans == 'B':
                    user_guess.append('blue')
                elif user_ans == 'g' or user_ans == 'G':
                    user_guess.append('green')
                elif user_ans == 'y' or user_ans == 'Y':
                    user_guess.append('yellow')
                elif user_ans == 'o' or user_ans == 'O':
                    user_guess.append('orange')
                elif user_ans == 'p' or user_ans == 'P':
                    user_guess.append('pink')
                else:
                    # Incorrect input: minus one to return to previous place
                    print('=======================================================')
                    print('\t\tIncorrect Input')
                    print('=======================================================')
                    i -= 1
                # Post-input: add one to move forward for the next input
                i += 1

            # Display hints for the user
            # Correct color and in the correct place
            v_place = 0

            # Correct color but in the wrong place
            x_place = 0

            # For loop in the range of four elements
            # If user input in color list is TRUE
            # Placed input is same as placed color in list: add one to correct place
            # Else, placed input is not the same: add one to wrong place
            for color in range(0, 4, +1):
                if user_guess[color] in check_Code:
                    if user_guess[color] == com_colors[color]:
                        v_place += 1
                    else:
                        x_place += 1
                    # Remove color if it is checked
                    # This is to not repeat its count or else it will confuse the user
                    check_Code.remove(user_guess[color])

            # Reset the list to re-enter the elements
            check_Code.clear()

            # Re-entering the elements of the colors
            for index in range(4):
                check_Code.append(com_colors[index])

            # Display the hints for the user
            print('\n\tCorrect color in correct place: ', v_place)
            print('\tCorrect color but in the wrong place: ', x_place)
            print('=======================================================')

            # Out of guesses: GAME OVER
            if user_chance == 1:
                print('\t\t-- OUT OF GUESSES --')
                print('\t\tGAME OVER')
                print('\tAns: ', end='')
                for ans in range(4):
                    print(com_colors[ans], '. ', end='')
                print()
                print('=======================================================')
                x = input('Press ENTER to continue >> ')
                while x != '':
                    print('=======================================================')
                    print('\t\tIncorrect Input')
                    print('=======================================================')
                    x = input('Press ENTER to continue >> ')
                print('=======================================================')
                # User return back to the main menu
                print('\n\n')
                game()
            else:
                # Check answers to proceed
                check_ans(user_chance, user_round)

        # Color generator
        for gen in range(4):
            ran_colors = random.choice(['red', 'blue', 'green', 'yellow', 'orange', 'pink'])
            com_colors.append(ran_colors)
            check_Code.append(ran_colors)

        # Function : input user answer
        guess_input(chance, game_round)

    # When user quits the game
    def endgame():

        # Display GAME OVER interface
        print('\t\t   GAME OVER')
        print('=======================================================')
        # Countdown from three to one to shut down the system
        time.sleep(3)
        print('\t\tSHUTTING OFF...')
        # System off
        sys.exit()

    # Menu after instructions is executed
    def menu2(menu_input2):

        # Quit game
        if menu_input2 == '2':

            # Function: user quits the game
            endgame()

        # Start Game
        elif menu_input2 == '':

            # Function: user starts the game
            game_start()

        # Incorrect user input
        else:
            print('\t\tIncorrect Input')
            print('=======================================================')
            input_correction = input('Command >> ')
            print('=======================================================')

            # Function: executing second menu input
            # Repeat second menu sequence when user input is incorrect
            menu2(input_correction)

    # Command in main menu is executed
    def menu(menu_input):

        # Instructions
        if menu_input == '1':
            print('\t\t Instructions' + '\n')
            time.sleep(1)
            print('1. You are given 10 chances to guess four colors.')
            time.sleep(3)
            print('2. There are six colors in this game: ')
            print('R-Red, B-Blue, G-Green, Y-Yellow, O-Orange, P-Pink')
            time.sleep(3)
            print('3. Guess the answer with a letter that represents the')
            print('color.')
            time.sleep(3)
            print('4. Enter your answer in the command.')
            time.sleep(3)
            print('5. Good luck and have fun.')
            time.sleep(1)

            # Second menu
            print('=======================================================')
            print('\t\tPress ENTER to start')
            print('\t\tType 2 to quit the game')
            print('=======================================================')

            # Second start up option
            start2 = input('Command >> ')

            print('=======================================================')

            # Function: Executing second menu input
            menu2(start2)

        # Quit game
        elif menu_input == '2':
            endgame()

        # Start game
        elif menu_input == '':

            # Function: starting up the game
            game_start()

        # Incorrect user input
        else:
            print('\t\t  Incorrect Input')
            print('=======================================================')
            input_correction = input('Command >> ')
            print('=======================================================')
            menu(input_correction)

    # Main Cover
    print('=======================================================')
    print('\t\t\tMASTERMIND')
    print('=======================================================')

    # Main menu
    print('\t\t Press ENTER to start')
    print('\t\tType 1 to show instructions')
    print('\t\tType 2 to quit the game')
    print('=======================================================')

    # First start up option
    start = input('Command >> ')

    print('=======================================================')

    # Function: executing main menu input
    menu(start)


# Start game function
game()
