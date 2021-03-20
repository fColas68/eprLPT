import time
import pandas as pd
import os

import matrix as cm
import algorithms as cmm
import ScheduleManagment as sm
import pwa


class Campaign():
    # set of testing matricies -------------------------------------
    matricies           = []
    #---------------------------------------------------------------
    campaignName        = ""
    campaignDate        = ""
    campaignUser        = ""
    #---------------------------------------------------------------
    N_NumberBegin       = 0
    N_NumberEnd         = 0
    M_NumberBegin       = 0
    M_MumberEnd         = 0 
    #---------------------------------------------------------------
    matUniformNumber    = 0
    matNonUniformNumber = 0
    matGammaNumber      = 0
    matBetaNumber       = 0
    matExponentialNumber= 0
    #print("_____ From Parallel WorkLoad Archive _____")
    matRealFiles        = [] # pwa.pwaFileChoice()
    #---------------------------------------------------------------
    a                   = 1.0
    b                   = 100.0
    alpha               = 1.0
    beta                = 1.0
    lambd               = 1.0
    #---------------------------------------------------------------
    seed = None #essential 

    # #######################################################################
    # CONSTRUCTOR
    # #######################################################################
    def __init__(self, campaignName, campaignUser, N_NumberBegin, N_NumberEnd, M_NumberBegin, M_NumberEnd, matUniformNumber, matNonUniformNumber, matGammaNumber, matBetaNumber, matExponentialNumber, matRealFiles, a, b, alpha, beta, lambd, seedForce = None):
        self.matricies           = []
        #
        self.campaignName        = campaignName
        self.campaignDate        = time.strftime("%d%m%Y")
        self.campaignUser        = campaignUser
        #
        self.N_NumberBegin        = N_NumberBegin
        self.N_NumberEnd          = N_NumberEnd
        self.M_NumberBegin        = M_NumberBegin
        self.M_NumberEnd          = M_NumberEnd
        #
        self.matUniformNumber    = matUniformNumber
        self.matNonUniformNumber = matNonUniformNumber
        self.matGammaNumber      = matGammaNumber
        self.matBetaNumber       = matBetaNumber
        self.matExponentialNumber= matExponentialNumber
        #print("_____ From Parallel WorkLoad Archive _____")
        self.matRealFiles        = matRealFiles[:]
        #
        self.a                   = a
        self.b                   = b
        self.alpha               = alpha
        self.beta                = beta
        self.lambd               = lambd
        #
        if seedForce:
            self.seed            = seedForce
            
        # CREATE INSTANCIES IN self.matricies
        self.createMatricies()

    # #######################################################################
    # MATRICIES CONSTRUCTION
    # #######################################################################
    def createMatricies(self):

        # j is the jobs iterator
        # i is the machines itérator
        print(self.N_NumberBegin, self.N_NumberEnd+1)
        
        for j in range(self.N_NumberBegin, self.N_NumberEnd+1):
            for i in range(self.M_NumberBegin, self.M_NumberEnd+1):
                # UNIFORM 
                for k in range(self.matUniformNumber):
                    m = cm.PTimes("UNIFORM", j, i, self.a, self.b, self.alpha, self.beta, self.lambd, "", self.seed)
                    self.matricies.append(m)
                # END FOR    

                # NON_UNIFORM

            # END for i in range(self.M_NumberBegin, self.M_NumberEnd)):
        # END FOR for i in range(self.N_NumberBegin, self.N_NumberEnd):
        
        
        
    # #######################################################################
    # CSV EXPORT
    # #######################################################################
    def exportCSV(self):
        resDir = resFolder()
        filename = resDir + "/" + self.campaignName+".csv"
        print("Exporting campaign to %s . please wait..." % (filename))

        collumns = ""
        dataResult       = []
        print(len(self.matricies))
        
        for n in range(len(self.matricies)):
            item = self.matricies[n].getResult() # used by __str__ method in matrix class
            print(">", item, "<")
            dataResult.append(item)
        # END FOR    
        expResultHead = pd.DataFrame(dataResult) #, collumns)
        expResultHead.to_csv(filename, index=False, header=False)
        

# ###########################################################################
# ===========================================================================
#   APPENDIX TOOLS
# ===========================================================================
# ###########################################################################
def resFolder():
    """
    Verify if resFolder exists.
    if not create it
    return the folder
    """
    resFolder = "./results"
    if not os.path.exists(resFolder):
        os.makedirs(resFolder)
    # END IF    
    return resFolder
        
