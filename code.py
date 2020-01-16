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
    Now, you should be able to play!!!")

def get_pitch_type():
    pitch_choices = ['f', 'v', 'e', 's']
    pitch = input("select a pitch type")
    return pitch

get_pitch_type()

pitch_choices = ['f', 'v', 'e', 's']
pitch = input(pitch_choices)
print(pitch)

def get_hit_type():
    """Return the type of hit that the hitter will select"""
    hitter_choices = ['n', 'p', 'c', 'x']
    hit_type = input(hitter_choices)
    return

# following code used as comment temporarily
# so that it can still be in code but will not be used for now
#pitcher_choices = ['f', 'v', 'e', 's']
#hitter_choices = ['n', 'p', 'c', 'x']
#pitch_type = input(pitcher_choices)
#hit_type = input(hit_type)

# all of the data
balls = 0
strikes = 0
outs = 0
bases = 0
away_team_runs = 0
home_team_runs = 0
# definition of a walk
while balls == 4:
    bases += 1
    balls = 0
    strikes = 0
while strikes == 3:
    outs += 1
    balls = 0
    strikes = 0
while outs == 3:
    # change sides
    balls = 0
    strikes = 0
    outs = 0
while bases == 4:
    team += 1

# these are the various outcomes and results
# different for each combination of input for the two players
if pitch_type == 'f':
    if hit_type == 'n':
        print("Strike swinging!")
        strikes += 1
    elif hit_type == 'p':
        print("Home run!")
        bases += 4
    elif hit_type == 'c':
        print("Single!")
        bases += 1
    elif hit_type == 'x':
        print("Stike looking!")
        strikes += 1
elif pitch_type == 'v':
    if hit_type == 'n':
        print("Groundout!")
        outs += 1
    elif hit_type == 'p':
        print("Strike swinging!")
        strikes += 1
    elif hit_type == 'c':
        print("Single!")
        bases += 1
    elif hit_type == 'x':
        print("Ball!")
        balls += 1
elif pitch_type == 'e':
    if hit_type == 'n':
        print("Double!")
        bases += 2
    elif hit_type == 'p':
        print("Home run!")
        bases += 4
    elif hit_type == 'c':
        print("Groundout!")
        outs += 1
    elif hit_type == 'x':
        print("Ball!")
        balls += 1
elif pitch_type == 's':
    if hit_type == 'n':
        print("Lineout!")
        outs += 1
    elif hit_type == 'p':
        print("Strike swinging!")
        strikes += 1
    elif hit_type == 'c':
        print("Single!")
        bases += 1
    elif hit_type == 'x':
        print("Ball!")
        balls += 1

# this is where the various abilities that the players have are stored
class players:
    """players class"""
        
    def __init__(self, name, attribute1, attribute2, attribute3, attribute4):

        pitcher = players("Pitcher Man", "fastball", "curveball", "changeup", "slider")
        hitter = players("Batter Boy", "normal swing", "power swing", "contact swing", "no swing")

code.interact(local=locals())