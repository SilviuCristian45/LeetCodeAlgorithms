def num_of_paths_to_dest(n):
    memoization = [ [-1] * (n+1) for _ in range(n+2)]
    print(memoization)
    def traverse(i, j):
        if i < 0 or j < 0 or i > n-1 or j > n-1:
            return 0
        if j == 0:
            return 1
        if i + j >= n-1:
            return 0
        #print(i, j)
        #print(i+1, j, " ", i, j-1)
        if memoization[i][j] != -1: 
            return memoization[i][j] 
        fromNorth= traverse(i+1, j)
        fromEast = traverse(i, j-1)

        memoization[i][j] = fromNorth + fromEast

        return memoization[i][j]
    n+=1
    return traverse(0, n-2)
    
res = num_of_paths_to_dest(4)
print(res)