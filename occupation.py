# All locations/occupations that a worker can inhabit

from main import resourcePool
from main import getPool

# TODO This current structure is not desired, instead make one class Occupation (now a stub)
# TODO that handles all current occupations


# Dictionary of all initialized Occupation (types)
occupationDict = {}

# Stub location class
class Occupation:
    """ type of occupation, regrowth rate and size of the occupation, taskName is the name of the task bound to the type of the Occupation

    """
    def __init__(self, type, taskName, resource, regrowth, size, efficiency):
        self.assignedWorkers = []
        self.type = type
        self.size = size
        self.efficiency = efficiency
        self.resource = resource
        self.regrowth = regrowth
        self.taskName = taskName
        occupationDict.update({type: self})

    def assignWorker(self, worker):
        if type == 'Free':
            if not worker.isFree():
                self.assignedWorkers += [worker]
                worker.workspace = self
                worker.task = self.taskName
        else:
            if worker.isFree():
                self.assignedWorkers += [worker]
                worker.workspace = self
                worker.task = self.taskName

    # used in main#economyLoop, adding the result of generateProduce to the resource pool
    def harvest(self):
        pool = getPool()
        harvest = self.generateProduce() + pool.get(type)
        pool.update({type: harvest})
        return pool

    # used to calculated the amount of resources this Occupation generated this step
    def generateProduce(self):
        produce = self.efficiency * len(self.assignedWorkers)
        if produce > self.size:
            produce = self.size
            print('our' + ' ' + str(type) + ' ' + 'is empty!')
        return produce

    # used to calculate the new size of the Occupation
    def grow(self):
        self.size += self.regrowth




# idea: for the Mine, in time the tunnels will go deeper into the earth, getting access to new minerals, that are not visible in the resource pool, until mined for the first time.

# ------------------------------- Deprecated
"""
class Mine(Occupation):
    ''' A place were workers mine stone and other minerals '''
    def __init__(self, size):
        super(Mine).__init__()
        self.size = size

    def assignWorker(self, worker):
        if worker.isFree():
            self.assignedWorkers += [worker]
            worker.workspace = self
            worker.task = 'mining'


class Woods(Occupation):
    """ """
    def __init__(self, regrowth, size):
        super(Woods).__init__()
        self.regrowth = regrowth
        self.size = size

    def assignWorker(self, worker):
        if worker.isFree():
            self.assignedWorkers += [worker]
            worker.workspace = self
            worker.task = 'woodcutting'


class Farm(Occupation):
    """ """
    def __init__(self, regrowth, size):
        super(Farm).__init__()
        self.regrowth = regrowth
        self.size = size

    def assignWorker(self, worker):
        if worker.isFree():
            self.assignedWorkers += [worker]
            worker.workspace = self
            worker.task = 'farmer'


class Free(Occupation):
    ''' A zero occupation, the unit is not doing anything useful '''
    def __init__(self):
        super(Free).__init__(self)

    def assignWorker(self, worker):
        if not worker.isFree():
            self.assignedWorkers += [worker]
            worker.workspace = self
            worker.task = 'free'
"""