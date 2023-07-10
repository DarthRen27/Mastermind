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
            aicount2 += 1
        if correct == False:
            print("thame")
            affirmation += "NOTHING "
        correct == False
        aicount2 == 0
        aicount += 1
    return affirmation
        

colors = "RED", "BLUE", "YELLOW", "ORANGE", "PURPLE", "BROWN", "PINK", "NOTHING"
guess = []
aiguess = []
count = 0
count2 = 0
newguess = 0
change = 0
reduced = False

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
        
else:
    plan = player()
    aiguess = aiselection(colors)
    print("The AI guesses " + aiguess + ". Please affirm")
    rw = playeraffirmation(aiguess)
    while count < 9:
        while count2 < 4:
            if rw[count2] == "BLACK":
                pass
            elif rw[count2] == "WHITE":
                change = count2
            else:
                newguess = random.randint(0,7)
                aiguess[count2] = colors[newguess]
                pass
            count2 += 1
        count2 = 0
        rw = playeraffirmation(aiguess)
        count += 1