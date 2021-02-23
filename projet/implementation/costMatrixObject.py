// Costs matricies generators library
import costMatrixGenerate

class CostMatrix:
    """
    CostMatrix manage costs matrix. 
    Managment properties ------------------------------------------------------
    :param problemType    : String. Define problem type P(default) for P||Cmax R for P||Cmax 
    Generation properties -----------------------------------------------------
    :param generateMethode: STRING describe how this matrix is generated.
                            SHUFFLING,   (Vtask = VMutask, Vmach = VMumach / Shuffling method)
                            NOISE1,      (Vtask = VMutask, Vmach = VMumach / first approch to set noise)
                            NOISE2,      (Vtask = MuVtask, Vmach = MuVmach / Decond approch to set noise)
                            UNIFORM,     (Vtask = a, Vmach = b / uniform instencies generation LORI and MARTELLO)
                            NON_UNIFORM, (Vtask = a, Vmach = b / non uniform instencies generation LORI and MARTELLO)
                            REEL         (from workload archive - www.cs.huji.ac.il/labs/parallel/workload)
    :param n              : Integer Jobs number. n > 0
    :param m              : Integer Machine number. 0 <= m < n. 0 if problemType = "P"
    :param Vtask          : Parameter 1 for heterogeneity tasks
    :param Vmach          : Parameter 2 for heterogeneity machines
    :param noise          : Only if generateMethode ="NOISE1" or "NOISE1". noise factor
    Heterogeneity properties comuted -------------------------------------------
    :param mch            : real. non intuitives measures : Machine Performance Homogeneity
    :param tdh            : real. non intuitives measures : Task Difficulty Homogeneity
    :param VMutask        : real. intuitives measures : CV of means tasks 
    :param MuVtask        : real. intuitives measures : mean of CVs tasks
    :param VMumach        : real. intuitives measures : CV of means machines 
    :param MuVmach        : real. intuitives measures : mean of CVs machines
    :param skewness       : real. futur : skewness factor
    :param kurtosis       : real. futur : kurtosis factor
    Matricies --------------------------------------------------------------------
    :param matrix         : double matrix. Pij set of costs
                            [[e1, e2, ... en]]
                            [[e11, e12, ... e1n]...[em1, em2, ... emn]]   for problemType = "R"
    :param matrixResults  : matrix.
                            [(ALGORITHM1, computed makespan, comutation time, resultMatrix []),...,(ALGORITHMn, computed makespan, comutation time, resultMatrix [])]
    :return: 
    """
    problemType     = ""
    #
    generateMethode = ""
    n               = 0
    m               = 0
    Vtask           = 0
    Vmach           = 0
    noise           = 0
    #
    mch             = 0
    tdh             = 0
    VMutask         = 0
    MuVtask         = 0
    VMumach         = 0
    MuVmach         = 0
    skewness        = 0
    kurtosis        = 0
    #
    matrix          = []
    matrixResults   = []

    
    def __init__(self,probleme, generateMethode, n, Vtask, Vmach, m = 0, noise=0):
        self.problemType        = probleme
        self.generateMethode    = generateMethode
        self.n                  = n
        self.m                  = m
        self.Vtask              = Vtask # MuVtask or VMutask or a
        self.Vmach              = Vmach # MuVmach or VMumach or b
        self.matrix = []
        self.matrixResults = []
        # self.matrix generation
        
        if (self.problemType) == "P":
            # UNIFORM : Uniform distribution
            if (self.generateMethode == "UNIFORM"):
                self.matrix = costMatrixGenerate.uniform(n,a, b)
            # NON_UNIFORM : Non uniform distribution
            elif (self.generateMethode == "NON_UNIFORM"):
                self.matrix = costMatrixGenerate.non_uniform(n,a, b)
            # REEL : Reel, According the "parallel work load archive"
            # elif (self.generateMethode == "REEL"):
            else:
                self.matrix = costMatrixGenerate.reel_p(n,xtask, xmach)
        #----------------------------------------------------------------
        #   R Problem
        #----------------------------------------------------------------
        elif (self.problemType) == "R":
            # SHUFFLING : Shuffling algorythm
            if (self.generateMethode == "SHUFFLING"):
                self.matrix = matrixGenerateshuffling.shuffling(n,m,xtask, xmach)
            # NOISE : Shuffling algorythm
            elif (self.generateMethode == "NOISE"):
                self.matrix = matrixGenerateshuffling.noise(n,m,xtask, xmach)
            # REEL : Reel, According the "parallel work load archive"
            # elif (self.generateMethode == "REEL"):
            else:
                self.matrix = costMatrixGenerate.reel_r(n,m,xtask, xmach)
