import time
from operator import attrgetter

# ########################################################################
#
#                               Processor
#
# part of schedule (Processor = machine)
# ########################################################################
class Processor:
    jobsTotal  = 0.0     # Stores the total time of the jobs loaded in the list.
    jobsGap    = 0.0     # stores the time span between the first and last job loaded in the list.
    jobsSet    = []      # Stores jobs

    def __init__(self):
        self.jobsTotal  = 0.0
        self.jobsGap    = 0.0
        self.jobsSet    = []
    
    def addJob(self, jobTime):
        m = self.jobsSet[:]                 # add item in the list
        m.append(jobTime)                   # self.jobsSet.append(jobTime)        
        self.jobsSet = m[:]                 # ---------------------
        #
        self.jobsTotal = self.getTotal()    # total <=> self.jobsLoaded+=jobTime
        self.jobsGap = self.getGap()        # gap for slack <=> self.jobsSet[0]-jobTime

    def getGap(self):
        return max(self.jobsSet)-min(self.jobsSet)

    def getTotal(self):
        return sum(self.jobsSet)
    

# ########################################################################
#
#                               ldmTuple
#
# list of pocessors
# ########################################################################
class ldmTuple:
    tupl          = []
    m             = 0
    tuplTotal     = 0.0
    tuplGap       = 0.0
    # =============================================
    # CONSTRUCTOR
    # =============================================
    def __init__(self, m):
        """        
        like ldm rule, Create a m-tuple with empty items
        e.g m = 5 [[],[],[],[],[]]
        each item is a Processor object
        """
        self.m          = m
        self.tuplTotal  = 0.0
        self.tuplGap    = 0.0
        self.tupl       = [] # list of m Processor
        for i in range(m):
            p = Processor()
            self.tupl.append(p)

    # =============================================
    # initialization of ldm tuple
    # =============================================
    def initialize(self, value):
        """
        like LDM rule, affect the value to the last item of the ldmTuple
        """
        self.tupl[self.m - 1].addJob(value)
        self.tuplTotal = self.getTotal()
        self.tuplGap   = self.getGap()
        
    def getTotal(self):
        total = 0.0
        for i in range(len(self.tupl)):
            total+= sum(self.tupl[i].jobsSet)
        # END FOR
        return total
        
    def getGap(self):
        minmax = []
        gap = 0.0
        for i in range(len(self.tupl)):
            minmax.append(sum(self.tupl[i].jobsSet))
        # END FOR
        gap = max(minmax) - min(minmax)
        return gap

# ########################################################################
#
#                               ldmPartition
#
# list of ldmTuple
# ########################################################################
class ldmPartition():
    part = [] # list of ldmTuple
    m    = 0

    def __init__(self, times, m):
        self.m = m
        self.part = []
        n = len(times)
        
        # create part (list) of n ldmTuple (lists) of m Processor
        for i in range(n):
            t = ldmTuple(m)
            t.initialize(times[i])
            self.part.append(t)
        # DEBUG
        self.printPart()
        
    def printPart(self):
        print("partition",len(self.part))
        
        for i in range(len(self.part)):
            print("")
            for j in range(len(self.part[i].tupl)):
                print(self.part[i].tupl[j].jobsSet, end = " ")

    def fusion(self, tupl1Indice, tupl2Indice):
        
        tuple1 = self.part[tuple1Indice] #, key=attrgetter("tuplTotal")))
        tuple2 = self.part[tuple2Indice] #, key=attrgetter("tuplTotal"), reverse = True)
     
# DEBUG            
#h = ldmPartition([1,2,3,4,5,6,7,8],5)



# ########################################################################
#
#                               PSched
#
# Structure to store a scheduling result
# ########################################################################
class PSched:
    algoName     = ""
    timeExpected = 0.0
    makespan     = 0.0
    time         = 0.0
    sched        = []

    def __init__(self, algoName, timeExpected, makespan, time, sched):
        self.algoName     = algoName 
        self.timeExpected = timeExpected 
        self.makespan     = makespan 
        self.time         = time 
        self.sched        = sched
        
    def __str__(self):
        return ""

    def getAlgoName(self):
        return self.algoName
    
    def getTimeExpected(self):
        return self.timeExpected
    
    def getMakespan(self):
        return self.makespan

    def getTime(self):
        return self.time
    
    def getSched(self):
        return self.sched
    
    def getResult(self):
        return (self.algoName, self.timeExpected, self.makespan, self.time)

# rec = lambda x: sum(map(rec, x)) if isinstance(x, list) else x
        


    
