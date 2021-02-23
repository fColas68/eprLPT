# to use gamma distribution
import numpy 

# ###########################################################################
#                                                                           #
#                                   SHUFFLING                               #
#                                                                           #
# ###########################################################################
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
    if m==0:
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

    #-----------------------------------------------------------#
    #                                                           #
    #  matrixResult : there are m rows of n cells               #
    #                                                           #
    #  eij ==>  matrixResult[j][i]                              #
    #-----------------------------------------------------------#
    
    # Matrix shuffling =========================================
    for j in range(m):
        for i in range(n):
            
            #
            iprime = ((numpy.random.random_integers(0, n-1)+ i - 1) % n)#+1
            jprime = ((numpy.random.random_integers(0, m-1)+ j - 1) % m)#+1

            #------------------------------------------------------
            #iprime = ((numpy.random.uniform(1, n-1)+ i - 1) % n)+1
            #jprime = ((numpy.random.uniform(1, n-1)+ i - 1) % m)+1
            #print(i,"-->",iprime,"##" ,j,"-->",jprime)
            #------------------------------------------------------
            e_ij           = matrixResult[j][i]
            e_iprimej      = matrixResult[j][iprime]
            e_ijprime      = matrixResult[jprime][i]
            e_iprimejprime = matrixResult[jprime][iprime]

            #
            if e_ij == min(e_ij, e_iprimej, e_ijprime, e_iprimejprime):
                d = min(e_iprimej-e_ij, e_ijprime - e_ij)
            elif e_iprimej == min(e_iprimej, e_ijprime, e_iprimejprime):
                d = -1 * min(e_ij-e_iprimej, e_iprimejprime - e_iprimej)
            elif e_ijprime == min(e_ijprime, e_iprimejprime):
                d = -1 * min(e_ij-e_ijprime, e_iprimejprime - e_ijprime)
            else:
                d = min(e_iprimej- e_iprimejprime, e_ijprime- e_iprimejprime)
            # end if

            matrixResult[j][i]          = e_ij          + d 
            matrixResult[j][iprime]     = e_iprimej     - d 
            matrixResult[jprime][i]     = e_ijprime     - d 
            matrixResult[jprime][iprime]= e_iprimejprime+ d 
            
        #end for i in range(n):
    #end for j in range(m):
            
    #===========================================================
    # RETURN matrixResult                                      =
    #===========================================================
    return matrixResult

# ###########################################################################
#                                                                           #
#                                   NOISE 1                                 #
#                                                                           #
# ###########################################################################
def noise1(n, Vtask, Vmach, m=1, Vnoise= 1):
    """
    Create a matrix according the shuffling method
                              the parameters choosen
    :param n    : jobs number
    :param m    : Machines number. idealy 0>=m>=n. (default=0). If m=0 or 1 then Problem is P.
    :param Vtask: Parameter 1 for heterogeneity tasks
    :param Vmach: Parameter 2 for heterogeneity machines
    :param Vnoise: noise factor 
    :return     : matrixResult (cost matrix) if m >1     : [[ei1, en1]...[e1m,...,enm]]
                                             if m=0 or 1 : [[ei, en]]] ( with [[ and ]] !!)
    """
    if m==0:
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
    else:
        bj.append(1)

    # ==========================================================
    # Matrix creation                                          =
    # With noise gamma distribution                            =
    # ==========================================================
    for j in range(m):
        machineRow = []
        for i in range(n):
            if m >= 2:
                machineRow.append(bj[j]* wi[i] * numpy.random.gamma(1/Vnoise**2, Vnoise**2))
            else:
                machineRow.append(wi[i] * numpy.random.gamma(1/Vnoise**2, Vnoise**2))
        # end for i in range(n):
            
        # add the machine row to the final matrix matrixResult
        matrixResult.append(machineRow)
    # end for j in range(m):

    #-----------------------------------------------------------#
    #                                                           #
    #  matrixResult : there are m rows of n cells               #
    #                                                           #
    #  eij ==>  matrixResult[j][i]                              #
    #-----------------------------------------------------------#

    #===========================================================
    # RETURN matrixResult                                      =
    #===========================================================
    return matrixResult

# ###########################################################################
#                                                                           #
#                                CROCE_UNIFORM                              #
#                                                                           #
# ###########################################################################
def noise1(n, a, b, m=1):




# m = noise1(500,2.8,200)
# print(m)
    
    
        
    

