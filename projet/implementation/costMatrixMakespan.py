import time
from operator import attrgetter
#
import costMatrixObject as cm
import ScheduleManagment as sm # Processor object
import tools

def lpt(costMatrix, m):
    print("Begin LPT Number of machines :",m)

    #------------------------------------------    
    # work with a copy of costMatrix
    #------------------------------------------    
    matrixW = tools.matrix1dCopy(costMatrix)

    #------------------------------------------    
    # sched is a list of Processor objects.
    #------------------------------------------    
    sched= [] 

    #------------------------------------------    
    # sort matrix according LPT rule
    #------------------------------------------    
    matrixW.sort(reverse=True)

    #------------------------------------------    
    #
    #------------------------------------------    
    before = time.time()

    #------------------------------------------    
    #
    #------------------------------------------    
    for i in range(len(matrixW)):
        if (len(sched) < m):
            p = sm.Processor()
            p.jobAdd(matrixW[i])
            sched.append(p)
            
        else:
            sched.sort(key=attrgetter("jobsLoaded"))
            sched[0].jobAdd(matrixW[i])
            

    #------------------------------------------            
    #
    #------------------------------------------    
    after = time.time()

    #------------------------------------------            
    # Retrieve Makespan
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
    


