#Lea Shushan 

######  MISSION 1 ########


# You're writing code to control your town's traffic lights. 
# You need a function to handle each change from green, to yellow, 
# to red, and then to green again. It means, if the function
# gets 'red' or 'RED', it should return 'green'.

# The function takes a string as an argument 
# representing the current state of the light 
# and returns a string representing the state the light should change to.

# For example, update_light('green') should return 'yellow'.

# traffic_lights.py contents should look like

### def update_light(curr_light) : - function header
### function body that consists of 
### if - elif - else that return or light color or "invalid color" message

### print(update_light('green'))
### print(update_light('YELLOW'))

# Working traffic_lights.py with above details grant you 30 points.

# BONUS CHALLENGE:
# Instead of if - elif - else construct you may use dictionary.
# In this case assume there is no invalid input.


# green -> yellow -> red -> green
def update_light(curr_light):
    
    curr_light = curr_light.lower()

    if curr_light == 'green':
        return 'yellow'
    elif curr_light == 'yellow':
        return 'red'
    elif curr_light == 'red':
        return 'green'
    else:
        return 'invalid color'

#for exemple:
# print(update_light('green'))
# print(update_light('YELLOW'))

#update_light()




# BONUS CHALLENGE:
# Instead of if - elif - else construct you may use dictionary.
# In this case assume there is no invalid input.

def update_light_challenge():

    curr_light = int(input("Choose the actual state of the traffic lights:\n1. Green\n2. Yellow\n3. Red\n"))

    next_light = {1:'yellow', 2:'red', 3:'green'}

    return print(next_light[curr_light])


#update_light_challenge()

