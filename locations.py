# All locations/occupations that a worker can inhabit

class Mine:
    """  """
    def __init__(self):
        self.assignedWorkers = []

    def assignWorker(self, worker):
        self.assignedWorkers += [worker]
        worker.workspace = self
        worker.task = 'mining'