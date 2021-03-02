import time
import math
from operator import attrgetter
#
import costMatrixObject as cm
import ScheduleManagment as sm # Processor object
import tools

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
      tuple of 3 items:
        makespan : makesapn comuted
        time     : the time it took to calculate the makespan
        sched    : in the form of a Processor object list. Each "Processor" object represents the load of a machine, with the total time and a list of each job cost allocated to that processor.
    """
    print("Begin LPT Number of machines :",m)
    #------------------------------------------    
    # work with a copy of costMatrix
    # this matrix will be sorted or modified
    #------------------------------------------    
    matrixW = tools.matrix1dCopy(costMatrix)

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
            p.jobAdd(matrixW[i])
            sched.append(p)
            
        else:
            #------------------------------------------    
            # The maximum number of processors (or machines) is reached.
            # Each cost is allocated to the least loaded
            # processor (machine) at this time.
            #------------------------------------------    
            sched.sort(key=attrgetter("jobsLoaded"))
            sched[0].jobAdd(matrixW[i])
            

    #------------------------------------------            
    # current time at the bégining
    #------------------------------------------    
    after = time.time()

    #------------------------------------------            
    # Retrieve Makespan (most loaded machine)
    #------------------------------------------    
    makespan = 0
    for i in range(len(sched)):
        makespan = max(makespan, sched[i].jobsLoaded)

    #------------------------------------------
    # RETURN Makespan obtained /
    #        Processing algorithm time /
    #        Schedul 
    #------------------------------------------    
    return makespan, after-before, sched
    

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
      tuple of 3 items:
        makespan : makesapn comuted
        time     : the time it took to calculate the makespan
        sched    : in the form of a Processor object list. Each "Processor" object represents the load of a machine, with the total time and a list of each job cost allocated to that processor.
    """
    print("Begin SLACK Number of machines :",m)
    #------------------------------------------    
    # work with a copy of costMatrix
    # this matrix will be sorted or modified
    #------------------------------------------    
    matrixW = tools.matrix1dCopy(costMatrix)
    
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
            p.jobAdd(matrixW[i])
            matrixGreedy.append(p)
        else:
            matrixGreedy[subsetNumbers].jobAdd(matrixW[i])
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
            p.jobAdd(matrixWSlack[i])
            sched.append(p)
            
        else:
            #------------------------------------------    
            # The maximum number of processors (or machines) is reached.
            # Each cost is allocated to the least loaded
            # processor (machine) at this time.
            #------------------------------------------    
            sched.sort(key=attrgetter("jobsLoaded"))
            sched[0].jobAdd(matrixWSlack[i])

    #------------------------------------------    
    # current time at the end
    #------------------------------------------    
    after  = time.time()

    #------------------------------------------            
    # Retrieve Makespan (most loaded machine)
    #------------------------------------------    
    makespan = 0
    for i in range(len(sched)):
        makespan = max(makespan, sched[i].jobsLoaded)

    #------------------------------------------
    # RETURN Makespan obtained /
    #        Processing algorithm time /
    #        Schedul 
    #------------------------------------------    
    return makespan, after-before, sched

