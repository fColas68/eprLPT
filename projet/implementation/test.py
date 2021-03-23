import campaign as cp
import matrix as cm
import algorithms as cmm
import ScheduleManagment as sm
import pwa


def main():
    # set of testing matricies
    matricies = []

    print("SEED ============================================================")
    campaignName         = input("Name of campaign : ")
    campaignUser         = input("Your Name : ")
    seedForce = None
    sSeedForce            = input("Force seed ? (None default): ")
    if sSeedForce:
        seedForce = int(sSeedForce)
    # END IF    
    

    print("Job Set size ============================================================")
    nN                  = int(input("Jobs number  (begin) : "))
    sNe                 = input("Jobs number (end) ("+str(nN)+" default) : ")

    N_NumberBegin = nN
    N_NumberEnd = nN
    if sNe:
        if int(sNe) >  nN:
            N_NumberEnd = int(sNe)
        # END IF
    # END IF
    
    nMmachineNumber     = int(input("Machines number (begin) : "))
    sMmachineNumbere    = input("Machines number (end) ("+str(nMmachineNumber)+"default) : ")
    M_NumberBegin = nMmachineNumber
    M_NumberEnd = nMmachineNumber
    
    if sMmachineNumbere:
        if int(sMmachineNumbere) >  nMmachineNumber:
            M_NumberEnd   = int(sMmachineNumbere)
        # END IF
    # END IF

    print("Job set generation ======================================================")    
    matUniformNumber    = int(input("How many uniform matricies to generate : "))
    matNonUniformNumber = int(input("How many non uniform matricies to generate : "))
    matGammaNumber      = int(input("How many Gamma matricies to generate : "))
    matBetaNumber       = int(input("How many Beta matricies to generate : "))
    matExponentialNumber= int(input("How many Exponential matricies to generate : "))
    print("_____ From Parallel WorkLoad Archive _____")
    matRealFiles        = pwa.pwaFileChoice()

    print("Properties of generation ================================================")
    nAb = 1.0
    nBb = 100.0
    nAlpah = 1.0
    nBeta = 1.0
    nLambda = 1.0
    filename=""

    if (matUniformNumber > 0 or matNonUniformNumber > 0):
        nAb = float(input("a parameter : "))
        nBb = float(input("b parameter : "))
    if (matGammaNumber > 0 or matBetaNumber > 0):
        nAlpah = float(input("alpha parameter (for gamma and beta) : "))
    if (matGammaNumber > 0):
        nBeta = float(input("beta parameter (for gamma) : "))
    if (matExponentialNumber>0):
        nLambda = float(input("lambda parameter (for ecxponential) : "))

    print("Algorithms ================================================")
    useLPT     = int(input("Use LPT rule ? : (1 yes, 0 no) : "))
    useSLACK   = int(input("Use Slack    ? : (1 yes, 0 no) : "))
    useLDM     = int(input("Use LDM      ? : (1 yes, 0 no) : "))
    useCOMBINE = int(input("Use COMBINE  ? : (1 yes, 0 no) : "))

    print("Results computation ================================================")    
    c = cp.Campaign(campaignName, campaignUser, N_NumberBegin, N_NumberEnd, M_NumberBegin, M_NumberEnd, matUniformNumber, matNonUniformNumber, matGammaNumber, matBetaNumber, matExponentialNumber, matRealFiles, nAb, nBb, nAlpah, nBeta, nLambda, seedForce)
    #
    if useLPT==1:
        c.runAlgorithm(cmm.lpt)
    # END IF    
    
    if useSLACK==1:
        c.runAlgorithm(cmm.slack)
    # END IF        
    
    if useLDM==1:
        c.runAlgorithm(cmm.ldm)
    # END IF
    
    if useCOMBINE==1:
        print("Not yet implemented.")
    # END IF

    c.exportCSV()        
    

if __name__ == "__main__":
    main()
