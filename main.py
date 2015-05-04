from tkinter import *
from _thread import *
from units import *
from locations import *
from time import sleep

# --< Bash import statement: >--
#import sys; sys.path.append("/home/tim/git/Python"); import main


#initializing view
root = Tk()

"""
listb = Listbox(root)
for item in list:
    listb.insert(0, item)
"""

d = Worker(1, 2);
m = Mine();
m.assignWorker(d);
for worker in m.assignedWorkers:
    print(worker)


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


thread = start_new_thread(threadLoop, tuple([]))
root.mainloop()
