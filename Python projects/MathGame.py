# -*- coding: utf-8 -*-
"""
Created on Sat May  2 15:53:59 2020

@author: Daniel DeMaria
"""

import tkinter
import random

class Globals:
    bignumber = None
    smallnumber = None
    answer = None
    
    gameWindow = None
    topFrame = None
    
    button1 = None
    label1 = None
    statusLabel = None
    wrongGuessLabel = None
    newProblemButton = None
    quitButton = None
    
    incorrectAnswers = 0
    wrongAnswersTotal = 0
    questionList = []
    attempted = 0
    solved = 0
    averageWrongAnswers = 0

    
def initializeGame():
    getQuestion()
    
    question = [Globals.bignumber, Globals.sign, Globals.smallnumber]
    while question in Globals.questionList:
        getQuestion()
        question = [Globals.bignumber, Globals.sign, Globals.smallnumber]
        
    Globals.questionList.append(question)
    Globals.attempted += 1
    

def getQuestion():    
    equation = random.choice(["subtraction", "addition", "multiplication", "division"])
        
    if equation == "subtraction":
        Globals.sign = "-"
        Globals.bignumber = random.randint(1,1000)
        Globals.smallnumber = random.randint(1,Globals.bignumber)
        Globals.answer = Globals.bignumber - Globals.smallnumber
    if equation == "addition":
        Globals.sign = "+"
        Globals.bignumber = random.randint(1,1000)
        Globals.smallnumber = random.randint(1,1000)
        Globals.answer = Globals.bignumber + Globals.smallnumber
    if equation ==  "multiplication":
        Globals.sign = "x"
        Globals.bignumber = random.randint(1,100)
        Globals.smallnumber = random.randint(1,100)
        Globals.answer = Globals.bignumber * Globals.smallnumber
    if equation == "division":
        Globals.sign = "/"
        Globals.smallnumber = random.randint(1,100)
        Globals.bignumber = random.randint(1,Globals.smallnumber) * Globals.smallnumber
        while Globals.bignumber > 1000:
            Globals.bignumber = random.randint(1,Globals.smallnumber) * Globals.smallnumber
        Globals.answer = Globals.bignumber / Globals.smallnumber

def newGame():
    forgetButtons()
    initializeGame()
    buttons()
    
def newProblem():
    Globals.wrongAnswersTotal += Globals.incorrectAnswers
    
    forgetButtons()
    initializeGame()
    buttons()
    

def checkGuess(guess):    
    if guess == Globals.answer:
        Globals.label1.destroy()
        guessEntry.destroy()
        Globals.newProblemButton.destroy()
        Globals.statusLabel.configure(text = str(guess) + " is it - you win!")
        Globals.button1.configure(text = "New game", command = newGame)
        Globals.solved += 1
        Globals.wrongAnswersTotal += Globals.incorrectAnswers
    else:
        Globals.statusLabel.configure(text = str(guess) + " is not correct. Try again.")
        Globals.incorrectAnswers += 1
        guessEntry.delete(0, tkinter.END)

    Globals.wrongGuessLabel = tkinter.Label(Globals.gameWindow, text = "Total Wrong Guesses: {}".format(Globals.incorrectAnswers))
    Globals.wrongGuessLabel.pack()

def dataValid():
    global guessEntry
    Globals.wrongGuessLabel.destroy()
    guessAsString = guessEntry.get()
    valid = True
    while valid == True:
        try:
            guess = int(guessAsString)
            valid = False
        except ValueError:
            Globals.statusLabel.configure(text="Please enter integers only! \n1 has been added to the wrong guess counter")
            Globals.incorrectAnswers += 1
            guessEntry.delete(0, tkinter.END)
            return

    checkGuess(guess)
    

def initializeGameWindow():    
    Globals.gameWindow = tkinter.Tk() 
    Globals.topFrame = tkinter.Frame(Globals.gameWindow)
    Globals.topFrame.pack()

def buttons():
    global guessEntry
    
    Globals.label1 = tkinter.Label(Globals.topFrame, text="{} {} {} =".format(Globals.bignumber, Globals.sign, Globals.smallnumber))
    Globals.label1.pack(side=tkinter.LEFT)
    guessEntry = tkinter.Entry(Globals.topFrame)
    guessEntry.pack(side=tkinter.LEFT)
    Globals.button1 = tkinter.Button(Globals.topFrame, text="Check It!", command=dataValid)
    Globals.button1.pack()

    Globals.statusLabel = tkinter.Label(Globals.gameWindow, text="You haven't made any guesses yet")
    Globals.statusLabel.pack()
    
    Globals.wrongGuessLabel = tkinter.Label(Globals.gameWindow, text = "Total Wrong Guesses: {}".format(Globals.incorrectAnswers))
    Globals.wrongGuessLabel.pack()
    
    Globals.newProblemButton = tkinter.Button(Globals.topFrame, text="New Problem", command=newProblem)
    Globals.newProblemButton.pack()
    
    Globals.quitButton = tkinter.Button(Globals.topFrame, text="Quit Game", command=quitGame)
    Globals.quitButton.pack()

def forgetButtons():
    global guessEntry
    
    Globals.incorrectAnswers = 0
    guessEntry.destroy()
    Globals.label1.destroy()
    Globals.button1.destroy()
    Globals.statusLabel.destroy()
    Globals.wrongGuessLabel.destroy()
    Globals.newProblemButton.destroy()
    Globals.quitButton.destroy()

def quitGame():
    Globals.averageWrongAnswers = Globals.wrongAnswersTotal / Globals.attempted
    
    print("Number of problems attempted: {}".format(Globals.attempted))
    print("Number of problems solved: {}".format(Globals.solved))
    print("Average number of incorrect answers per problem: {}".format(Globals.averageWrongAnswers))
    
    Globals.gameWindow.destroy()

def startmathGameGUI():
    Globals.incorrectAnswers = 0
    Globals.wrongAnswersTotal = 0
    Globals.questionList = []
    Globals.attempted = 0
    Globals.solved = 0
    Globals.averageWrongAnswers = 0
    initializeGame()
    initializeGameWindow()
    buttons()
    Globals.gameWindow.mainloop()    
    
startmathGameGUI()
