# to use distributions
import numpy
import random
# import statistics

# tools library
import tools
import pwa

# ############################################################################
#
#                               PTimes class
#
# ############################################################################
class PTimes:
    """
    ##> management of the PTimes object: time list. 

    # Generation properties
    :param generateMethode: STRING describe how this list is generated.
                            "GAMMA"
                            "BETA"
                            "EXPONENTIAL"  
                            "UNIFORM"      uniform instencies generation LORI and MARTELLO)
                            "NON_UNIFORM"  non uniform instencies generation LORI and MARTELLO)
                            "REAL"         from workload archive - www.cs.huji.ac.il/labs/parallel/workload
    :param m              : Integer Machine number. 0 <= m < n. 0 if problemType = "P" and completedM1 = False
    :param a              : a value for uniform and non uniform generation
    :param b              : b value for uniform and non uniform generation
    :param alpha          : alpha value for beta and gamma generation
    :param beta           : beta value for gamma generation (beta value for beta is equal 1)
    :param lamlbd         : lambda value for exponential generation

    # List and Computed results with original times List
    :param Times                         : List   : of Pj : set of times   : [e1, e2, ... en]
    :param n                             : Integer: Jobs number. n > 0 for the original 
    :param LowBound                      : Float  : known low bound
    -----
    :param Results                       : tuples list of the results obtained with each algorithm, from the original time list.
                                           [(ALGORITHM1, computed makespan, computation time, resultMatrix []),...,(ALGORITHMp, computed makespan, computation time, resultMatrix[])]
    :param BestResult_Makespan           : Float  : Best Makespan obtained (closer to the lower bound)
    :param BestResult_MakespanAlgorithm  : String : Which algo got the best Makespan
    :param BestResult_Time               : float  : Best Time obtained (lower time)
    :param BestResult_TimeAlgorithm      : String : Which algo got the best time


    # List and Computed results with times List completed with m-1 job times
    :param Times                         : List   : of Pj : set of times   : [e1, e2, ... en']
    :param m1_n                          : Integer: new number of times set
    :param m1Optimal                     : Float  : known optimal 
    -----
    :param m1Results                     : Tuples List of the results obtained with each algorithm, from the completed time list.
                                           [(ALGORITHM1, computed makespan, computation time, resultMatrix []),...,(ALGORITHMp, computed makespan, computation time, resultMatrix[])]
    :param m1BestResult_Makespan         : FLOAT  : Best Makespan obtained (closer to the known m1Optimal)
    :param m1BestResult_MakespanAlgorithm: String : Which algo got the best Makespan
    :param m1BestResult_Time             : Float  : Best Time obtained (lower time)
    :param m1BestResult_TimeAlgorithm    : String :Which algo got the best time
    :return: nichts
    """
    # Generation properties 
    generateMethode                = ""
    m                              = 0
    a                              = 0.0
    b                              = 0.0
    alpha                          = 1.0
    beta                           = 1.0
    lambd                          = 1.0 # not lambda (with a) because reserved word
    fileName                       = ""
    
    # origin problem instance (not completed)
    Times                          = []
    n                              = 0
    lowBound                       = 0.0 
    Results                        = []
    BestResult_Makespan            = 0.0
    BestResult_MakespanAlgorithm   = ""
    BestResult_Time                = 0.0
    BestResult_TimeAlgorithm       = ""

    # completed problem instance (with m-1 tasks completion)
    m1Times                        = []
    m1_n                           = 0
    m1lowBound                     = 0.0 
    m1Optimal                      = []
    m1Results                      = []
    m1BestResult_Makespan          = 0.0
    m1BestResult_MakespanAlgorithm = ""
    m1BestResult_Time              = 0.0
    m1BestResult_TimeAlgorithm     = ""

    # ############################################################################
    # CONSTRUCTOR
    # ############################################################################
    def __init__(self, generateMethode, n, m, a=1.0, b=100.0, alpha=1.0, beta=1.0, lambd=1.0, fileName=""):
        """
        create Lists instances with
        # Input
        :param generateMethode: STRING describe how this matrix is generated. 
        :param n              : Integer Jobs number. n > 0
        :param m              : Integer Machine number. 0 <= m < n. 0 if problemType = "P" and completedM1 = False
        :param a              : Float   a value for uniform and non uniform generation
        :param b              : Float   b value for uniform and non uniform generation
        :param alpha          : Float   alpha value for beta and gamma generation
        :param beta           : Float   beta value for gamma generation (beta value for beta is equal 1)
        :param lamlbd         : Float   lambda value for exponential generation
        :param fileName       : String  (complete filename) for PWA (Parallel Workload Archive) import

        # Computed
        Times                 
        n                     
        LowBound
        m1Times                 
        m1_n
        m1LowBound
        m1Optimal

        # Output
        nichts
        
        """
        # =======================================================================
        # generation properties
        # =======================================================================
        self.generateMethode    = generateMethode
        self.m                  = m
        self.a                  = a
        self.b                  = b
        self.alpha              = alpha
        self.beta               = beta
        self.lambd              = lambd
        self.fileName           = fileName

        # =======================================================================
        # self.Times generation
        # =======================================================================
        self.Time               = []
        self.n                  = n
        # UNIFORM P: 
        if (self.generateMethode == "UNIFORM"):
            self.Times = uniform_p(n,a,b)
        # NON_UNIFORM P:
        elif (self.generateMethode == "NON_UNIFORM"):
            self.Times  = non_uniform_p(n,a, b)
        # GAMMA P: problem not considered at this time.
        elif (self.generateMethode == "GAMMA"):
            self.Times  = gamma_p(n,alpha, beta)
        # BETA P:
        elif (self.generateMethode == "BETA"):
            self.Times  = beta_p(n,alpha)
        # EXPONENTIAL P: 
        elif (self.generateMethode == "EXPONENTIAL"):
            self.Times  = exponential_p(n,lambd)
        # REAL : Real, According the "parallel work load archive"
        #elif (self.generateMethode == "REEL"):
        else:
            self.Times  = real_p(fileName)
            
        # ENDIF

        self.lowBound = max(max(self.Times), sum(self.Times)/self.n)
        
        # =======================================================================
        # self.m1Times generation
        # =======================================================================
        self.completeM1()

    # ############################################################################
    # Matrix transformations methods
    # ############################################################################
    def completeM1(self):
        """
        Complete list Times with m-1 job times in list m1Times
        # input
        no input
        # Compute
        m1Times
        m1Optimal,
        m1_n,
        """
        #------------------------------------------------------------------------
        #   INIT
        #------------------------------------------------------------------------
        proc = []               # work with processors list len(proc) <= m
        
        #------------------------------------------------------------------------
        #   matrixOrigin --> matrix
        #------------------------------------------------------------------------
        self.m1Times = tools.matrix1dCopy(self.Times)
        new_n = self.n
        
        #------------------------------------------------------------------------
        # Scrolls through the "self.matrix" list to
        # fill in the processor load list "proc"
        #------------------------------------------------------------------------
        for i in range(len(self.Times)):
            if (len(proc) < self.m):
                proc.append(float(self.Times[i]))
            else:
                # sorts the proc list and fills in the first one which is the smallest.
                proc.sort()  
                proc[0] = float(proc[0]) + float(self.Times[i])
            # END IF
        # END FOR

        #------------------------------------------------------------------------
        # sorts the list proc in the rerverse order.
        # The first element is the most loaded :
        # fill in the remain self.m&Times to obtain same Cmax on all proc[x]
        #------------------------------------------------------------------------
        proc.sort(reverse=True)
        Cmax = proc[0]
        for i in range(len(proc)):
            if (i > 0):
                self.m1Times.append(Cmax - proc[i])
                new_n += 1
            # END IF
        # END FOR

        #------------------------------------------------------------------------
        #   Update self concerneds values
        #------------------------------------------------------------------------
        self.m1_n       = new_n
        self.m1lowBound = max(max(self.m1Times), sum(self.m1Times)/self.m1_n)
        self.m1Optimal  = Cmax

    # ############################################################################
    # ADD RESULTS
    # ############################################################################
    def addSched(self, sched):
        self.Results.append(sched)
        if (sched.getTime() < self.BestResult_Time) or (self.BestResult_Time == 0.0):
            self.BestResult_Time          = sched.getTime()
            self.BestResult_TimeAlgorithm = sched.getAlgoName()
        # END IF
        if (sched.getMakespan() < self.BestResult_Makespan) or (self.BestResult_Makespan == 0.0):
            self.BestResult_Makespan      = sched.getMakespan()
            self.BestResult_TimeAlgorithm = sched.getAlgoName()
        # END IF

    def addM1Sched(self, sched):
        self.m1Results.append(sched)
        if (sched.getTime() < self.m1BestResult_Time)  or (self.m1BestResult_Time == 0.0):
            self.m1BestResult_Time          = sched.getTime()
            self.m1BestResult_TimeAlgorithm = sched.getAlgoName()
        # END IF
        if (sched.getMakespan() < self.m1BestResult_Makespan) or (self.BestResult_Makespan == 0.0):
            self.m1BestResult_Makespan      = sched.getMakespan()
            self.m1BestResult_TimeAlgorithm = sched.getAlgoName()
        # END IF

