# This module includes all units
# http://stackoverflow.com/questions/6760685/creating-a-singleton-in-python

class Units:
    """ Start program with this class initialized, it keeps track of all units that exist"""
    def __init__(self):
        self = self
        workers = []

    def getInstance(empty_self):
        return None

# --- --- Units --- ---
# Contains lists with references to certain unit groups
workers = []



class Worker:
    """ A worker, can work in different places for resources"""
    def __init__(self, condition, task):
        self.condition = condition
        self.task = task
        self.workspace = 0
        workers.append(self)


    def __str__(self):
        return str(self.task)

    def assignTask(self, task):
        pass

    def isFree(self):
        if self.task == '' or self.task == 'None':
            return True
        else:
            return False

    def destroy(self):
        for worker in workers:
            if