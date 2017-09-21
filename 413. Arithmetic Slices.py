def numberOfArithmeticSlices(A):
    """
    :type A: List[int]
    :rtype: int
    """

    curr = 0
    sum = 0
    for i in range(2,len(A)):
        if A[i]-A[i-1] == A[i-1]-A[i-2]:
            curr += 1
            sum += curr
        else:
            curr = 0
    return sum

if __name__ == '__main__':
    A = [1,2,3,4]
    res = numberOfArithmeticSlices(A)
    print(res)
