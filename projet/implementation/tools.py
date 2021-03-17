def matrix2dCopy(source):
    target = []
    row = []
    
    for i in range(len(source)):
        row = []
        for j in range(len(source[i])):
           row.append(source[i][j])
        # end for
        target.append(row)
    # end for
    return target
        
def matrix1dCopy(source):
    target = []
    for i in range(len(source)):
        target.append(source[i])
    # end for
    return target
