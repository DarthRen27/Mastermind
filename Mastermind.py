# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 18:23:44 2022

@author: Justin
"""

import random

def aiselection(colors):
    aicount = 0
    selection = []
    while aicount < 4:
        grab = random.randint(0,7)
        if colors[grab] not in selection:
            selection.append(colors[grab])
            aicount += 1
    return selection

def player():
    choice = []
    playcount = 0
    while playcount < 4:
        color = input("Enter the color you think is at position " + str(playcount) + ". Options are RED, BLUE, YELLOW, ORANGE, PURPLE, BROWN, PINK, NOTHING: ")
        choice.append(color.upper())
        playcount += 1
    return choice

def playeraffirmation():
    correction = ""
    verdict = []
    playcount = 0
    while playcount < 4:
        correction = input("If position " + str(playcount) + " is the correct color and is in the correct space enter BLACK, if it is the correct color but in the wrong space enter WHITE, if it is not the correct color or space enter NOTHING: ")
        verdict.append(correction.upper())
        playcount += 1
    return verdict
    
def aiaffirmation(plan, check):
    affirmation = ""
    aicount = 0
    aicount2 = 0
    correct = False
    while aicount < 4:
        while aicount2 < 4:
            if check[aicount] == plan[aicount2]:
                if aicount2 == aicount:
                    affirmation += "BLACK "
                    correct = True
                else:
                    affirmation += "WHITE "
                    correct = True
            if correct == True:
                aicount2 += 4
            else:
                aicount2 += 1
        if correct == False:
            affirmation += "NOTHING "
        correct = False
        aicount2 = 0
        aicount += 1
    return affirmation
        

colors = "RED", "BLUE", "YELLOW", "ORANGE", "PURPLE", "BROWN", "PINK", "NOTHING"
possibles = "RED", "BLUE", "YELLOW", "ORANGE", "PURPLE", "BROWN", "PINK", "NOTHING"
guess = []
aiguess = []
count = 0
count2 = 0
newguess = []
change = []
noplace = []
correct = {}
oldpos = 0
newpos = 0
aicheck = {}
go = False

ai = input("Do you want to be the mastermind? Yes or No: ")
dev = input("Do you want to check that everything is working: ")

if ai == "No":
    plan = aiselection(colors)
    if dev == "Yes":
        print(plan)
    while count < 10:
        out = ""
        check = player()
        out = aiaffirmation(plan, check)
        print(out)
        if out == "BLACK BLACK BLACK BLACK ":
            print("That's correct, you win")
            count += 10
        count += 1
    if count == 10:
        print("You've lost, the plan was " + plan)
        
else:
    plan = player()
    aiguess = aiselection(colors)
    print("The AI guesses " + aiguess + ". Please affirm")
    rw = playeraffirmation(aiguess)
    while count < 9:
        while count2 < 4:
            if rw[count2] == "BLACK":
                correct[count2] = rw[count2]
            elif rw[count2] == "WHITE":
                change.append((count2,rw[count2]))
            else:
                newguess.append(count2)
            count2 += 1
        if len(change) != 0:
            if len(change) > 1:
                if len(correct) != 0:
                    
                    pass
                else:
                    aiguess = []
                    while check < len(change):
                        oldpos = check
                        newpos = random.randint(1,4)
                        if newpos != oldpos:
                            aiguess[newpos] = aiguess[oldpos]
            else:
                if len(correct) != 0:
                    oldpos = change[0][0]
                    noplace = list(correct.keys())
                    while go != True:
                        newpos = random.randint(1,4)
                        if newpos not in noplace:
                            aiguess[newpos] = change[0][1]
                            go = True
                else:
                    while go != True:
                        newpos = random.randint(1,4)
                        if newpos != change[0][0]:
                            aiguess[newpos] = change[0][1]
                            go = True
                    
        count2 = 0
        change = []
        go = False
        rw = playeraffirmation(aiguess)
        count += 1