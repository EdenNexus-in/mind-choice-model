import random as rm
import time

# possible actions
actions=['rock', 'paper', 'scissors']

# agent's mind
mind={}

while True:
    time.sleep(1)

    #situvation
    sense = rm.choice(actions)
    print(f"Sense: {sense}")

    # initialize mind
    if sense not in mind:
        mind[sense] = [1] * len(actions)

    # discision
    act = rm.choices(actions, mind[sense],k=1)[0]
    print(f"Act: {act}")

    # env rule
    if sense == act:
        reward = 3
        got = "draw"
    elif (sense == 'rock' and act == 'scissors') or (sense == 'paper' and act == 'rock') or (sense == 'scissors' and act == 'paper'):
        reward = 5
        got = "win"
    else:
        reward = 1
        got = "lose"
    print(f"Got: {got}")

    # feedback
    mind[sense][actions.index(act)] = reward

    print(f"Mind: {mind}\n")
