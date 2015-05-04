import random
from Tkinter import *

# --< Bash import statement: >--
#import sys; sys.path.append("/home/tim/git/Python"); import main

root = Tk()
list = 'Carl Patric Lindsay Helmut Chris Gwen'.split()
listb = Listbox(root)
for item in list:
    listb.insert(0, item)



class Worker:
    """  """
    def __init__(self, condition, task):
        self.condition = condition
        self.task = task
        self.workspace = 0

    def __str__(self):
        return str(self.task)

    def assignTask(self, task):
        pass


class Mine:
    """  """
    def __init__(self):
        self.assignedWorkers = []

    def assignWorker(self, worker):
        self.assignedWorkers += [worker]
        worker.workspace = self
        worker.task = 'mining'


d = Worker(1, 2);
m = Mine();
m.assignWorker(d);
for worker in m.assignedWorkers:
    print(worker)

def guiLoop(integer):
    int = integer + 1
    print 'Potje vet?: ' + str(int)
    root.after(200, guiLoop(int))


def Pressed():
    d.assignTask('mining')
    print 'Assigned Worker to' + ' ' + str(d.task)


button = Button(root, text='Assign current to mines', command = Pressed)
entry = Entry(root)

button.pack(pady=20, padx=20)
listb.pack()
entry.pack()

root.after(200, guiLoop(10))
root.mainloop()