# ############################################################################
#
#                               Time lists generation
#
# ############################################################################
def uniform_p(n,a,b):
    matrix = []
    for i in range(n):
        rand = random.uniform(a,b)
        matrix.append(rand)
    # END FOR    
    return matrix

def non_uniform_p(n,a,b):
    matrix = []
    #
    n98 = int((98*n) / 100)
    a1 = 0.9*(b-a)
    b1 = b
    a2 = a
    b2 = 0.2*(b-a)
    for i in range(n98):
        rand = random.uniform(a1,b1)
        matrix.append(rand)
    # END FOR
    for i in range(n-n98):
        rand = random.uniform(a2,b2)
        matrix.append(rand)
    # END FOR    
    return matrix

def gamma_p(n,alpha,beta):
    matrix = []
    for i in range(n):
        rand = random.gammavariate(alpha,beta)
        matrix.append(rand)
    # END FOR        
    return matrix

def beta_p(n,alpha):
    """
    beta allways 1 for this set
    """
    matrix = []
    for i in range(n):
        rand = random.betavariate(alpha,1)
        matrix.append(rand)
    # END FOR        
    return matrix

def exponential_p(n,lambd):
    matrix = []
    for i in range(n):
        rand = random.expovariate(lambd)
        matrix.append(rand)
    # END FOR        
    return matrix

def real_p(fileName):
    matrix = pwa.pwaFileRead(fileName)
    return matrix





