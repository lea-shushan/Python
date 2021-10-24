#Lea Shushan

######  MISSION 2 ########

# You're writing a code for a tool which checks if the  given text
# is a palindrome.
# Palindrome is a text that is being read the same in any direction.

# palindromes.py should contain

# ** Import of "palindromes" list from another file.
# Example of the "palindromes" list : ['level','Anna','racecar','madam','mom','noon','radar','kayak','wow',"Don't nod","my gym",'I did, did I?','Red rum, sir, is murder','Step on no pets','Was it a cat I saw?','Eva, can I see bees in a cave?','no melon, no lemon','never odd or even','A nut for a jar of tuna.','Amore, Roma!',"Don't do!",'Borrow or rob?',"King, are you glad you are king?",'Was it a car or a cat I saw?','Dennis, Nell, Edna, Leon, Nedra, Anita, Rolf, Nora, Alice, Carol, Leo, Jane, Reed, Dena, Dale, Basil, Rae, Penny, Lana, Dave, Denny, Lena, Ida, Bernadette, Ben, Ray, Lila, Nina, Jo, Ira, Mara, Sara, Mario, Jan, Ina, Lily, Arne, Bette, Dan, Reba, Diane, Lynn, Ed, Eva, Dana, Lynne, Pearl, Isabel, Ada, Ned, Dee, Rena, Joel, Lora, Cecil, Aaron, Flora, Tina, Arden, Noel, and Ellen sinned.',"Madam, in Eden, I’m Adam.",'Murder for a jar of red rum','רק פושטק עלוב בולע קטשופ קר','מחר קר? חם!','מי אמר שיש רמאים?','ילד כותב בתוך דלי']

# ** Function check_palindrome that takes string as an argument, strips it
# of all the characters as spaces, quotes, exclamation 
# and question signs, dots, commas - which are not affect palindromes.
# For this purpose it uses several times replace() method.
# After this the string is compared to it's reversed variant.
# Eventually the function returns True if the given string is a palindrome
# and False if not.

# For example check_palindrome('Yey! ') returns True,
#             check_palindrome('Hugs and kisses and hugs') returns False.

# ** Function get_random() that has no arguments. It returns randomly
# a string from the palindromes list (there are not only palindromes).

# for example,         get_random() may return "Was it a cat I saw?"
# in one more example, get_random() may return ""Don't do!""

# ** Function get_input() has no arguments. It asks the user to input 
# a string on purpose to check if it is a palindrome, and returns the string.
# No need to validate the input.

# ** Function show_palindrome() has one string argument. It uses 
# show_palindrome() to check if it is a palindrome.
# After that shows the string with the appropriate title.

# For example, show_palindrome("Was it a cat I saw?") prints 
#                         "Was it a cat I saw?" is a palindrome
#          or, show_palindrome("That thing is closer than that") prints
#                         "That thing is closer than that" is not a palindrome

# ** Function run_palindromes() without arguments, but containing
# two calls for the function show_palindrome.
# In the first it gets get_random() as an argument.
# In the second it gets get_input() as an argument.

# ** Call for the function palindromes()

# Example 1: if you input a string "-Lol", you get
#  <random string> is <not> a palindrome
#  '-Lol' is a palindrome

# Example 2: if you input a string 'never say "never"', you get
#  <random string> is <not> a palindrome
#  'never say "never"' is not a palindrome

# Example 3: if you input a string '548 ?.45', you get
#  <random string> is <not> a palindrome
#  '548 ?.45' is a palindrome

# Example 4: if you input an empty string, you get
#  <random string> is <not> a palindrome
#  '' is a palindrome

# Working palindromes.py with the above details grant you 30 points.

# BONUS CHALLENGE: For the function check_palindrome(str). 
# Put all the characters we should remove from the string
# into a list and go over it with replace() method in a loop instead
# of repeating replace() method several times.

# BONUS CHALLENGE CHALLENGE: For the function check_palindrome(str).
# Import "re" module. Learn about re.sub() method and use it.



from import_palindromes import palindromes_list
import random
import re

def check_palindrome(input_string):
    # remove invalid characters with a for loop through a list of invalid charcaters
    invalid_chars = [',', '?', ' ', '!', '.', '"', '\'', '’']
    for symbol in invalid_chars:
        input_string = input_string.replace(symbol, '')
    
    
    # remove invalid characters for the challenge challenge with re.sub()
    input_string = re.sub(r"[\!|\?|,|\"|\'|`| ]", '', input_string)
    

    input_string = input_string.lower() 


    input_string= input_string.replace('ן', 'נ')
    input_string= input_string.replace('ץ', 'צ')
    input_string= input_string.replace('ם', 'מ')
    input_string= input_string.replace('ף', 'פ')
    input_string= input_string.replace('ך', 'כ')

    # palindrome verification , with reverse string
    if input_string == input_string[::-1]:
        return True
    else:
        return False


def get_random():
    return random.choice(palindromes_list)

def get_input():
    return input('Enter a Palindrome: ')


def show_palindrome(palindrome):
    True_palindrome = check_palindrome(palindrome)

    if(True_palindrome):
        print(palindrome + ' is a palindrome')
    else:
        print(palindrome + ' is not a palindrome')

def run_palindromes():
    print("First part random from the list and check it")
    palindrome = get_random()
    show_palindrome(palindrome)

    print("Second part inpur from the user")
    palindrome = get_input()
    show_palindrome(palindrome)


#run_palindromes()



