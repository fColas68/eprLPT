# to use gamma distribution
import numpy 

def shuffling(n, Vtask, Vmach, m=1):
    """
    Create a matrix according the shuffling method
                              the parameters choosen
    :param n    : jobs number
    :param m    : Machines number. idealy 0>=m>=n. (default=0). If m=0 or 1 then Problem is P.
    :param Vtask: Parameter 1 for heterogeneity tasks
    :param Vmach: Parameter 2 for heterogeneity machines
    :return     : matrixResult (cost matrix) if m >1     : [[ei1, en1]...[e1m,...,enm]]
                                             if m=0 or 1 : [[ei, en]]] ( with [[ and ]] !!)
    """
    if m=0:
        m=1

    wi = []
    bj = []
    machineRow = []
    matrixResult = []

    # Tasks ====================================================
    for i in range(n):
        wi.append(numpy.random.gamma(1/Vtask**2, Vtask**2))

    # speed machines cycle =====================================
    if m >= 2:
        for j in range(m):
            bj.append(numpy.random.gamma(1/Vmach**2, Vmach**2))

    # Matrix creation ==========================================
    if m >= 2:
        for j in range(m):
            machineRow = []
            for i in range(n):
                machineRow.append(bj[j]* wi[i])
            # end for i in range(n):
            
            # add the machine row to the final matrix matrixResult
            matrixResult.append(machineRow)
        # end for j in range(m):
        
    else:
        matrixResult.append(wi)
    # end  if m > 1:
    
    # Matrix shuffling =========================================
    for j in range(m):
        for i in range(n):
            iprime = (numpy.random.uniform(1, n-1)+ i - 1 mod n)+1
            jprime = (numpy.random.uniform(1, n-1)+ i - 1 mod m)+1
            
        #end for i in range(n):
    #end for j in range(m):    
            
    
    return matrixResult

m = shuffling(4,2,2, 3)
print(m)
    
    
        
    

