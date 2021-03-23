import time
import math
from operator import attrgetter
#
import matrix as cm
import ScheduleManagment as sm # Processor object


# #######################################################################
#                                                                       #
#                               LPT                                     #
#                                                                       #
# #######################################################################
def lpt(costMatrix, m):
    """
    Compute a schedule with LPT rule algorithm.
    Input
      costMatrix : matrix (1 dimension) conaining a set of n jobs cost time
      m          : number of machines
    Output
      tuple of 5 items:
        algoName     : name of algorithm
        timeExpected : the time expected computed with algorithm complexity
        makespan     : makesapn comuted
        time         : the time it took to calculate the makespan
        sched        : in the form of a Processor object list. Each "Processor" object represents the load of a machine, with the total time and a list of each job cost allocated to that processor.
    """
    
    print("Begin LPT Number of machines :",m)

    #------------------------------------------
    #
    #------------------------------------------
    algoName = "LPT"
    timeExpected = 0.0

    #------------------------------------------    
    # work with a copy of costMatrix
    # this matrix will be sorted or modified
    #------------------------------------------    
    matrixW = costMatrix[:] # tools.matrix1dCopy(costMatrix)

    #------------------------------------------    
    # sched is a list of Processor objects.
    #------------------------------------------    
    sched= [] 

    #------------------------------------------    
    # current time at the bégining
    #------------------------------------------    
    before = time.time()

    #==========================================    
    # LPT RULE 
    #==========================================    

    #------------------------------------------    
    # sort matrix by non - increasing costs
    #------------------------------------------    
    matrixW.sort(reverse=True)

    #==========================================    
    # Sched calculation
    #==========================================    
    for i in range(len(matrixW)):
        #------------------------------------------    
        # The maximum number of processors (or machines) is not reached.
        # One more processor is added for each iteration.
        #------------------------------------------    
        if (len(sched) < m):
            p = sm.Processor()
            p.addJob(matrixW[i])
            sched.append(p)
            
        else:
            #------------------------------------------    
            # The maximum number of processors (or machines) is reached.
            # Each cost is allocated to the least loaded
            # processor (machine) at this time.
            #------------------------------------------    
            sched.sort(key=attrgetter("jobsTotal"))
            sched[0].addJob(matrixW[i])
            

    #------------------------------------------            
    # current time at the bégining
    #------------------------------------------    
    after = time.time()

    #------------------------------------------            
    # Retrieve Makespan (most loaded machine)
    #------------------------------------------    
    makespan = 0
    for i in range(len(sched)):
        makespan = max(makespan, sched[i].jobsTotal)

    #------------------------------------------
    # RETURN Makespan obtained /
    #        Processing algorithm time /
    #        Schedul 
    #------------------------------------------
    timeAlgo = after-before
    res = sm.PSched(algoName, timeExpected, makespan, timeAlgo, sched)
    return res
    

