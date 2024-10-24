### Part Two -- your code goes here. 

import random 

def generator():
    global x
    x = random.randint(1,100)
    
def output():
    guess = None      #using None to say it's an empty variable rn
    while guess != x:
        guess = int(input("Guess a number between 1 to 100: "))
        if guess > x:
            print("Too high")
        elif guess < x:
            print("Too low")
        else:
            pass
    print("Well done! The number was", x)
generator()
output()