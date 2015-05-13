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
farm = Occupation(resourcePool, 'Farm', 'farming', 'food', 0.1, 100, 3)
mine = Occupation(resourcePool, 'Mine', 'mining', 'stone', 0, 123456, 0.8)
forest = Occupation(resourcePool, 'Forest', 'woodcutting', 'wood', 0.05, 100, 1)
free = Occupation(resourcePool, 'Free', 'free', None, None, None, None)
dwarf = Worker('healty')
forest.assignWorker(dwarf)


# --- Getters --- #
def get_pool():
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
            occupationDict[occupation].harvest()
        print(str(resourcePool))


def Pressed():
    #tkSimpleDialog.askstring('Occupation', 'From: \'mining\'')
    print('Assigned Worker to' + ' !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    root.after(500, Pressed)

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
#root.after(100, Pressed())
root.mainloop()
