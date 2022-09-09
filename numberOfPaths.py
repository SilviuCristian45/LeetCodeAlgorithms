def num_of_paths_to_dest(n):
    def numberOfPaths(m, nn):
        if(m == 1 or nn == 1):
            return 1
        return numberOfPaths(m-1, nn) + numberOfPaths(m, nn-1)
    return numberOfPaths(n, n)
    
res = num_of_paths_to_dest(4)
print(res)