def countArrangement(N):
    """
    :type N: int
    :rtype: int
    """
    cache = {}

    def helper(i, X):
        if i==1:
            return 1
        key = (i,X)
        total = 0
        if key in cache:
            return cache[key]
        for j in range(len(X)):
            if X[j]%i==0 or i%X[j]==0:
                total += helper(i-1,X[:j]+X[j+1:])
        cache[key] = total
        return total
    return helper(N,tuple(range(1,N+1)))



if __name__ == '__main__':
    N = 4
    res = countArrangement(N)
    print(res)
