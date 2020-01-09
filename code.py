import pygame

# this doesn't work right now cause i still have to add a lot of stuff

# these are the set of rules/the introduction that will show up on the screen when the game is starting
print("Let's play baseball!!!")
print("Here are the rules:\
    One player will be a pitcher and the other will be the hitter.\
    Each of these players will have to chose between different types of pitches and hit.\
    For the pitcher:\
    f=fastball\
    c=curveball\
    e=changeup\
    s=slider\
    For the hitter:\
    n=normal swing\
    p=power swing\
    c=contact swing\
    x=no swing\
    now, you should be able to play!!!")

# this is where the various abilities that the players have are stored
class players:
    """players class"""
        
    def __init__(self, name, attribute1, attribute2, attribute3, attribute4):

        pitcher = players("Pitcher Man", "fastball", "curveball", "changeup", "slider")
        hitter = players("Batter Boy", "normal swing", "power swing", "contact swing", "no swing")

code.interact(local=locals())

# this is where the base runners are drawn
import turtle as t
t.rt(315)
t.fd(250)

# these are the various outcomes and results
# different for each combination of input for the two players
if pitcher.input == fastball:
    if hitter.input == normal swing:
        print("Strike swinging!")
        strikes += 1
    elif hitter.input == power swing:
        print("Home run!")
        bases += 4
    elif hitter.input == contact swing:
        print("Single!")
        bases += 1
    elif hitter.input == no swing:
        print("Stike looking!")
        strikes += 1
elif pitcher.input == curveball:
    if hitter.input == normal swing:
        print("Groundout!")
        outs += 1
    elif hitter.input == power swing:
        print("Strike swinging!")
        strikes += 1
    elif hitter.input == contact swing:
        print("Single!")
        bases += 1
    elif hitter.input == no swing:
        print("Ball!")
        balls += 1
elif pitcher.input == changeup:
    if hitter.input == normal swing:
        print("Double!")
        bases += 2
    elif hitter.input == power swing:
        print("Home run!")
        bases += 4
    elif hitter.input == contact swing:
        print("Groundout!")
        outs += 1
    elif hitter.input == no swing:
        print("Ball!")
        balls += 1
elif pitcher.input == slider:
    if hitter.input == normal swing:
        print("Lineout!")
        outs += 1
    elif hitter.input == power swing:
        print("Strike swinging!")
        strikes += 1
    elif hitter.input == contact swing:
        print("Single!")
        bases += 1
    elif hitter.input == no swing:
        print("Ball!")
        balls += 1