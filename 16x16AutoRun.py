import pandas
import pygame
from mazes import *
from time import time,sleep
from numpy import savetxt
from random import randint as r
import random

path1 = 'C:/Users/Jack/PycharmProjects/QGame/PROPER16x16DATA/'
path5 = '.csv'
maze1 = Mazes()
maze2 = Mazes()
maze3 = Mazes()

terminals = maze1.getMaze3Terminals()



def select_action(current_state):
    global current_position, epsilon
    possible_actions = []
    if np.random.uniform(0, 1) <= epsilon:  # exploration
        global ModeFlag
        if current_position[0] != 0:
            possible_actions.append("up")
        if current_position[0] != n - 1:
            possible_actions.append("down")
        if current_position[1] != 0:
            possible_actions.append("left")
        if current_position[1] != n - 1:
            possible_actions.append("right")
        action = actions[possible_actions[r(0, len(possible_actions) - 1)]]
        ModeFlag = True
    else:  # Use Q table
        minQ = np.min(Q[current_state])
        if current_position[0] != 0:  # up movement possible
            possible_actions.append(Q[current_state, 0])
        else:
            possible_actions.append(minQ - 100)
        if current_position[0] != n - 1:  # down movement possible
            possible_actions.append(Q[current_state, 1])
        else:
            possible_actions.append(minQ - 100)
        if current_position[1] != 0:  # left movement possible
            possible_actions.append(Q[current_state, 2])
        else:
            possible_actions.append(minQ - 100)
        if current_position[1] != n - 1:  # right movement possible
            possible_actions.append(Q[current_state, 3])
        else:
            possible_actions.append(minQ - 100)
        action = random.choice([i for i, a in enumerate(possible_actions) if a == max(possible_actions)])
        ModeFlag = False
    return action

def epoch(terminals, reward):
    global safesteps, current_position, epsilon, its, wins, win1, win2, win3, win4, step, ouches
    current_state = states[(current_position[0], current_position[1])]
    action = select_action(current_state)
    if action == 0:  # move up
        current_position[0] -= 1
    elif action == 1:  # move down
        current_position[0] += 1
    elif action == 2:  # move left
        current_position[1] -= 1
    elif action == 3:  # move right
        current_position[1] += 1
    new_state = states[(current_position[0], current_position[1])]
    if new_state not in terminals:
        Q[current_state, action] += alpha * (
                    reward[current_position[0], current_position[1]] + gamma * (np.max(Q[new_state])) - Q[
                current_state, action])
        step += 1
        safesteps += 1
        if current_position == [7, 7]:
            win1 += 1
            win2 += 0
            win3 += 0
            win4 += 0
            wins += 1
            its += 1
            updateStacks()
            current_position = [0, 0]
            step = 0
            ouches = 0
            if epsilon > 0:
                epsilon -= EDegrade
        if current_position == [5, 12]:
            win1 += 0
            win2 += 1
            win3 += 0
            win4 += 0
            wins += 1
            its += 1
            updateStacks()
            current_position = [0, 0]
            step = 0
            ouches = 0
            safesteps = 0
            if epsilon > 0:
                epsilon -= EDegrade
        if current_position == [9, 15]:
            win1 += 0
            win2 += 0
            win3 += 1
            win4 += 0
            wins += 1
            its += 1
            updateStacks()
            current_position = [0, 0]
            step = 0
            ouches = 0
            if epsilon > 0:
                epsilon -= EDegrade
        if current_position == [13, 0]:
            win1 += 0
            win2 += 0
            win3 += 0
            win4 += 1
            wins += 1
            its += 1
            updateStacks()
            current_position = [0, 0]
            step = 0
            ouches = 0
            if epsilon > 0:
                epsilon -= EDegrade
    else:
        Q[current_state, action] += alpha * (
                    reward[current_position[0], current_position[1]] + gamma * (np.max(Q[new_state])) - Q[
                current_state, action])
        step += 1
        ouches += 1
    outState1.append(place)
    outStep1.append(step)
    outWins1.append(wins)

def epochAlt(terminals, reward):
    global current_position, epsilon, its, wins, win1, win2, win3, win4, step, safesteps, ouches
    current_state = states[(current_position[0], current_position[1])]
    action = select_action(current_state)
    if action == 0:  # move up
        current_position[0] -= 1
    elif action == 1:  # move down
        current_position[0] += 1
    elif action == 2:  # move left
        current_position[1] -= 1
    elif action == 3:  # move right
        current_position[1] += 1
    new_state = states[(current_position[0], current_position[1])]
    if new_state not in terminals:
        Q[current_state, action] += alpha * (
                    reward[current_position[0], current_position[1]] + gamma * (np.max(Q[new_state])) - Q[
                current_state, action])
        step += 1
        safesteps += 1
        if current_position == [0, 9]:
            win1 += 1
            win2 += 0
            win3 += 0
            win4 += 0
            wins += 1
            its += 1
            updateStacks()
            current_position = [0, 0]
            step = 0
            ouches = 0
            safesteps = 0
            if epsilon > 0:
                epsilon -= EDegrade
        if current_position == [5, 12]:
            win1 += 0
            win2 += 1
            win3 += 0
            win4 += 0
            wins += 1
            its += 1
            updateStacks()
            current_position = [0, 0]
            step = 0
            ouches = 0
            if epsilon > 0.1:
                epsilon -= EDegrade
        if current_position == [9, 15]:
            win1 += 0
            win2 += 0
            win3 += 1
            win4 += 0
            wins += 1
            its += 1
            updateStacks()
            current_position = [0, 0]
            step = 0
            ouches = 0
            if epsilon > 0.1:
                epsilon -= EDegrade
        if current_position == [13, 0]:
            win1 += 0
            win2 += 0
            win3 += 0
            win4 += 1
            wins += 1
            its += 1
            updateStacks()
            current_position = [0, 0]
            step = 0
            ouches = 0
            if epsilon > 0:
                epsilon -= EDegrade
    else:
        Q[current_state, action] += alpha * (
                    reward[current_position[0], current_position[1]] + gamma * (np.max(Q[new_state])) - Q[
                current_state, action])
        step += 1
        ouches += 1
    outState1.append(place)
    outStep1.append(step)
    outWins1.append(wins)

