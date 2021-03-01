import costMatrixGenerate    # Costs matricies generators library
import tools

class CostMatrix:
    """
    CostMatrix manage costs matrix. 

    ----- Managment properties --------------------------------------------------------------------------------
    :param problemType    : String. Define problem type P(default)                                            
                            P: for P||Cmax                                                                    
                            R: for R||Cmax
                            Q: for Q||Cmax
    ----- Generation properties -------------------------------------------------------------------------------
    :param generateMethode: STRING describe how this matrix is generated.
                            "GAMMA"
                            "BETA"
                            "EXPONENTIAL"  
                            "UNIFORM"      uniform instencies generation LORI and MARTELLO)
                            "NON_UNIFORM"  non uniform instencies generation LORI and MARTELLO)
                            "REAL"         from workload archive - www.cs.huji.ac.il/labs/parallel/workload
    :param completedM1         : boolean True if worklaod completed with m-1 jobs (to reach low bound)
    :param n              : Integer Jobs number. n > 0
    :param m              : Integer Machine number. 0 <= m < n. 0 if problemType = "P" and completedM1 = False
    :param a              : a value for uniform and non uniform generation
    :param b              : b value for uniform and non uniform generation
    :param alpha          : alpha value for beta and gamma generation
    :param beta           : beta value for gamma generation (beta value for beta is equal 1)
    :param lamlbd         : lambda value for exponential generation
    
    ----- Generation Hererogeneity properties ----------------------------------------------------------------
    :param Vtask          : Parameter 1 for heterogeneity tasks
    :param Vmach          : Parameter 2 for heterogeneity machines
    :param noise          : Only if generateMethode ="NOISE1" or "NOISE1". noise factor
     
    ----- Heterogeneity properties computed ------------------------------------------------------------------
    :param mch            : real. non intuitives measures : Machine Performance Homogeneity
    :param tdh            : real. non intuitives measures : Task Difficulty Homogeneity
    :param VMutask        : real. intuitives measures : CV of means tasks 
    :param MuVtask        : real. intuitives measures : mean of CVs tasks
    :param VMumach        : real. intuitives measures : CV of means machines 
    :param MuVmach        : real. intuitives measures : mean of CVs machines
    :param skewness       : real. futur : skewness factor
    :param kurtosis       : real. futur : kurtosis factor
     
    ----- Matricies ------------------------------------------------------------------------------------------
    :param matrixOrigin   : double matrix. Pij set of costs
                            [[e1, e2, ... en]]
                            [[e11, e12, ... e1n]...[em1, em2, ... emn]]   for problemType = "R"
    :param matrix         : double matrix. Pij set of costs after transformation. 
                            [[e1, e2, ... en]]
                            [[e11, e12, ... e1n]...[em1, em2, ... emn]]   for problemType = "R"
     
    ---- Computed results ------------------------------------------------------------------------------------
    :param lowBoundcompletedM1 : float
    :param bestResult     : float 
     
    :param matrixResults  : matrix.
                            [(ALGORITHM1, computed makespan, comutation time, resultMatrix []),...,(ALGORITHMn, computed makespan, comutation time, resultMatrix [])]
                            
    :return: nichts
    """
    problemType     = ""
    #
    generateMethode = ""
    completedM1     = False
    n               = 0
    m               = 0
    a               = 0.0
    b               = 0.0
    alpha           = 1.0
    beta            = 1.0
    lambd           = 1.0 # non lambda (with a) because reserved
    #
    Vtask           = 0.0
    Vmach           = 0.0
    noise           = 0.0
    #
    mch             = 0.0
    tdh             = 0.0
    VMutask         = 0.0
    MuVtask         = 0.0
    VMumach         = 0.0
    MuVmach         = 0.0
    skewness        = 0.0
    kurtosis        = 0.0
    #
    matrixOrigin    = []
    matrix          = []
    #
    matrixResults   = []
    lowBoundcompletedM1 = 0.0
    bestResult      = 0.0
    # ############################################################################
    # CONSTRUCTOR
    # ############################################################################
    def __init__(self, probleme, generateMethode, n=0, a=0.0, b=0.0, alpha=1.0, beta=1.0, lambd=1.0, m = 0):
        """
        create CostMatrix instance with
        :param problemType    : String. Define problem type P(default) "P" "Q" "R"
        :param generateMethode: STRING describe how this matrix is generated. 
        :param n              : Integer Jobs number. n > 0
        :param m              : Integer Machine number. 0 <= m < n. 0 if problemType = "P" and completedM1 = False
        :param a              : a value for uniform and non uniform generation
        :param b              : b value for uniform and non uniform generation
        :param alpha          : alpha value for beta and gamma generation
        :param beta           : beta value for gamma generation (beta value for beta is equal 1)
        :param lamlbd         : lambda value for exponential generation
        result is matrixOrigin
        """
        self.problemType        = probleme
        self.generateMethode    = generateMethode
        self.n                  = n
        self.m                  = m
        self.a                  = a
        self.b                  = b
        self.alpha              = alpha
        self.beta               = beta
        self.lambd              = lambd
        self.matrixOrigin       = []

        # =======================================================================
        # self.matrixmatrixOrigin generation
        # =======================================================================

        #------------------------------------------------------------------------
        #   P Problem
        #------------------------------------------------------------------------
        if (self.problemType) == "P":
            # UNIFORM P: 
            if (self.generateMethode == "UNIFORM"):
                self.matrixOrigin = costMatrixGenerate.uniform_p(n,a,b)
                
            # NON_UNIFORM P:
            elif (self.generateMethode == "NON_UNIFORM"):
                self.matrixOrigin = costMatrixGenerate.non_uniform_p(n,a, b)

            # GAMMA P: problem not considered at this time.
            elif (self.generateMethode == "GAMMA"):
                self.matrixOrigin = costMatrixGenerate.gamma_p(n,alpha, beta)

            # BETA P: 
            elif (self.generateMethode == "BETA"):
                self.matrixOrigin = costMatrixGenerate.beta_p(n,alpha)

            # EXPONENTIAL P: 
            elif (self.generateMethode == "EXPONENTIAL"):
                self.matrixOrigin = costMatrixGenerate.exponential_p(n,lambd)
                
            # REAL : Real, According the "parallel work load archive"
            # elif (self.generateMethode == "REEL"):
            else:
                self.matrixOrigin = costMatrixGenerate.real_p()
                
        #----------------------------------------------------------------
        #   Q-R Problem
        #----------------------------------------------------------------
        elif (self.problemType == "Q" or self.problemType == "R"):
            print("problem not considered at this time.")
            # SHUFFLING : Shuffling algorythm
            #if (self.generateMethode == "SHUFFLING"):
            #    self.matrix = matrixGenerateshuffling.shuffling(n,m,xtask, xmach)
            # NOISE : Shuffling algorythm
            #elif (self.generateMethode == "NOISE"):
            #    self.matrix = matrixGenerateshuffling.noise(n,m,xtask, xmach)
            # REEL : Reel, According the "parallel work load archive"
            # elif (self.generateMethode == "REEL"):
            #else:
            #    self.matrix = costMatrixGenerate.reel_r(n,m,xtask, xmach)

        #------------------------------------------------------------------------
        #   matrixOrigin --> matrix
        #------------------------------------------------------------------------
        self.matrix = tools.matrix2dCopy(self.matrixOrigin)
        

    # ############################################################################
    # Matrix transformations methods
    # ############################################################################
    def completeM1(self, m):
        """
        Transform  matrixOrigin in matrixTransformed
        :param m              : Integer 
        result create matrixTransformed,
               update lowBoundcompletedM1,
               update m,
               update completedM1 = True
        """
        #------------------------------------------------------------------------
        #   INIT
        #------------------------------------------------------------------------
        proc = []               # work with processors list len(proc) <= m
        
        #------------------------------------------------------------------------
        #   matrixOrigin --> matrix
        #------------------------------------------------------------------------
        self.matrix = tools.matrix2dCopy(self.matrixOrigin)
        
        #------------------------------------------------------------------------
        # Scrolls through the "self.matrix" list to
        # fill in the processor load list "proc"
        #------------------------------------------------------------------------
        for i in range(len(self.matrix[0])):
            if (len(proc) < m):
                proc.append(float(self.matrix[0][i]))
            else:
                # sorts the proc list and fills in the first one which is the smallest.
                proc.sort()  
                proc[0] = float(proc[0]) + float(self.matrix[0][i])
            # end if    
        # end for

        #------------------------------------------------------------------------
        # sorts the matrix in the rerverse order.
        # The first element is the most loaded :
        # fill in the remain self.matrix to obtain same Cmax on all proc[x]
        #------------------------------------------------------------------------
        proc.sort(reverse=True)
        Cmax = proc[0]
        for i in range(len(proc)):
            if (i > 0):
                self.matrix[0].append(Cmax - proc[i])
            #end if
        # end for

        #------------------------------------------------------------------------
        #   Update self concerneds values
        #------------------------------------------------------------------------
        self.m                   = m              # update number of machines
        self.completedM1         = True # indicates that matrix is completed with m-1 jobs (to reach the optimal)
        self.lowBoundcompletedM1 = Cmax
                
        
                
                
        
        

        






        
