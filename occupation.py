# All locations/occupations that a worker can inhabit
import _thread


# TODO This current structure is not desired, instead make one class Occupation (now a stub)
# TODO that handles all current occupations

# Stub location class
class Occupation:
    """ """
    def __init__(self):
        self.assignedWorkers = []


    def assignWorker(self, worker):
        pass


class Mine(Occupation):
    """ A place were workers mine stone and other minerals """
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
    """ A zero occupation, the unit is not doing anything useful """
    def __init__(self):
        super(Free).__init__(self)

    def assignWorker(self, worker):
        if not worker.isFree():
            self.assignedWorkers += [worker]
            worker.workspace = self
            worker.task = 'free'