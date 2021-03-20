import time
import pandas as pd
import os

import matrix            as cm
import algorithms        as cmm
import ScheduleManagment as sm
import pwa               as pwa
import setup             as s


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
    #
    #                       CONSTRUCTOR
    #
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
        #
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
        # END IF    
            
        # CREATE "SET OF TIMES INSTANCIES" IN self.matricies
        self.createMatricies()

    # #######################################################################
    #
    #                       MATRICIES CONSTRUCTION
    #
    # #######################################################################
    def createMatricies(self):
        #=====================================================
        # according statistics distributions
        # j is the jobs iterator
        # i is the machines itérator
        #=====================================================
        for j in range(self.N_NumberBegin, self.N_NumberEnd+1):
            for i in range(self.M_NumberBegin, self.M_NumberEnd+1):
                # UNIFORM 
                for k in range(self.matUniformNumber):
                    m = cm.PTimes("UNIFORM", j, i, self.a, self.b, self.alpha, self.beta, self.lambd, "", self.seed)
                    self.matricies.append(m)
                # END FOR    

                # NON UNIFORM P    
                for k in range(self.matNonUniformNumber):
                    m = cm.PTimes("NON_UNIFORM", j, i, self.a, self.b, self.alpha, self.beta, self.lambd, "", self.seed)
                    self.matricies.append(m)
                # END FOR
                
                # GAMMA P    
                for k in range(self.matGammaNumber):
                    m = cm.PTimes("GAMMA", j, i, self.a, self.b, self.alpha, self.beta, self.lambd, "", self.seed)
                    self.matricies.append(m)
                # END FOR
                
                # BETA P    
                for k in range(self.matBetaNumber):
                    m = cm.PTimes("BETA", j, i, self.a, self.b, self.alpha, self.beta, self.lambd, "", self.seed)
                    self.matricies.append(m)
                # END FOR

                # EXPENENTIAL P    
                for k in range(self.matExponentialNumber):
                    m = cm.PTimes("EXPONENTIAL", j, i, self.a, self.b, self.alpha, self.beta, self.lambd, "", self.seed)
                    self.matricies.append(m)
                # END FOR
            # END for i in range(self.M_NumberBegin, self.M_NumberEnd)):
        # END FOR for i in range(self.N_NumberBegin, self.N_NumberEnd):

        #=====================================================
        # Real life jobs log
        # i is the machines itérator
        #=====================================================
        for i in range(self.M_NumberBegin, self.M_NumberEnd+1):
            # REAL P    
            for k in range(len(self.matRealFiles)):
                m = cm.PTimes("REAL", j, i, self.a, self.b, self.alpha, self.beta, self.lambd, self.matRealFiles[k])
                self.matricies.append(m)
            # END FOR    
        # END for i in range(self.M_NumberBegin, self.M_NumberEnd)):

    # #######################################################################
    #
    #                              RUN ALGORITHMS
    #
    # #######################################################################
    def runAlgorithm(self, algo):
        """
        algo is a function from algorithm.py
        lpt
        slack
        combine
        ldm
        ...
        """
        # each matricies[k] is a PTimes object
        for k in range(len(self.matricies)):
            # work with PTimes.Times list cmm.lpt
            r = algo(self.matricies[k].Times, self.matricies[k].m)
            self.matricies[k].addSched(r)
            print("best result      :",self.matricies[k].BestResult_Makespan,", Obtained :",r.getMakespan(), ", Time:", r.getTime())
            
            # work with PTimes.m1Times list
            r = algo(self.matricies[k].m1Times, self.matricies[k].m)
            self.matricies[k].addM1Sched(r)
            print("Expected optimal :",self.matricies[k].m1Optimal,", Obtained :",r.getMakespan(), ", Time:", r.getTime())
        # END FOR    

        
    # #######################################################################
    #
    #                              CSV EXPORT
    #
    # #######################################################################
    def exportCSV(self):

        # target file
        resDir = s.folder(s.FOLDER_RESULTS)
        filename = resDir + s.sepDir()+ self.campaignName+".csv"
        print("Exporting campaign to %s . please wait..." % (filename))
        #
        # collumns = ""
        dataResult       = []
        #print(len(self.matricies))

        # 
        for k in range(len(self.matricies)):
            item = self.matricies[k].getResult() 
            dataResult.append(item)
        # END FOR

        # EXPORT
        expResultHead = pd.DataFrame(dataResult) #, collumns)
        expResultHead.to_csv(filename, index=False, header=False)
        

