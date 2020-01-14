# loading pygame
import sys
import pygame

#initiate the pygame
pygame.init()

# size of pygame window
screen = pygame.display.set_mode( (800, 450) )

# this doesn't work right now cause i still have to add a lot of stuff

# these are the set of rules/the introduction that will show up on the screen when the game is starting
print("Let's play baseball!!!")
print("Here are the rules:\
    One player will be a pitcher and the other will be the hitter.\
    Each of these players will have to chose between different types of pitches and hit.\
    For the pitcher:\
    f=fastball\
    v=curveball\
    e=changeup\
    s=slider\
    For the hitter:\
    n=normal_swing\
    p=power_swing\
    c=contact_swing\
    x=no_swing\
    now, you should be able to play!!!")

pitcher_choices = ['f', 'v', 'e', 's']
hitter_choices = ['n', 'p', 'c', 'x']

pitch_type = input(pitcher_choices)
hit_type = input(hit_type)

# load the image of the baseball field
background_image = pygame.image.load(baseball_field.png).convert()

# all of the data
ball = 0
# definition of a walk
while ball == 4:
    base += 1
strike = 0
while strike == 3:
    out += 1
out = 0
while out == 3:
    sys.exit()

# load the turtle, which will be the path that the baserunners take
import turtle as t
turtle.speed(8)
# turtle.pos(-,-)
# above is not finished, i will have to go through trial end error so i can insert the exact points

t.rt(-45)

def bases():
    """This is how the runners will advance"""
    
    for n in range(base):
        t.fd(50)
        t.rt(-90)

# this is where the various abilities that the players have are stored
class players:
    """players class"""
        
    def __init__(self, name, attribute1, attribute2, attribute3, attribute4):

        pitcher = players("Pitcher Man", "fastball", "curveball", "changeup", "slider")
        hitter = players("Batter Boy", "normal swing", "power swing", "contact swing", "no swing")

code.interact(local=locals())

# these are the various outcomes and results
# different for each combination of input for the two players
if pitch_type == 'f':
    if hit_type == 'n':
        print("Strike swinging!")
        strike += 1
    elif hit_type == 'p':
        print("Home run!")
        base += 4
    elif hit_type == 'c':
        print("Single!")
        base += 1
    elif hit_type == 'x':
        print("Stike looking!")
        strike += 1
elif pitch_type == 'v':
    if hit_type == 'n':
        print("Groundout!")
        out += 1
    elif hit_type == 'p':
        print("Strike swinging!")
        strike += 1
    elif hit_type == 'c':
        print("Single!")
        base += 1
    elif hit_type == 'x':
        print("Ball!")
        ball += 1
elif pitch_type == 'e':
    if hit_type == 'n':
        print("Double!")
        base += 2
    elif hit_type == 'p':
        print("Home run!")
        base += 4
    elif hit_type == 'c':
        print("Groundout!")
        out += 1
    elif hit_type == 'x':
        print("Ball!")
        ball += 1
elif pitch_type == 's':
    if hit_type == 'n':
        print("Lineout!")
        out += 1
    elif hit_type == 'p':
        print("Strike swinging!")
        strike += 1
    elif hit_type == 'c':
        print("Single!")
        base += 1
    elif hit_type == 'x':
        print("Ball!")
        ball += 1