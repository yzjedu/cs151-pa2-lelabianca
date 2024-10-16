# shut up little boy.

import random

player1_losses = 0
player2_losses = 0
computer_losses = 0
continue_playing = True
print("Welcome to the online 3-player sticks game!\nThe goal is to NOT pick up the very last stick.\nThe computer will go first, then player 1, then player 2.\nThe game will start with 100 sticks on the metaphorical table.\n")
while continue_playing:
    stick_count = 100
    player_turn = 1
    while stick_count != 0:
        while player_turn == 1:
            print("Computer's turn:")
            if stick_count == 4:
                stick_count -= 3
                print("Computer took 3 stick(s).")
                print(f"{stick_count} stick(s) left.\n")
                player_turn = 2
            elif stick_count == 3:
                stick_count -= 2
                print("Computer took 2 stick(s).")
                print(f"{stick_count} stick(s) left.\n")
                player_turn = 2
            elif stick_count == 2:
                stick_count -= 1
                print("Computer took 1 stick(s).")
                print(f"{stick_count} stick(s) left.\n")
                player_turn = 2
            elif stick_count > 4:
                sticks_taken = random.randint(1, 3)
                stick_count -= sticks_taken
                print(f"Computer took {sticks_taken} stick(s).")
                print(f"{stick_count} stick(s) left.\n")
                player_turn = 2
            else:
                stick_count -= 1
                print("Computer took 1 stick(s).")
                print("Computer took the last stick and lost the game.\n")
                computer_losses += 1
                player_turn = 4
        if player_turn == 2:
            print("Player 1 turn:")
        while player_turn == 2:
            sticks_taken = input("How many sticks would player 1 like to take from the table? ")
            if sticks_taken.isdigit():
                sticks_taken = int(sticks_taken)
                if sticks_taken >= 1 and sticks_taken <= 3 and sticks_taken < stick_count:
                    sticks_taken = int(sticks_taken)
                    stick_count -= sticks_taken
                    print(f"Player 1 took {sticks_taken} stick(s).")
                    print(f"{stick_count} stick(s) left.\n")
                    player_turn = 3
                elif sticks_taken >= 1 and sticks_taken <= 3 and sticks_taken == stick_count:
                    sticks_taken = int(sticks_taken)
                    stick_count -= sticks_taken
                    print(f"Player 1 took {sticks_taken} stick(s).")
                    print(f"Player 1 took the last stick and lost the game.\n")
                    player1_losses += 1
                    player_turn = 4
                else:
                    print("This input is invalid. Please try a number between 1 and 3 less than the current stick count.\n")
            else:
                print("This input is invalid. Please try a number between 1 and 3 less than the current stick count.\n")
        if player_turn == 3:
            print("Player 2 turn:")
        while player_turn == 3:
            sticks_taken = input("How many sticks would player 2 like to take from the table? ")
            if sticks_taken.isdigit():
                sticks_taken = int(sticks_taken)
                if sticks_taken >= 1 and sticks_taken <= 3 and sticks_taken < stick_count:
                    sticks_taken = int(sticks_taken)
                    stick_count -= sticks_taken
                    print(f"Player 2 took {sticks_taken} stick(s).")
                    print(f"{stick_count} stick(s) left.\n")
                    player_turn = 1
                elif sticks_taken >= 1 and sticks_taken <= 3 and sticks_taken == stick_count:
                    sticks_taken = int(sticks_taken)
                    stick_count -= sticks_taken
                    print(f"Player 2 took {sticks_taken} stick(s).")
                    print(f"Player 2 took the last stick and lost the game\n")
                    player2_losses += 1
                    player_turn = 4
                else:
                    print(
                        "This input is invalid. Please try a number between 1 and 3 less than the current stick count.\n")
            else:
                print("This input is invalid. Please try a number between 1 and 3 less than the current stick count.\n")
        while player_turn == 4:
            continue_query = input('Would you like to play again? Please type your answer as yes or no: ')
            if continue_query.lower() == 'yes':
                print("New game starting now!\n")
                break
            elif continue_query.lower() == 'no':
                print(f"Computer lost {computer_losses} times.\nPlayer 1 lost {player1_losses} times.\nPlayer 2 lost {player2_losses} times.\nThank you for playing!")
                continue_playing = False
                break
            else:
                print("Invalid input. Please type your answer as 'yes' or 'no'.\n.")