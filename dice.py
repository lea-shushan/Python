
#Lea shushan

######  MISSION 4 ########



# BONUS CHALLENGE: Add to the menu "4. Throw a die with your friends"
# Use for this dice.py that will contain the next parts:
#
# ** Input the list of the players, for example,
#    ['Margaret','Mike','Jane','John'], and the maximal score.
# ** Make necessary validations.
# ** Go over the list and create a dictionary to store their scores.
# ** Throw a die for each player (random 1-6) and add to the score unti somebody
#    gets the maximal score and wins.
# ** Praize the winner



from random import randint
from time import sleep

def dice():

    # New input for all the players that will be separate into a list , with split() fuction
    players_name = input("Enter players' name with space: ").split(' ')
    
    max_score = 10

    # Dictionnary for all players' scores
    scores = {}
        
    # Put all payers' name in the dictionary + with value scores = 0 at this time..
    for player in players_name:
        scores[player] = 0

    while True:
        # this for loop is for each players' turn 
        for player in players_name:
            input(f"{player} Press 'Enter' to throw the dice ")
            score = randint(1,6)
            print(f"{player} scores {score}")
            sleep(0.5)
            # adding turn's score to the total score of the player
            scores[player] += score
            print(f"scores : {scores}")
            sleep(0.5)
            # when the player reached the max_score , the game ends
            if scores[player] >= max_score:
                print(f"{player} won the game with {max_score} points")
                sleep(1)
                return
#dice()




# BONUS CHALLENGE CHALLENGE: Change "4. Throw a die with you friends"
# to be "4. Play pig dice with you friends".
# Make the scores according to the pig dice rules (thanks to Wikipedia):
#
# Each turn, a player repeatedly rolls a die until either a 1 is rolled
# or the player decides to "hold":
#
# If the player rolls a 1, they score nothing and it becomes the next player's turn.
# If the player rolls any other number, it is added to their turn total and the player's turn continues.
# If a player chooses to "hold", their turn total is added to their score, and it becomes the next player's turn.
#The first player to score 100 or more points wins.

#For example, the first player, Donald, begins a turn with a roll of 5. Donald could hold and score 5 points, but chooses to roll again. Donald rolls a 2, and could hold with a turn total of 7 points, but chooses to roll again. Donald rolls a 1, and must end his turn without scoring. The next player, Alexis, rolls the sequence 4-5-3-5-5, after which she chooses to hold, and adds her turn total of 22 points to her score.

def pig():
    

    # New input for all the players that will be separate into a list , with split() fuction
    players = input("Enter players' name with space: " ).split(' ') 

    max_score = 100


    # Dictionnary for all players' scores
    scores = {} 

    # Put all payers' name in the dictionary + with value scores = 0 at this time..
    for player in players:
        scores[player] = 0
    
    while True:
        # this for loop is for each players' turn 
        for player in players:
            # score = it's the actual turn's score
            score = 0
            while True:
                input(f'{player} Press "Enter" to throw the dice ')
                dice = randint(1,6)
                print(f"{player}, you did {dice}")
                sleep(1) 
                # If the player rolls a 1, they score nothing and it becomes the next player's turn with the break statement
                if dice == 1:
                    print(f"{player}, End of your turn")
                    break
                # adding to the actual turn's score 
                score += dice
                # If the player rolls any other number, it is added to their turn total and the player's turn continues.
                if input(f'{player}\'s points are: {score}\n{player}, Do you want to continue or hold your points? (C\H) ').upper()[:1] == 'C':
                    continue
                # If a player chooses to "hold", their turn total is added to their score, and it becomes the next player's turn.
                else:
                    scores[player] += score
                    print(f'This turn you won {score} and your total points are {scores[player]}')
                    break
            print(f"Total scores : {scores}")
            #The first player to score 100 or more points wins.
            if scores[player] >= max_score:
                print(f"{player} won the game with {scores[player]} points")
                return
#pig()

