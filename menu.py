#Lea Shushan

######  MISSION 4 ########


# You're creating the script that unites all the parts you've created till now.

# menu.py should contain

# ** Necessary imports

# ** Function show_menu() gets no arguments.
# It displays menu like this:
#     What do you like to do?
#       1. Change traffic light
#       2. Check palindrome
#       3. Calculate gematria value
#       Quit (q/Q)

# ** Function get_input() that gets 1,2,3,q or Q.
# Make the user to enter a valid input.

# ** Infinite loop that shows the menu, gets the input and
# performs 1,2,3 or quits.

# Working menu.py with the above details grant you 20 points.



import traffic_lights 
import palindromes
import guematria
import dice
import time


def show_menu():

    while True:
        user_choice = input(""" 
What do you like to do?
1. Change traffic light
2. Check palindrome
3. Calculate gematria value
4. Dice
5. Pig
6. Quit
""")

        if user_choice == '1':
            traffic_lights.update_light_challenge()
            time.sleep(1)
        elif user_choice == '2':
            palindromes.run_palindromes()
            time.sleep(1)
        elif user_choice == '3':
            guematria.get_input()
            time.sleep(1)
        elif user_choice == '4':
            dice.dice()
            time.sleep(1)
        elif user_choice == '5':
            dice.pig()
            time.sleep(1)
        elif user_choice == '6':
            break
        else:
            print('Your choice isn\'t a valid option!')

            

# Catch the Ctrl-C error and control it to notify the exit of the program
try:
    print("Press Ctrl-C to quit")
    show_menu()
except KeyboardInterrupt:    
    exit('\n\nYou pressed Ctrl-C \nExiting ...')


