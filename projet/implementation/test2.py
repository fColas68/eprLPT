import costMatrixObject as cm
import costMatrixMakespan as cmm
import ScheduleManagment as sm

def main():
    # set of testing matricies
    matricies = []
    print("Job Set size ============================================================")
    nN                  = 5
    #
    matUniformNumber    = 2
    matNonUniformNumber = 0
    matGammaNumber      = 0
    matBetaNumber       = 0
    matExponentialNumber= 0
    matRealNumber       = 0
    #
    nAb = 1.0
    nBb = 100.0
    nAlpah = 1.0
    nBeta = 1.0
    nLambda = 1.0
    #
    lCompleteM1 = True  # issue : deffect when False
    machineNumber = 4

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
    print("")

    print("===========================================================")
    print("LPT ")    
    print("===========================================================")
    for i in range(len(matricies)):
        reslpt = cmm.lpt(matricies[i].matrix[0], matricies[i].m)
        print("Expected :",matricies[i].lowBoundcompletedM1,", Obtained :",reslpt[0], ", Time:", reslpt[1])

        #
        # print("Schedule obtained")
        # for i in range(len(reslpt[2])):
        #    print(reslpt[2][i].jobsLoaded,"#" ,reslpt[2][i].jobsSet)
        
        
        resslack = cmm.slack(matricies[i].matrix[0], matricies[i].m)
        print("Expected :",matricies[i].lowBoundcompletedM1,", Obtained :",resslack[0], ", Time:", resslack[1])

        print("")
        # resSlack = cmm.slack(matricies[i].matrix[0], matricies[i].m)
        # print(resSlack[0], matricies[i].lowBoundcompletedM1, resSlack[1])
        
    
if __name__ == "__main__":
    main()

    
    
