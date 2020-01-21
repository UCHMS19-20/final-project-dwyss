# these are the set of rules/the introduction that will show up on the screen when the game is starting
print("Let's play baseball!!!")
print("Here are the rules:")
print("One player will be a pitcher and the other will be the hitter.")
print("Each of these players will have to chose between different types of pitches and swings.")
print("For the pitcher:")
print("'f' = fastball")
print("'v' = curveball")
print("'e' = changeup")
print("'s' = slider")
print("For the hitter:")
print("'n' = normal swing")
print("'p' = power swing")
print("'c' = contact swing")
print("'x' = no swing")
print("Now, you should be able to play!!!")

# all of the stats in the game
balls = 0
strikes = 0
outs = 0
total_bases = 0
runs = 0

def determine_playable():
    if balls < 4:
        if strikes < 3:
            if outs < 3:
                return True
            elif outs >= 3:
                return False
        elif strikes >= 3:
            return False
    elif balls >= 4:
        return False

# dictionaries of the possible inputs for the players
pitch_choices = ['f', 'v', 'e', 's']
hitter_choices = ['n', 'p', 'c', 'x']

def get_pitch_type():
    global pitch_type
    pitch_choices = ['f', 'v', 'e', 's']
    pitch_type = input(pitch_choices)
    return pitch_type

def get_hit_type():
    global hit_type
    hitter_choices  = ['n', 'p', 'c', 'x']
    hit_type = input(hitter_choices)
    return hit_type

# these are the various outcomes and results
# different for each combination of input for the two players
def get_result():
    global balls
    global strikes
    global outs
    global total_bases
    global runs
    if pitch_type == 'f':
        if hit_type == 'n':
            print("Strike swinging!")
            strikes += 1
            print(f"Strike {strikes}!")
        elif hit_type == 'p':
            print("Home run!")
            total_bases += 4
        elif hit_type == 'c':
            print("Single!")
            total_bases += 1
        elif hit_type == 'x':
            print("Stike looking!")
            strikes += 1
            print(f"Strike {strikes}!")
    elif pitch_type == 'v':
        if hit_type == 'n':
            print("Groundout!")
            outs += 1
            print(f"{outs} outs!")
        elif hit_type == 'p':
            print("Strike swinging!")
            strikes += 1
            print(f"Strike {strikes}!")
        elif hit_type == 'c':
            print("Single!")
            total_bases += 1
        elif hit_type == 'x':
            balls += 1
            print(f"Ball {balls}!")
    elif pitch_type == 'e':
        if hit_type == 'n':
            print("Double!")
            total_bases += 2
        elif hit_type == 'p':
            print("Home run!")
            total_bases += 4
            runs += 1
            print(f"You have {runs} runs!")
        elif hit_type == 'c':
            print("Groundout!")
            outs += 1
            print(f"{outs} outs!")
        elif hit_type == 'x':
            balls += 1
            print(f"Ball {balls}!")
    elif pitch_type == 's':
        if hit_type == 'n':
            print("Lineout!")
            outs += 1
            print(f"{outs} outs!")
        elif hit_type == 'p':
            print("Strike swinging!")
            strikes += 1
            print(f"Strike {strikes}!")
        elif hit_type == 'c':
            print("Single!")
            total_bases += 1
        elif hit_type == 'x':
            balls += 1
            print(f"Ball {balls}!")

def determine_runs():
    global total_bases
    global runs
    return total_bases
    runs = total_bases // 4

def process():
    global balls
    global strikes
    global outs
    global total_bases
    while True:
        print(f"runs = {runs}")
        print(f"{balls} balls, {strikes} strikes, {outs} outs")
        get_pitch_type()
        get_hit_type()
        get_result()
        determine_runs()
        determine_playable()
    while False:
        if balls >= 4:
            print("Walk!")
            total_bases += 1
            balls = 0
            strikes = 0
        elif strikes >= 3:
            print("Strikeout!")
            outs += 1
            balls = 0
            strikes = 0
        elif outs >= 3:
            print("Change sides")
            balls = 0
            strikes = 0
            outs = 0

def baseball():
    determine_playable()
    process()

baseball()

# this is where the various abilities that the players have are stored
class players:
    """players class"""
        
    def __init__(self, name, attribute1, attribute2, attribute3, attribute4):

        pitcher = players("Pitcher Man", "fastball", "curveball", "changeup", "slider")
        hitter = players("Batter Boy", "normal swing", "power swing", "contact swing", "no swing")

# code.interact(local=locals())