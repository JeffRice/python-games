# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui


# initialize global variables used in your code
secret_number = random.randrange(0, 100)
user_guess = 1
guesses = 7
game = 'low'


# define event handlers for control panel
def output():
    global secret_number, user_guess, guesses
    print secret_number
    print user_guess
    print guesses
    


     # button that changes range to range [0,100) and restarts
def secret_low():
    global secret_number, user_guess, guesses, game
    secret_number = random.randrange(0, 100)
    guesses = 7
    game = 'low'
    print 'New Game! Range is from 0 to 100'
    return
     # button that changes range to range [0,1000) and restarts
def secret_high():
    global secret_number, guesses, game
    secret_number = random.randrange(0, 1000)
    guesses = 10
    game = 'high'
    print 'New Game! Range is from 0 to 1000'
    return
    # main game logic goes here	
def too_high():
    global secret_number, user_guess, guesses, game
    if guesses == 0:
        print 'Out of guesses!'
        if game == 'high':
            secret_high()
            return
        else:
            secret_low()
            return
    print 'You guessed ' + str(user_guess)
    print 'Lower'
    print 'You have ' + str(guesses) + ' guesses remaining'
    
def too_low():
    global secret_number, user_guess, guesses, game
    if guesses == 0:
        print 'Out of guesses!'
        if game == 'high':
            secret_high()
            return
        else:
            secret_low()
            return
    print 'You guessed ' + str(user_guess)
    print 'Higher'
    print 'You have ' + str(guesses) + ' guesses remaining'
    
def correct():
    global secret_number, user_guess, guesses
    print 'You guessed ' + str(user_guess)
    print 'That is Correct!'
    if game == 'high':
        secret_high()
        return
    else:
        secret_low()
        return
    
def user_inp(guess):
    global user_guess, secret_number, guesses
    user_guess = float(guess)
    if user_guess == secret_number:
        correct()
    elif user_guess > secret_number:
        guesses = guesses - 1
        too_high()
    else:
        guesses = guesses - 1
        too_low()

# create frame
frame = simplegui.create_frame("Guessing Game", 300, 300)

# register event handlers for control elements
frame.add_button("Range (0, 100)", secret_low, 100)
frame.add_button("Range (0, 1000)", secret_high, 100)
frame.add_input("Guess", user_inp, 100)
frame.add_button("output", output, 100)

# start frame
secret_low()

# always remember to check your completed program against the grading rubric
