# All locations/occupations that a worker can inhabit


class Location:
    """ """
    def __init__(self):
        pass






class Mine(Location):
    """ A place were workers mine stone and other minerals """
    def __init__(self):
        super(Mine, self).__init__()
        self.assignedWorkers = []

    def assignWorker(self, worker):
        self.assignedWorkers += [worker]
        worker.workspace = self
        worker.task = 'mining'


class Forest(Location):
    """ """
    def __init__(self, regrowth, size):
        super(Forest, self).__init__()
        self.regrowth = regrowth
        self.size = size

    #TODO asigned wordkers