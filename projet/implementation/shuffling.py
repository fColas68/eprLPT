# to use gamma function
import numpy as np

def shuffling(matrixprobleme,n,m,Vtask, Vmach):
    instance_tasks_weight = []
    instance_machine_row = []
    
    # ==================================================
    # Generate  instance_tasks_weight with gamma distribution
    # ==================================================
    for i in range(n):
        # ----------------------------------------------
        # GAMMA value with Vtask bound
        # ----------------------------------------------
        wi = np.random.gamma(1,1)
        
        # ----------------------------------------------
        # Construct ist
        # ----------------------------------------------
        instance_machine_row.append(wi)
        
    return instance_machine_row
    
