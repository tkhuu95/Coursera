# Thomas Khuu
# June 2015 - July 2015

import random
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    if name == 'rock': return 0
    elif name == 'Spock': return 1
    elif name == 'paper': return 2
    elif name == 'lizard': return 3
    elif name == 'scissors': return 4

def number_to_name(number):
    if number == 0: return 'rock' 
    elif number == 1: return 'Spock'
    elif number == 2: return 'paper'
    elif number == 3: return 'lizard'
    elif number == 4: return 'scissors'

def rpsls(player_choice): 
    print
    
    print "Player chooses " + player_choice
    
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(5)
    comp_choice = number_to_name(comp_number)
    
    print "Computer chooses " + comp_choice
    
    result = (comp_number - player_number) % 5
    
    if result == 1 or result == 2: print "Computer wins!"
    elif result == 3 or result == 4: print "Player wins!"
    else: print "Player and computer tie!"
    
# TEST
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
