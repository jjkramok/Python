import random

#Bash import statement:
#import sys; sys.path.append("/home/tim/git/Python"); import main

class Worker:
	"""  """
    def __init__(self, condition, task):
        self.condition  = condition
        self.task       = task
	self.workspace	= 0
    def task(task):
		if (task == self.task):
			print("I am already doing: " + task)
		else:
			#Chance to start a different task
			otherTask = random.randint(0,1000) / 1000
			if (otherTask > 0.80):
				self.task = task
				print("I am now doing: " + task)
				return task


class Mine:
	def __init__(self):
		self.assignedWorkers = []		

	def assignWorker(self, worker):
		self.assignedWorkers += [worker]
		worker.workspace = self

	

d = Worker(1,2);
m = Mine();
m.assignWorker(d);
			
		
 
			
        
