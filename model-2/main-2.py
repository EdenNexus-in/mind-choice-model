import random as rm
import time
import difflib 

# possible actions
actions=['rock', 'paper', 'scissors']       

# agent's mind
mind={}

while True:
    time.sleep(1)
    #situvation
    sense = f"{rm.choice(actions)}${rm.choice(actions)}"
    print(f"Sense: {sense}")

    # initialize mind
    if sense not in mind:
        matches = difflib.get_close_matches(sense, mind.keys(), n=1, cutoff=0.6)
        if matches:
            print(f"Found match: {matches[0]}")
            mind[sense] = mind[matches[0]].copy()
        else:
            print(f"Found match: None")
            mind[sense] = [1] * len(actions)

    # discision
    act = rm.choices(actions, mind[sense],k=1)[0]
    print(f"Act: {act}")

    # env rule
    if sense == act:
        reward = 3
        got = "draw"
    elif (sense in 'rock' and act in 'scissors') or (sense in 'paper' and act in 'rock') or (sense in 'scissors' and act in 'paper'):
        reward = 5
        got = "win"
    else:
        reward = 1
        got = "lose"
    print(f"Got: {got}")

    # feedback
    mind[sense][actions.index(act)] = reward

    print(f"Mind: {mind}\n")