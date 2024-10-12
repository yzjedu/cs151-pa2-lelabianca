# Initial Design Document

1. Set variables player1_losses, player2_losses, and computer_losses equal to 0
2. Set a variable, continue_playing, equal to boolean True 
3. Output a welcome message that explains the rules
4. While continue_playing is equal to boolean True:
   1. Set stick_count equal to 100
   2. Set player_turn equal to 1
   3. While player_turn is equal to 1:
      1. Output to user(s) that it is the computers turn
      2. If there are 4 sticks remaining:
         * Computer subtracts 3 sticks from pile
         * Output sticks taken
         * Output sticks left on table
         * Set player_turn equal to 2
      3. Otherwise, If there are 3 sticks remaining:
         * Computer subtracts 2 sticks from pile
         * Output sticks taken
         * Output sticks left on table
         * Set player_turn equal to 2
      4. Otherwise, If there are 2 sticks remaining:
         * Computer subtracts 1 stick from pile
         * Output sticks taken
         * Output sticks left on table
         * Set player_turn equal to 2
      5. Otherwise, If there is 1 stick remaining:
         * Computer takes last stick
         * Output sticks taken
         * Output loss message
         * Add 1 to computer_losses
         * Set player_turn equal to 4
      6. Otherwise If there is more than 4 sticks remaining
         * Computer takes a random number of sticks from 1-3
         * Output sticks taken
         * Output sticks left on table
         * Set player_turn equal to 2
   4. If player_turn is equal to 2, output that it is player 1's turn
   5. While player_turn is equal to 2:
      1. sticks_taken is set equal to an input from the user
      2. if sticks_taken is a digit: 
         * If sticks_taken is between 1 and 3 and less than stick_count:
           * Remove sticks_taken from the pile
           * Output sticks taken
           * Output sticks left on table
           * Set player_turn equal to 3
         * otherwise if sticks_taken is between 1 and 3 and is equal to stick_count:
            * Remove sticks_taken from the pile
            * Output sticks taken
            * Output loss message
            * Add 1 to player1_losses
            * Set player_turn equal to 4
         * otherwise output an error message reminding the user the input must be a number between 1 and 3 less than the current number of sticks
      3. otherwise output an error message reminding the user the input must be a number between 1 and 3 less than the current number of sticks
   6. If player_turn is equal to 3, output that it is player 1's turn
   7. While player_turn is equal to 3:
      1. sticks_taken is set equal to an input from the user
      2. if sticks_taken is a digit: 
         * If sticks_taken is between 1 and 3 and less than stick_count:
           * Remove sticks_taken from the pile
           * Output sticks taken
           * Output sticks left on table
         * otherwise if sticks_taken is between 1 and 3 and is equal to stick_count:
            * Remove sticks_taken from the pile
            * Output sticks taken
            * Output loss message
            * Add 1 to player1_losses
            * Set player_turn equal to 4
         * otherwise output an error message reminding the user the input must be a number between 1 and 3 less than the current number of sticks
   8. While player_turn is equal to 4:
      1. set a variable, play_again, to be equal to a user input
      2. if play_again in lowercase form is equal to 'yes':
         * output a message to the user that states a new round of sticks is starting
         * break code
      3. otherwise, if play_again in lowercase form is equal to 'no':
         * output computer_losses, player1_losses, and player2_losses to user
         * output a message thanking the player for playing
         * set continue_playing to boolean False
         * break code
      4. otherwise print an error message and remind the user to put in their answer as specifically the words 'yes' or 'no'

