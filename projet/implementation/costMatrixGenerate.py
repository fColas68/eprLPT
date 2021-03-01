# to use distributions
import numpy
import random


# ############################################################################
# P problem matrix (Origin) generation
# ############################################################################
def uniform_p(n,a,b):
    # ========================================================================
    matrix = []
    matrixProc = []
    
    # ========================================================================
    for i in range(n):
        rand = random.uniform(a,b)
        matrixProc.append(rand)
    matrix.append(matrixProc)
    return matrix

def non_uniform_p(n,a,b):
    # ========================================================================
    matrix = []
    matrixProc = []
    #
    n98 = int((98*n) / 100)
    a1 = 0.9*(b-a)
    b1 = b
    a2 = a
    b2 = 0.2*(b-a)
    # ========================================================================
    for i in range(n98):
        rand = random.uniform(a1,b1)
        matrixProc.append(rand)
        
    for i in range(n-n98):
        rand = random.uniform(a2,b2)
        matrixProc.append(rand)
        
    matrix.append(matrixProc)
    return matrix

def gamma_p(n,alpha,beta):
    # ========================================================================
    matrix = []
    matrixProc = []
    #
    # ========================================================================
    for i in range(n):
        rand = random.gammavariate(alpha,beta)
        matrixProc.append(rand)
    matrix.append(matrixProc)
    return matrix

def beta_p(n,alpha):
    """
    beta allways 1 for this set
    """
    # ========================================================================
    matrix = []
    matrixProc = []
    #
    # ========================================================================
    for i in range(n):
        rand = random.betavariate(alpha,1)
        matrixProc.append(rand)
    matrix.append(matrixProc)
    return matrix

def exponential_p(n,lambd):
    # ========================================================================
    matrix = []
    matrixProc = []
    #
    # ========================================================================
    for i in range(n):
        rand = random.expovariate(lambd)
        matrixProc.append(rand)
    matrix.append(matrixProc)
    return matrix

def real_p():
    # ========================================================================
    matrix = []
    matrixProc = []
    
    return matrix
