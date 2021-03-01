class Processor:
    jobsLoaded = 0
    jobsSet    = []
    
    def __init__(self):
        self.jobsLoaded = 0
        self.jobsSet    = []
    
    def jobAdd(self, jobTime):
        self.jobsLoaded+=jobTime
        self.jobsSet.append(jobTime)



    