def updateStacks():
    outMoves.append(place)
    outSteps.append(step)
    outIts.append(its)
    outWin1.append(win1)
    outWin2.append(win2)
    outWin3.append(win3)
    outWin4.append(win4)
    outWins.append(wins)
    outMode.append(ModeFlag)
    outOuches.append(ouches)
    outSafeSteps.append(safesteps)
    outEpsilon.append(epsilon)
    outTest.append(test)
    outBaseE.append(baseE)

run1 = True
run2 = False
for Experiment in range(0,2,1):
    if Experiment == 0:
        rewards1 = maze1.getMaze3Rewards()
        colours1 = maze1.getMaze3Colours()
        path2 = 'Goal1/'
        run1 = True
        run2 = False
    if Experiment == 1:
        maze1.reset()
        rewards2 = maze2.getMaze3altRewards()
        terminals = maze1.getMaze3Terminals()
        colours2 = maze2.getMaze3altColours()
        path2 = 'Goal2/'
        run1 = False
        run2 = True
    for Eps in range(0, 5, 1):
        if Eps == 0:
            epsilon = 0
            baseE = 0
            path3 = 'E0_'
        if Eps == 1:
            epsilon = 0.25
            baseE = 0.25
            EDegrade = 0.003125
            path3 = 'E02_'
        if Eps == 2:
            epsilon = 1
            EDegrade = 0.0125
            baseE = 1
            path3 = 'E1_'
        if Eps == 3:
            epsilon = 0.5
            EDegrade = 0.00625
            baseE = 0.5
            path3 = "E05_"
        if Eps == 4:
            epsilon = 0.75
            EDegrade = 0.009375
            baseE = 0.75
            path3 = "E075_"
        for test in range(0,50,1):
            ds = str(test)
            path4 = ds
            safesteps = 0
            step = 0
            its = 0
            wins = 0
            win1 = 0
            win2 = 0
            win3 = 0
            win4 = 0
            ouches = 0
            state = 0
            outTest = []
            outSafeSteps = []
            outMode = []
            outSteps = []
            outIts = []
            outMoves = []
            outWins = []
            outWin1 = []
            outWin2 = []
            outWin3 = []
            outWin4 = []
            outOuches = []
            outState = []
            outState1 = []
            outWins1 = []
            outStep1 = []
            outEpsilon = []
            outBaseE = []
            #QTable: UP DOWN LEFT RIGHT
            Q = np.zeros((n ** 2, 4))

            ModeFlag = False

            actions = {"up": 0, "down": 1, "left": 2, "right": 3}
            states = {}

            k = 0
            for i in range(n):
                for j in range(n):
                    states[(i, j)] = k
                    k += 1

            alpha = 0.6
            gamma = 0.9

            current_position = [0, 0]

            while run1:
                layout(current_position, colours1)
                print(terminals)
                overlayAlt()
                pygame.display.flip()
                place = states[(current_position[0], current_position[1])]
                epoch(terminals,rewards1)
                if wins == 100:
                    QPath = path1 + path2 + "Q/" + path3 + path4 + 'Q' + path5
                    np.savetxt(QPath, Q, delimiter=',')
                    break
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

                sleep(0.2)
                print("Experiment: ", Experiment, "TEST: ", test, "Epsilon: ", epsilon, "iteration: ", its, "movement: ", current_position, "Win1: ", win1, "Win2: ", win2, "Win3", win3, "Win4", win4, "wins", wins, "Ouches: ", ouches)
            while run2:
                ##Alternate Goal##
                layout(current_position, colours2)
                overlayAlt()
                pygame.display.flip()
                place = states[(current_position[0], current_position[1])]
                epochAlt(terminals,rewards2)
                if wins == 100:
                    QPath = path1 + path2 + "Q/" + path3 + path4 + 'Q' + path5
                    np.savetxt(QPath, Q, delimiter=',')
                    break
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                #print("ouches: ", ouches, "  ", step)
                #print("Experiment: ", Experiment, "TEST: ", test, "Epsilon: ", epsilon, "iteration: ", its, "movement: ", current_position, "Win1: ", win1, "Win2: ", win2, "Win3", win3, "Win4", win4, "wins", wins, "Ouches: ", ouches)
            path = path1 + path2 + path3 + path5
            pathM = path1 + path2 + "M/" + path3 + path5
            dataMoves = pandas.DataFrame({"Wins": outWins1, "Step": outStep1, "place": outState1})
            dataMoves.to_csv(pathM, mode = 'a')
            data = pandas.DataFrame({"Test": outTest, "iteration ": outIts, "Step": outSteps, "Move": outMoves, "Ouches": outOuches,
                                     "Safe Steps": outSafeSteps, "Total Wins": outWins, "Wins1": outWin1, "Wins2": outWin2, "Wins3": outWin3, "Wins4": outWin4, "Exploration?": outMode,
                                     "Epsilon": outEpsilon})
            data.to_csv(path, mode='a')
            epsilon = baseE
            print("Experiment: ", Experiment, "Epsilon: ", epsilon,"TEST: ", test, "Win1: ", win1, "Win2: ", win2, "Win3", win3, "Win4", win4, "wins", wins, "Ouches: ", ouches)

pygame.quit()