class Processor:
    jobsLoaded = 0       # Stores the total time of the jobs loaded in the list.
    jobsGap    = 0       # stores the time span between the first and last job loaded in the list.
    jobsSet    = []      # Stores jobs
    
    def __init__(self):
        self.jobsLoaded = 0
        self.jobsGap    = 0
        self.jobsSet    = []
    
    def jobAdd(self, jobTime):
        self.jobsLoaded+=jobTime               # total
        self.jobsSet.append(jobTime)           # add item in the list
        self.jobsGap = self.jobsSet[0]-jobTime # gap



    
