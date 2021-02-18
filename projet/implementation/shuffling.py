# for the parameters
import sys, getopt

# to use gamma function
import numpy as nm

# ######################################################
#             MAIN
# ######################################################
def main(argv):
    n=0
    m=0
    Vtask=0
    Vmach=0
    output_dir = ""

    # ==================================================
    # Parses Parameters
    # ==================================================
    try:
        opts, args = getopt.getopt(argv,"h:d:n:m:t:p:",["output_dir=","n=","m=","Vtask=","Vmach="])
        
    except getopt.GetoptError:
        print ("shuffling.py -h")
        print("or")
        print ("shuffling.py -d <directory generation> -n <jobs number> -m <machines number> -t <Vtask parameter> -p <Vmach parameter>")
        sys.exit(2)

    # ==================================================
    # Retrieve Parameters
    # ==================================================
    for opt, arg in opts:
        # ----------------------------------------------
        # AIDE
        # ----------------------------------------------
        if opt == '-h':
            print ("shuffling.py -d <directory generation> -n <jobs number> -m <machines number> -t <Vtask parameter> -p <Vmach parameter>")
            sys.exit()
        # ----------------------------------------------
        # DIRECTORY OF INSTANCE GENERATION CSV
        # ----------------------------------------------
        elif opt in ("-d", "--output_dir"):
            output_dir = arg
        # ----------------------------------------------
        # N and M
        # ----------------------------------------------
        elif opt in ("-n", "--n"):
            n = arg
        elif opt in ("-m", "--m"):
            m = arg
        # ----------------------------------------------
        # Vtask and Vmach
        # ----------------------------------------------
        elif opt in ("-t", "--Vtask"):
            Vtask = arg
        elif opt in ("-p", "--Vmach"):
            Vmach = arg

    # ----------------------------------------------
    # PARAMETERS NUMBER. Must be 6.
    # Shuffling.py and 5 others parameters 
    # ----------------------------------------------
    if (len(sys.argv)!=6):
        print ("shuffling.py -h")
        print("or")
        print ("shuffling.py -d <directory generation> -n <jobs number> -m <machines number> -t <Vtask parameter> -p <Vmach parameter>")
        sys.exit(2)

    # ==================================================
    # CALL SHUFFLING FUNCTION
    # ==================================================
    instance = shuffling(n,m,Vtask, Vmach)

    # ==================================================
    # PREPARE HEADER
    # ==================================================
    # header = header(instance)

    # ==================================================
    # WRITE File CSV 
    # ==================================================
    
           
# ######################################################
#
#             SHUFFLING FUNCTION
#
# ######################################################
# INPUT
# n
# m     if m = 1 then all Bj are = 1
# Vtask
# Vmach
# OUTPU
# n*m cost matrix (list of lists)
def shuffling(n,m,Vtask,Vmach):
    instance = []
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
        instance_tasks_weight.append(wi)
    
        
    
    
   

# ######################################################
#             EXEC
# ######################################################
if __name__ == "__main__":
    main(sys.argv[1:])

