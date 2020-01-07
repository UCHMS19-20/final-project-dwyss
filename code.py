# import pygame

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
    x=no swing")

class baseball:
    """baseball class"""
    
    def __init__(self, name, attribute1, attribute2, attribute3, attribute4):

        pitcher = baseball("Pitcher Man", "fastball", "curveball", "changeup", "slider")
        hitter = baseball("Batter Boy", "normal swing", "power swing", "contact swing", "no swing")

code.interact(local=locals())

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