import costMatrix

def main():
    n = int(input("n:"))
    m = int(input("m:"))
    mat = costMatrix.CostMatrix("P","",n,m,1,1)

    print(mat.problemType)
    print(mat.matrix)

# ######################################################
#             EXEC
# ######################################################
if __name__ == "__main__":
    main()
