import shuffling

class CostMatrix:
    # ###################################################################
    #
    #   PROERTIES
    #
    # ###################################################################
    
    # ===================================================================
    # MANAGEMENT
    # ===================================================================
    problemType     = ""    # P pour P||Cmax R pour R||Cmax
    
    # ===================================================================
    # GENERATION
    # ===================================================================
    generateMethode = ""    #  
    n               = 0     # Jobs number. n > 0
    m               = 0     # Machine number. 0 <= m < n. 0 if problemType = "P"
    Xtask           = 0     #
    Xmach           = 0     #

    # ===================================================================
    # HETERGENEITY PROPERTIES
    # ===================================================================
    mch             = 0
    tdh             = 0

    # ===================================================================
    # MATRIX    
    # Pij set.
    # [e1, e2, ... en]                              for problemType = "P"
    # [[e11, e12, ... e1n]...[em1, em2, ... emn]]   for problemType = "R"
    # ===================================================================
    matrix          = []    
    
    # ###################################################################
    #
    #   CONSTRUCTOR
    #
    # ###################################################################
    def __init__(self,probleme, generateMethode, n, m, xtask, xmach):
        self.problemType        = probleme
        self.generateMethode    = generateMethode
        self.n                  = n
        self.m                  = m
        self.Xtask              = xtask
        self.Xmach              = xmach
        self.matrix = []
        self.matrix = shuffling.shuffling(probleme, n,m,xtask, xmach)    
