# -*- coding: utf-8 -*-

"""
Interactive NimGame 

How to play:
    
The game starts with one or more "heaps" of one or more items (we'll call them balls).
Players take turns removing one or more balls from any heap. 
The player who removes the last ball wins.

"""
import random

Status = 0
Game = None
Ballcountlist = []
Heaps = None
Heapslist = []


def message():
    global Ballcountlist
    global Heaps
    
    num = 0
    outputString = "Nim game with {} heaps.\n".format(Heaps)
    for item in Ballcountlist:
        newString = "\t\tHeap {}: {} balls\n".format(num, Ballcountlist[num])
        outputString = outputString + newString
        num += 1

    print(outputString)
    

def remove(Balls, Heap_pick):
    global Status
    global Ballcountlist
    global Heaps
    global Heapslist 
    
    
    if Balls >= 0:
            
        Total = 0
        num1 = 0
        for item in Ballcountlist:
            Total += Ballcountlist[num1]
            num1 += 1
        
        while Total > 0:
            if Balls <= Ballcountlist[Heap_pick]:
                Ballcountlist[Heap_pick] = Ballcountlist[Heap_pick] - Balls
                Total = Total - Balls
                    
                if Total > 0:
                    update = "You took {} balls from Heap {}.\n".format(Balls, Heap_pick)
                            
                    heapChoice = random.randrange(len(Ballcountlist))
                    while Ballcountlist[heapChoice] == 0:
                        heapChoice = random.randrange(len(Ballcountlist))
                    upperLimit = Ballcountlist[heapChoice]+1
                    ballChoice = random.randrange(1, upperLimit)
                    Ballcountlist[heapChoice] = Ballcountlist[heapChoice] - ballChoice
                    Total = Total - ballChoice
                    
                    if Total > 0:
                        print (update + "The computer took {} balls from Heap {}.".format(ballChoice, heapChoice))
                        message()
                        break
                    if Total == 0:
                        print (update + "Computer took {} balls from Heap {}. \nComputer Wins!".format(ballChoice, heapChoice))
                        Status = 1
                        break
                  
                if Total == 0:
                    print ("You took {} balls from Heap {}.\nYou Win!".format(Balls, Heap_pick))
                    Status = 1
                    break
            else:
                return "You can't take that many balls from heap {}. Try again.".format(Heap_pick)  
    else:
        return "You can't take a negative amount of Balls from heap {}. Try again.".format(Heap_pick)  
    


def main():
    global Status
    global Ballcountlist
    global Heaps

    
    Heaps = int(input('Enter the number of Heaps: '))
    while Heaps <= 0:
        Heaps = int(input('That is not a valid choice! \nEnter the number of Heaps: '))
    count = Heaps
    Ballcountlist = []
    for i in range(Heaps):
        Ballcount = int(input('Enter the number of Balls in Heap {}: '.format(Heaps - count)))
        while Ballcount <= 0:
            Ballcount = int(input('That is not a valid choice! \nEnter the number of Balls in Heap {}: '.format(Heaps - count)))
            
        count = count - 1
        Ballcountlist.append(Ballcount)
        
    print("Nim game initialized with {} heaps.".format(Heaps))
    
    message()
    
    while Status == 0:
        Heap_pick = int(input('Pick a heap: '))
        while Heap_pick > (Heaps - 1) or Heap_pick < 0:
            Heap_pick = int(input('That is not a valid choice! \nPick a heap: '))
            
        Ball_pick = int(input('Pick amount of balls: '))
        while Ball_pick > Ballcountlist[Heap_pick]:
             Ball_pick = int(input('You cant take that many balls! \nPick amount of balls: '))
        while Ball_pick < 0:
             Ball_pick = int(input('You cant take negative balls! \nPick amount of balls: '))
        remove(Ball_pick, Heap_pick)
        
        
  
    
    

main()
           