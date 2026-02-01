import random as rm
import time


actions=['rock', 'paper', 'scissors']

mind={}


while True:
    time.sleep(1)

    #situvation
    sense = rm.choice(actions)
    if sense not in mind:
        mind[sense] = [1] * len(actions)

    act = rm.choices(actions, mind[sense],k=1)[0]

    if sense == act:
        reward = 1
    elif (sense == 'rock' and act == 'scissors') or (sense == 'paper' and act == 'rock') or (sense == 'scissors' and act == 'paper'):
        reward = 1
    else:
        reward = 5

    mind[sense][actions.index(act)] += reward

    print(f"Sense: {sense}, Act: {act}, Reward: {reward}, Mind: {mind}")
