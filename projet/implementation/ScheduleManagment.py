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
        m = self.jobsSet[:]  # add item in the list
        m.append(jobTime)    # self.jobsSet.append(jobTime)        
        self.jobsSet = m[:]  # ---------------------
        #
        self.getTotal()      # total <=> self.jobsLoaded+=jobTime
        self.getGap()        # gap for slack <=> self.jobsSet[0]-jobTime

    def getGap(self):
        self.jobsGap = max(self.jobsSet)-min(self.jobsSet)
        return self.jobsGap

    def getTotal(self):
        self.jobsTotal = sum(self.jobsSet)
        return self.jobsTotal

    def getJobsSetSize(self):
        return len(self.jobsSet)

    def getJobTime(self, k):
        return self.jobsSet[k]
    
    def razJobsSet(self):
        self.jobsTotal  = 0.0
        self.jobsGap    = 0.0
        self.jobsSet    = []

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
        self.getTotal()
        self.getGap()
        
    def getTotal(self):
        total = 0.0
        for i in range(len(self.tupl)):
            total+= sum(self.tupl[i].jobsSet)
        # END FOR
        self.tuplTotal = total
        #
        return self.tuplTotal
        
    def getGap(self):
        minmax = []
        gap = 0.0
        for i in range(len(self.tupl)):
            minmax.append(sum(self.tupl[i].jobsSet))
        # END FOR
        gap = max(minmax) - min(minmax)
        #
        self.tuplGap = gap
        #
        return self.tuplGap
    
    def smaler(self):
        """
        return the index in the list tupl so the processor has the smallest sum.
        in the case of a tie, the index of the furthest right.
        """
        res = 0
        smalValue = None
        for k in range(len(self.tupl)):
            value = self.getProcessor(k).getTotal()
            if smalValue==None:
                smalValue = value
                res = k
            else:
                if value <= smalValue:
                    smalValue = value
                    res = k
                # END IF
            # END IF
        # END FOR
        return res

    def largest(self):
        """
        return the index in the list tupl so the processor has the largest sum.
        in the case of a tie, the index of the furthest right.
        """
        res = 0
        largValue = 0
        for k in range(len(self.tupl)):
            value = self.getProcessor(k).getTotal()
            if value >= largValue:
                largValue = value
                res = k
            # END IF
        # END FOR
        return res

    def getProcessor(self, m):
        return self.tupl[m]
    

# ########################################################################
#
#                               ldmPartition
#
# list of ldmTuple
# ########################################################################
class ldmPartition():
    part = [] # list of ldmTuple
    m    = 0

    # =============================================
    # CONSTRUCTOR
    # =============================================
    def __init__(self, times, m):
        """
        Store in self.part (list) n ldmTuple
        each ldmTuple is an Object with tuplTotal tuplGap computed and ldmTuple.tupl (list ) filled with m Processors
        part ==> ldmTuple1                   - ldmTuple2 - ... - ldmTuple1n
                 -------------------           ---------         -------------------
                 ldmTuple1.tuplTotal           ...               ldmTuplen.tuplTotal
                 ldmTuple1.tuplGap             ...               ldmTuplen.tuplGap
                 ldmTuple1.tupl                                  ldmTuplen.tupl
                            ---------------                                ---------------
                            tupl.Processor1                                tupl.Processor1
                            tupl.Processor2                                tupl.Processor2
                            ...                                            ...
                            tupl.Processorm                                tupl.Processorm
        """
        self.m = m
        self.part = []
        n = len(times)
        # create part (list) of n ldmTuple (lists) of m Processor
        for i in range(n):
            t = ldmTuple(m)
            t.initialize(times[i])
            self.part.append(t)

    # =============================================
    # getPartSize
    # =============================================
    def getPartSize(self):
        return len(self.part)

    # =============================================
    # getSched
    # =============================================
    def getSched(self):
        if len(self.part) == 1:
            l = self.part[0].tupl[:]
            return l
        else:
            return []
        # END IF

    # =============================================
    # partSortBytuplGapDec
    # =============================================
    def partSortBytuplGapDec(self):
        """
        Sort part by non increasing part. ldmTupleX.tuplGap
        so as to obtain the m-tuples that have the largest difference (ldmTupleX.tuplGap) first.
        """
        self.part.sort(key=attrgetter("tuplGap"), reverse=True)

    # =============================================
    # partPrint
    # =============================================
    def partPrint(self):
        """
        Just for debug or verify result
        Print the part state represented by
        ldmTuple1 [][][][][]
        ldmTuple2 [][][][][]
        ...
        ldmTuplen [][][][][]
        each [] is the jobsSet of Processor objext
        """
        print("")
        print("partition size :",len(self.part))
        for i in range(len(self.part)):
            print("")
            for j in range(len(self.part[i].tupl)):
                print(self.part[i].tupl[j].jobsSet, end = " ")
    # =============================================
    # partMerge
    # =============================================
    def partMerge(self, tupl1Indice, tupl2Indice):
        """
        of two m-tuples, only one remains, by combining 
        the processor with the smaller sum of one with the larger sum of the other, and so on.
        e.g
        
        ldmTuple1 [3,3][4][4] gap=2 : (3+3) - 4
        ldmTuple2 [][][][1]   gap=1 : 1-0
        ...
        ldmTuplen [][][][][]
        result
        ldmTuple1 [3,3][4,1][4] gap=2 (3+3) - 4
        ldmTuple1 [][][][1] --> deleted
        ...
        ldmTuplen [][][][][]
        
        """
        ldmTuple1 = self.part[tupl1Indice] 
        ldmTuple2 = self.part[tupl2Indice] 
        
        for m in range(self.m):
            
            # LARGEST : index in the ldmTuple2 so the processor has the largest sum.
            largest = ldmTuple2.largest()
            # SMALEST : ndex in the ldmTuple1 so the processor has the smallest sum.
            smaller = ldmTuple1.smaler()

            for k in range(ldmTuple2.getProcessor(largest).getJobsSetSize()):
                ldmTuple1.getProcessor(smaller).addJob(ldmTuple2.getProcessor(largest).getJobTime(k))
            # END FOR
            ldmTuple2.getProcessor(largest).razJobsSet()
        
            ldmTuple1.getGap()
            ldmTuple1.getTotal()
            
        # END FOR
        
        self.part.pop(tupl2Indice)
        

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
        


    
