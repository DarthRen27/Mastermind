# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 18:23:44 2022

@author: Justin
"""

import random

def aiselection(colors):
    #Have the AI fill out it's plan
    aicount = 0
    selection = []
    while aicount < 4:
        grab = random.randint(0,7)
        if colors[grab] not in selection:
            selection.append(colors[grab])
            aicount += 1
    return selection

def player(ai):
    #Acquire the player's guess or plan
    choice = []
    playcount = 0
    if ai == "Yes":
        while playcount < 4:
            color = input("Enter the color you want at position " + str(playcount) + ". Options are RED, BLUE, YELLOW, ORANGE, PURPLE, BROWN, PINK, NOTHING: ")
            choice.append(color.upper())
            playcount += 1
    else:
        while playcount < 4:
            color = input("Enter the color you think is at position " + str(playcount) + ". Options are RED, BLUE, YELLOW, ORANGE, PURPLE, BROWN, PINK, NOTHING: ")
            choice.append(color.upper())
            playcount += 1
    return choice

def playeraffirmation():
    #Have the player confirm the AI's guess
    correction = ""
    verdict = []
    playcount = 0
    while playcount < 4:
        correction = input("If position " + str(playcount) + " is the correct color and is in the correct space enter BLACK, if it is the correct color but in the wrong space enter WHITE, if it is not the correct color or space enter NOTHING: ")
        verdict.append(correction.upper())
        playcount += 1
    return verdict
    
def aiaffirmation(plan, check):
    #Look over player guess and see if it's right or not
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
possibles = ["RED", "BLUE", "YELLOW", "ORANGE", "PURPLE", "BROWN", "PINK", "NOTHING"]
guess = []
aiguess = []
count = 0
count2 = 0
change = []
noplace = []
correct = {}
oldpos = 0
newpos = 0
check = 0
aicheck = {}
go = False

ai = input("Do you want to be the mastermind? Yes or No: ")
dev = input("Do you want to check that everything is working: ")

if ai == "No":
    #If user wants to be guesser
    plan = aiselection(colors)
    if dev == "Yes":
        print(plan)
    while count < 10:
        out = ""
        check = player(ai)
        out = aiaffirmation(plan, check)
        print(out)
        if out == "BLACK BLACK BLACK BLACK ":
            print("That's correct, you win")
            count += 10
        count += 1
    if count == 10:
        print("You've lost, the plan was " + plan)
        
else:
    #Testing
    plan = player(ai)
    aiguess = aiselection(colors)
    print("The AI guesses " + aiguess[0] + ", " + aiguess[1] + ", " + aiguess[2] + ", " + aiguess[3] + ". Please affirm")
    while count < 9:
        rw = playeraffirmation()
        #Place the AI's guesses into appropriate places
        while count2 < 4:
            if rw[count2] == "BLACK":
                correct[count2] = aiguess[count2]
            elif rw[count2] == "WHITE":
                change.append((count2,aiguess[count2]))
            else:
                possibles.remove(aiguess[count2])
            count2 += 1
        if len(correct) == 4:
            print("You've lost, the AI guessed your plan")
        else:
            #Function this
            #Have the AI create new guess given information
            aiguess = ["", "", "", ""]
            if len(change) != 0:
                if len(change) > 1:
                    if len(correct) != 0:
                        while check < len(change):
                            oldpos = change[0][0]
                            noplace = list(correct.keys())
                            while go != True:
                                newpos = random.randint(0,3)
                                if newpos not in noplace:
                                    aiguess[newpos] = change[0][1]
                                    go = True
                    else:
                        while check < len(change):
                            oldpos = change[check][0]
                            newpos = random.randint(0,3)
                            if newpos != oldpos:
                                if aiguess[newpos] != "":
                                    aiguess[newpos] = change[check][1]
                                    check += 1
                else:
                    if len(correct) != 0:
                        oldpos = change[0][0]
                        noplace = list(correct.keys())
                        while go != True:
                            newpos = random.randint(0,3)
                            if newpos not in noplace:
                                aiguess[newpos] = change[0][1]
                                go = True
                    else:
                        while go != True:
                            newpos = random.randint(0,3)
                            if newpos != change[0][0]:
                                aiguess[newpos] = change[0][1]
                                go = True
        for a in noplace:
            #Place correct guesses back into AI guess
            b = correct[a]
            aiguess[a] = b
        for x in aiguess:
            if x == "":
                #Fill the blanks in the guess
                z = len(possibles) - 1
                y = random.randint(0, z)
                x = possibles[y]
        count2 = 0
        change = []
        go = False
        rw = playeraffirmation()
        count += 1