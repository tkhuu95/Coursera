import simplegui
import random

# global variable
num_range = 100

# helper function to start and restart the game
def new_game():
    global secret_number, num_range, num_of_guesses
    print
    
    if num_range == 100:
        secret_number = random.randrange(100)
        num_of_guesses = 7
        print "New game - Range is [0, 100)"
        print "Number of remaining guesses is 7"
        
    elif num_range == 1000:
        secret_number = random.randrange(1000)
        num_of_guesses = 10
        print "New game - Range is [0, 1000)"
        print "Number of remaining guesses is 10"
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = 1000
    new_game()
    
def input_guess(guess):
    print
    print "Guess was " + guess
    
    global num_of_guesses
    num_of_guesses -= 1
    print "Number of remaining guesses is " + str(num_of_guesses)
    
    if (num_of_guesses == 0) and (int(guess) != secret_number):
        print "You ran out of guesses. The number was " + str(secret_number)
        new_game()
        
    elif int(guess) > secret_number: print "Lower!"
   
    elif int(guess) < secret_number: print "Higher!"
        
    elif int(guess) == secret_number: 
        print "Correct!"
        new_game()

# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0,1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)
frame.start()

new_game()
