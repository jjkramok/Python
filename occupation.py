# All locations/occupations that a worker can inhabit

# Dictionary of all initialized Occupation (types)
occupationDict = {}

# Stub location class
class Occupation(object):
    """ Occupation is where a worker can work and generate produce
        type: Which kind of Occupation this is. First letter is upper-case Ex. Farm, Mine
        taskName: The action name of the Occupation#type, entirely lower-case Ex. farming, mining
        resource: The type of resource this Occupation yields, entirely lower-case Ex. food, stone
        regrowth: The rate at which the Occupation#size grows in time, in units per unit
        size: Initial size of the Occupation, if the size is 0, there are no resources left to gather
        efficiency: How easy/hard it is to extract produce from this type of Occupation, in resourceUnits per step (per worker)
    """
    def __init__(self, resourcePool, type, taskName, resource, regrowth, size, efficiency):
        self.assignedWorkers = []
        self.type = type
        self.size = size
        self.efficiency = efficiency
        self.resource = resource
        self.regrowth = regrowth
        self.taskName = taskName
        self.pool = resourcePool
        occupationDict.update({self.type: self})

    def assignWorker(self, worker):
        if type == 'Free':  # TODO If statement not really needed
            if not worker.isFree():
                self.assignedWorkers += [worker]
                worker.workspace = self
                worker.task = self.taskName
        else:
            if worker.isFree():
                print("Worker is free!")
                self.assignedWorkers += [worker]
                worker.workspace = self
                worker.task = self.taskName

    # used in main#economyLoop, adding the result of generateProduce to the resource pool, beware multithreading?
    def harvest(self):
        print("Harvesting you souls!: " + str(self.pool.get(self.type)))
        if self.pool.get(self.type) is not None:
            harvest = self.generateProduce() + self.pool.get(self.type)
            self.pool.update({self.resource: harvest})
            #return pool

    # used to calculated the amount of resources this Occupation generated this step
    def generateProduce(self):
        produce = self.efficiency * len(self.assignedWorkers)
        print(type + ' size is: ' + str(self.size))
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