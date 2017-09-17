def complexNumberMultiply(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    a1,a2 = map(int,a[:-1].split('+'))
    b1,b2 = map(int,b[:-1].split('+'))
    return '{}+{}i'.format(a1*b1-a2*b2,a1*b2+a2*b1)

if __name__ == '__main__':
    a = "1+-1i"
    b = "1+-1i"
    res = complexNumberMultiply(a,b)
    print(res)