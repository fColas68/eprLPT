import costMatrixObject as cm
import costMatrixMakespan as cmm


def main():
    # set of testing matricies
    matricies = []
    print("Job Set size ============================================================")
    nN                  = int(input("Number of jobs : "))

    print("Job set generation ======================================================")    
    matUniformNumber    = int(input("How many uniform matricies to generate : "))
    matNonUniformNumber = int(input("How many non uniform matricies to generate : "))
    matGammaNumber      = int(input("How many Gamma matricies to generate : "))
    matBetaNumber       = int(input("How many Beta matricies to generate : "))
    matExponentialNumber= int(input("How many Exponential matricies to generate : "))
    matRealNumber       = int(input("How many Real matricies to generate : "))

    print("Properties of generation ================================================")
    nAb = 0.0
    nBb = 0.0
    nAlpah = 0.0
    nBeta = 0.0
    nLambda = 0.0
    if (matUniformNumber > 0 or matNonUniformNumber > 0):
        nAb = float(input("a parameter : "))
        nBb = float(input("b parameter : "))
    if (matGammaNumber > 0 or matBetaNumber > 0):
        nAlpah = float(input("alpha parameter (for gamma and beta) : "))
    if (matGammaNumber > 0):
        nBeta = float(input("beta parameter (for gamma) : "))
    if (matExponentialNumber>0):
        nLambda = float(input("lambda parameter (for ecxponential) : "))

    print("Transformation completion for real optimal ==============================")
    machineNumber = 0
    if int(input("Complete with m-1 job 0=False, 1=True : ")) == 0:
        lCompleteM1 = False
    else:
        lCompleteM1 = True
        machineNumber = int(input("Machines number : "))

    print("Generation (please wait =================================================")
    # UNIFORM P    
    for i in range(matUniformNumber):
        m = cm.CostMatrix("P", "UNIFORM", nN, nAb, nBb)
        if (lCompleteM1 == True):
            m.completeM1(machineNumber)
        matricies.append(m)
        
    # NON UNIFORM P    
    for i in range(matNonUniformNumber):
        m = cm.CostMatrix("P", "NON_UNIFORM", nN, nAb, nBb)
        if (lCompleteM1 == True):
            m.completeM1(machineNumber)
        matricies.append(m)
    # GAMMA P    
    for i in range(matNonUniformNumber):
        m = cm.CostMatrix("P", "GAMMA", nN, nAb, nBb)
        if (lCompleteM1 == True):
            m.completeM1(machineNumber)
        matricies.append(m)    
    # BETA P    
    for i in range(matNonUniformNumber):
        m = cm.CostMatrix("P", "BETA", nN, nAb, nBb)
        if (lCompleteM1 == True):
            m.completeM1(machineNumber)
        matricies.append(m)    
    # EXPENENTIAL P    
    for i in range(matNonUniformNumber):
        m = cm.CostMatrix("P", "EXPONENTIAL", nN, nAb, nBb)
        if (lCompleteM1 == True):
            m.completeM1(machineNumber)
        matricies.append(m)    
    # REAL P    
    for i in range(matRealNumber):
        m = cm.CostMatrix("P", "REAL")
        if (lCompleteM1 == True):
            m.completeM1(machineNumber)
        matricies.append(m)    

    print("Generated ================================================================")
    
    print(matricies)

    print("===========================================================")
    print(matricies[0].matrixOrigin)
    print("===========================================================")
    print(matricies[0].matrix)
    
    print("===========================================================")
    print("LPT ")    
    print("===========================================================")
    for i in range(len(matricies)):
        print(matricies[i].matrix[0])
        cmm.lpt(matricies[i].matrix[0], matricies[i].m)

if __name__ == "__main__":
    main()

    
    