# #######################################################################
#                                                                       #
#                               SLACK                                   #
#                                                                       #
# #######################################################################
def slack(costMatrix, m):
    """
    Compute a schedule with SLACK algorithm.
    Input
      costMatrix : matrix (1 dimension) conaining a set of n jobs cost time
      m          : number of machines
    Output
      tuple of 5 items:
        algoName     : name of algorithm
        timeExpected : the time expected computed with algorithm complexity
        makespan     : makesapn comuted
        time         : the time it took to calculate the makespan
        sched        : in the form of a Processor object list. Each "Processor" object represents the load of a machine, with the total time and a list of each job cost allocated to that processor.
    """
    print("Begin SLACK Number of machines :",m)
    
    #------------------------------------------
    #
    #------------------------------------------
    algoName = "SLACK"
    timeExpected = 0.0
    
    #------------------------------------------    
    # work with a copy of costMatrix
    # this matrix will be sorted or modified
    #------------------------------------------
    matrixW = costMatrix[:] # tools.matrix1dCopy(costMatrix)
    
    #------------------------------------------    
    # sched is a list of Processor objects.
    #------------------------------------------
    makespan = 0.0
    sched= []

    #------------------------------------------    
    # current time at the bégining
    #------------------------------------------    
    before = time.time()

    #==========================================    
    # GREEDY Approach
    #==========================================    

    #------------------------------------------    
    # SORT Jobs cost by non increasing costs
    #------------------------------------------    
    matrixW.sort(reverse=True)
    
    #------------------------------------------    
    # Cutting of the starting matrix in n/m under dies of size m each.
    # result is a list of Processors objects of m item each.
    # NB
    # We use the object Processor structure because the matrixWSlack will be sorted by non increasing jobsGap value
    #------------------------------------------
    # subsetSize = math.ceil(len(matrixW)/m) to keep command
    #------------------------------------------
    matrixGreedy = [] 

    itemNb = 0
    subsetNumbers = 0
    
    for i in range(len(matrixW)):
        #
        itemNb+=1
        # 
        if (itemNb > m):
            itemNb = 1
            subsetNumbers+=1
            
        # end if    
        if (itemNb == 1):
            p = sm.Processor()
            p.addJob(matrixW[i])
            matrixGreedy.append(p)
        else:
            matrixGreedy[subsetNumbers].addJob(matrixW[i])
        # end if
    #------------------------------------------    
    # SORT subsets by non increasing jobsGap value
    #------------------------------------------
    matrixGreedy.sort(key=attrgetter("jobsGap"), reverse=True)

    #------------------------------------------    
    # flattening the job list. (in matrixWSlack)
    #------------------------------------------
    matrixWSlack = []
    for i in range(len(matrixGreedy)):
        for j in range(len(matrixGreedy[i].jobsSet)):
            matrixWSlack.append(matrixGreedy[i].jobsSet[j])
        # end for
    # end for
    
    #==========================================    
    # COMPUTE PART (like LPT)
    # work with matrixWSlack
    #==========================================    
    for i in range(len(matrixWSlack)):
        #------------------------------------------    
        # The maximum number of processors (or machines) is not reached.
        # One more processor is added for each iteration.
        #------------------------------------------    
        if (len(sched) < m):
            p = sm.Processor()
            p.addJob(matrixWSlack[i])
            sched.append(p)
            
        else:
            #------------------------------------------    
            # The maximum number of processors (or machines) is reached.
            # Each cost is allocated to the least loaded
            # processor (machine) at this time.
            #------------------------------------------    
            sched.sort(key=attrgetter("jobsTotal"))
            sched[0].addJob(matrixWSlack[i])

    #------------------------------------------    
    # current time at the end
    #------------------------------------------    
    after  = time.time()

    #------------------------------------------            
    # Retrieve Makespan (most loaded machine)
    #------------------------------------------    
    makespan = 0
    for i in range(len(sched)):
        makespan = max(makespan, sched[i].jobsTotal)

    #------------------------------------------
    # RETURN Makespan obtained /
    #        Processing algorithm time /
    #        Schedul 
    #------------------------------------------
    timeAlgo = after-before
    res = sm.PSched(algoName, timeExpected, makespan, timeAlgo, sched)
    return res

# #######################################################################
#                                                                       #
#                               LDM                                     #
#                                                                       #
# !!!!!!!! Dont work : issue of lists addresses                         #
# #######################################################################
def ldm(costMatrix, m):
    print("Begin LDM Number of machines :",m)
    
    #------------------------------------------
    #
    #------------------------------------------
    algoName = "LDM"
    timeExpected = 0.0
    
    #------------------------------------------    
    # work with a copy of costMatrix
    # this matrix will be sorted or modified
    #------------------------------------------
    matrixW = costMatrix[:] # matrixW = tools.matrix1dCopy(costMatrix)
    
    #------------------------------------------    
    # sched is a list of Processor objects.
    #------------------------------------------
    makespan = 0.0
    sched= []

    #------------------------------------------    
    # current time at the bégining
    #------------------------------------------    
    before = time.time()

    #==========================================    
    # NUMBERS PARTITIONNING Approach
    #==========================================
    
    #------------------------------------------    
    # m-tuples (lists) creation
    #------------------------------------------
    partition = sm.ldmPartition(matrixW, m)
                   
    
