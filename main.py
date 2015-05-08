from tkinter import *
from _thread import *
from units import *
from occupation import *
from time import sleep

# --< Bash import statement: >--
#import sys; sys.path.append("/home/tim/git/Python"); import main


# --- initializing view --- #
root = Tk()


# --- initializing stuff --- #
resourcePool = {'wood': 0, 'food': 0, 'stone': 0}
farm = Occupation('Farm', 'farming', 'food', 3.0, 100, 1)
mine = Occupation('Mine', 'mining', 'stone', 0, 123456, 0.9)
forest = Occupation('Farm', 'farming', 'food', 3.0, 100, 1)

# --- Getters --- #
def getPool():
    return resourcePool

"""
listb = Listbox(root)
for item in list:
    listb.insert(0, item)
"""


def economy():
    while(True):
        sleep(1)
        for occupation in occupationDict:
            occupation.harvest()


def Pressed():
    #tkSimpleDialog.askstring('Occupation', 'From: \'mining\'')
    d.assignTask('mining')
    print('Assigned Worker to' + ' ' + str(d.task))

def threadLoop():

    while(True):
        print('bla')
        sleep(0.5)


button = Button(root, text='Assign current to mines', command = Pressed)
entry = Entry(root)

button.pack(pady=20, padx=20)
entry.pack()

econ_thread = start_new_thread(economy, tuple([]))
thread = start_new_thread(threadLoop, tuple([]))
root.mainloop()
