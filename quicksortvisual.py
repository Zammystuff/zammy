import tkinter as tk
import numpy as num
from numpy import *
from tkinter import *
from tkinter import ttk
from numpy.random import rand

randomArray = [num.random.randint(1,100,100)]
safeArray = []

win = Tk()
win.resizable(True,True)
canvas=Canvas(win,width=500,height=500)
canvas.pack()
r = 1

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low,high):
        if array[j] <= pivot:
            i = i +1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1
    


def quicksort(array,low,high):
    if low < high:
        pi = partition(array,low,high)
        quicksort(array,low,pi - 1)
        quicksort(array,pi + 1,high)
        return []
def drawLineUnsorted():
    for j in range(len(safeArray)):
        x1pos = j
        y1pos = 500 
        x2pos = x1pos
        y2pos = j
        canvas.create_line(x1pos,y1pos,x2pos,y2pos)




size = len(randomArray)

quicksort(randomArray, 0 , size - 1)
print(randomArray)


print ('Sorted array in Ascending Order')








##Control Tkinter window Start - 







##Control Tkinter Window End
    
def drawLineSorted():
    for i in range(len(randomArray)):

        x1pos = i
        y1pos = 300
        x2pos = i
        y2pos = randomArray[i] + 100
        i+=1
        print(i)
        
        ##canvas.create_line(x1pos,y1pos,x2pos,y2pos)
        print("this function is running")
        
        



 


drawLineSorted()

drawLineUnsorted()


win.mainloop()