##    for i in range(len(matrixW)):
##        partItem = sm.Processor()
##        for j in range(m-1):
##            # partItem.append(0)
##            partItem.addJob(0)
##        #END FOR
##        # partItem.append(matrixW[i])
##        partItem.addJob(matrixW[i])
##        print(partItem.jobsSet)
##        partition.append(partItem)
##    # END FOR
##    print(partition)
#ldm([1,2,5,8,7,9,10], 4)


# #######################################################################
#                                                                       #
#                               COMBINE                                 #
# need FFD algorithm                                                    #
# #######################################################################
def combine(costMatrix, m, alpha = 0.005):
    print("Begin COMBINE Number of machines :",m)
    algoName = "COMBINE"

    #------------------------------------------    
    # work with a copy of costMatrix
    # this matrix will be sorted or modified
    #------------------------------------------
    matrixW = costMatrix[:] # matrixW = tools.matrix1dCopy(costMatrix)
    matrixW.sort(reverse=True)
    
    #------------------------------------------    
    # sched is a list of Processor objects.
    #------------------------------------------
    makespan = 0.0
    sched= []

    #------------------------------------------    
    # current time at the bégining
    #------------------------------------------    
    before = time.time()

    #------------------------------------------    
    # Bounds for binary search
    #------------------------------------------
    A          = sum(matrixW)/m
    PSchedLPT  = lpt(matrixW, m)    # is a PSched
    M          = PSchedLPT.getMakespan()

    if M >= 1.5 * A:
        return PSchedLPT
    else:
        upperBound = M                                             # LPT result
        lowerBound = max(1, matrixW[0], (M / (4/3 - 1 / (3-m) )))  # for m <> 3

        while upperBound - lowerBound > alpha:
            n,sched = ffd(matrixW, M)
        
    # END IF
    
    
    


    
    

    #------------------------------------------
    # RETURN Makespan obtained /
    #        Processing algorithm time /
    #        Schedul 
    #------------------------------------------
    timeAlgo = after-before
    res = sm.PSched(algoName, timeExpected, makespan, timeAlgo, sched)
    return res





# #######################################################################
#                                                                       #
#                               FFD                                 #
#                                                                       #
# #######################################################################
def ffd(sizesList, binSize, sortList = False):
    """
    order the given objects in a non-decreasing order
    so that wehaves1≥···≥sn. Initialize a counterN= 0.2.
    Let the bins beB1,···, Bn.
    Put the next (first) object in thefirst “possible” bin ,
    scanning the bins in the orderB1,···, Bn.If a new bin is used, incrementN.
    Return number of bins used, and the binpacking computed
    """
    ffd        = []
    binsNumber = 0
    
    #------------------------------------------    
    # work with a copy of costMatrix
    # this matrix will be sorted or modified
    #------------------------------------------
    sizesListW = sizesList[:] # sizesListW = tools.matrix1dCopy(sizesList)
    if sortList==True:
        # the list is already sorted (if sortList=false)
        sizesListW.sort(reverse = True)
    # END IF    

    # FIRST FIT DECREASING 
    for i in range(len(sizesListW)):
        # Create first bin
        if binsNumber == 0:
            binsNumber+=1
            p = sm.Processor()
            ffd.append(p)
        # END IF
        
        # if bin loaded + new size > binSize
        # Must create a new bin
        if ffd[binsNumber-1].getTotal() + sizesListW[i] > binSize:
            binsNumber+=1
            p = sm.Processor()
            ffd.append(p)
        # END IF
        ffd[binsNumber-1].addJob(sizesListW[i])
    # END FOR
    return binsNumber,ffd




