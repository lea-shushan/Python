#Lea shushan

######  MISSION 3 ########

# You're writing a code for a tool which checks the numerology value
# of the given text.
# The basic option is to do this for the English texts only.

# gematria.py should contain

# ** Function create_numerology() gets no arguments.
# It imports abc string ('abcdefghijklmnopqrstuvwxyz') from another file.
# It initializes the empty "numerology" dictionary and a counter.
# It loops over the "abc" string, uses counter, creates 26 'key-value' pairs
# in the "numerology" dictionary like
# {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6, ... 'z':26},
# and returns this dictionary.

# ** Function get_score() that gets one string argument.
# It initializes the sum, creates "numerology" dictionary with
# numerology = create_numerology(), and uses the dictionary
# to find the score of the given string.
# It returns the score.
# We assume that the string contains the english letters only.

# For example get_score('corporation') returns 144,
#             get_score('') returns 0.

# ** Function get_input() that has no arguments.
# It prompts the user to enter a string to calculate it's numerology value.
# We assume that the input contains the english letters only -
# no need in validation.

# ** Two calls for the function get_score().
# In the first it gets an empty string as an argument.
# In the second it gets get_input() as an argument.

# Working menu.py with the above details grant you 30 points.

# BONUS CHALLENGE: get_input() makes validation - checks that there are no digits or
# makes the user to enter the input with no digits.



# BONUS CHALLENGE: Add Hebrew option. For gematria calculation
# import the next lists:
# digits = ['','א','ב','ג','ד','ה','ו','ז','ח','ט']
# tens = ['','י','כ','ל','מ','נ','ס','ע','פ','צ']
# hundreds = ['','ק','ר','ש','ת']
# and use their indicies.
# Before starting the calculation ask if the score should be calculated
# for an English or a Hebrew string.


import abc_guematria_import as a
import hebrew_guematria_import as h


def create_numerology():
    
    
    # dictionnary for each language 
    numerology_en = {}
    numerology_he = {} 


    # variable that will be used for guematria values
    counter = 1

    
    # for loop to create dictionnary with appropriate guematria values
    for i in a.abc:
        numerology_en[i] = counter
        counter += 1
    counter = 1
    for i in h.digits:
        numerology_he[i] = counter
        counter += 1
    for i in h.tens:
        numerology_he[i] = counter
        counter += 10
    for i in h.hundreds:
        numerology_he[i] = counter
        counter += 100



    # return two dictionnaries
    return numerology_en,numerology_he



def get_score(input_string):


    numerology_en,numerology_he = create_numerology() 

    sum = 0
    
    
    input_string = input_string.lower()

    # for loop to calculate guematria for each letter with he or en check
    for i in input_string:
        if i in numerology_en:
            sum += numerology_en[i]
        elif i in numerology_he:
            sum+= numerology_he[i]
        else:
            print('Incorect language!')
    return sum        




# BONUS CHALLENGE: get_input() makes validation - checks that there are no digits or
# makes the user to enter the input with no digits.


def get_input():
    
    user = input("Enter a string to get its value: ")

    #remove spaces because isalpha function doesn't accept it    
    user = user.replace(' ', '')
    
    # check for digits in the input string with .isalpha() fuction
    if not user.isalpha() :
        print("Please enter only alphbetic letters ")       
        return get_input()
    
    #print the result of calculate gematria's function
    print(get_score(user))


#get_input()

