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

# determine whether or not the input is ready to be received
def determine_playable():
    global balls
    global strikes
    global outs
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

# if the input is not ready, this will change the stats to make it true
def make_true():
    global balls
    global strikes
    global aouts
    if balls >= 4:
        print("Walk!")
        total_bases += 1
        balls = 0
        strikes = 0
        return balls
        return strikes
        return total_bases
        return True
    elif strikes >= 3:
        print("Strikeout!")
        outs += 1
        balls = 0
        strikes = 0
        return balls
        return strikes
        return outs
        return True
    elif outs >= 3:
        print("That's 3 outs!")
        balls = 0
        strikes = 0
        outs = 0
        return balls
        return strikes
        return outs

# where the input of the pitch type is gotten from
def get_pitch_type():
    global pitch_type
    pitch_choices = ['f', 'v', 'e', 's']
    pitch_type = input(pitch_choices)
    return pitch_type

# where the input of the hit type is gotten from
def get_swing_type():
    global swing_type
    hitter_choices  = ['n', 'p', 'c', 'x']
    swing_type = input(hitter_choices)
    return swing_type

# how the number of runs that the player has is calculated
def determine_runs():
    global total_bases
    return total_bases
    runs = total_bases // 4
    print(f"runs = {runs}")

# these are the various outcomes and results and vary for each combo of inputs
def get_result():
    global balls
    global strikes
    global outs
    global total_bases
    global runs
    if pitch_type == 'f':
        if swing_type == 'n':
            print("Strike swinging!")
            strikes += 1
            return strikes
            print(f"Strike {strikes}!")
            determine_playable()
        elif swing_type == 'p':
            print("Home run!")
            total_bases += 4
            return total_bases
            return_runs()
            determine_playable()
        elif swing_type == 'c':
            print("Single!")
            total_bases += 1
            return total_bases
            return_runs()
            determine_playable()
        elif swing_type == 'x':
            print("Stike looking!")
            strikes += 1
            return strikes
            print(f"Strike {strikes}!")
            determine_playable()
    elif pitch_type == 'v':
        if swing_type == 'n':
            print("Groundout!")
            outs += 1
            return outs
            print(f"{outs} outs!")
            determine_playable()
        elif swing_type == 'p':
            print("Strike swinging!")
            strikes += 1
            return strikes
            print(f"Strike {strikes}!")
            determine_playable()
        elif swing_type == 'c':
            print("Single!")
            total_bases += 1
            return total_bases
            return_runs()
            determine_playable()
        elif swing_type == 'x':
            balls += 1
            return balls
            print(f"Ball {balls}!")
            determine_playable()
    elif pitch_type == 'e':
        if swing_type == 'n':
            print("Double!")
            total_bases += 2
            return total_bases
            return_runs()
            determine_playable()
        elif swing_type == 'p':
            print("Home run!")
            total_bases += 4
            return total_bases
            return_runs()
            determine_playable()
        elif swing_type == 'c':
            print("Groundout!")
            outs += 1
            return outs
            print(f"{outs} outs!")
            determine_playable()
        elif swing_type == 'x':
            balls += 1
            return balls
            print(f"Ball {balls}!")
            determine_playable()
    elif pitch_type == 's':
        if swing_type == 'n':
            print("Lineout!")
            outs += 1
            return outs
            print(f"{outs} outs!")
            determine_playable()
        elif swing_type == 'p':
            print("Strike swinging!")
            strikes += 1
            return strikes
            print(f"Strike {strikes}!")
            determine_playable()
        elif swing_type == 'c':
            print("Single!")
            total_bases += 1
            return total_bases
            return_runs()
            determine_playable()
        elif swing_type == 'x':
            balls += 1
            return balls
            print(f"Ball {balls}!")
            determine_playable()

# the order in which the functions will run
def baseball():
    global balls
    global strikes
    global outs
    global total_bases
    determine_playable
    while True:
        print(f"{balls} balls, {strikes} strikes, {outs} outs")
        get_pitch_type()
        get_swing_type()
        get_result()
    while False:
        make_true()

baseball()