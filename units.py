#This module includes all units

class Worker:
    """ A worker, can work in different places for resources"""
    def __init__(self, condition, task):
        self.condition = condition
        self.task = task
        self.workspace = 0

    def __str__(self):
        return str(self.task)

    def assignTask(self, task):
        pass

    def isFree(self):
        if self.task == '' or self.task == 'None':
            return True
        else:
            return False