from collections import defaultdict
def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """

    if len(s)==0 or numRows<=1:return s

    res = defaultdict(str)

    row = 0
    delta = 1

    for c in s:
    	res[row] += c
    	print(row,c)
    	row += delta
    	if row >= numRows:
    		row = numRows - 2
    		delta = -1
    	if row < 0:
    		row = 1
    		delta = 1


    return ''.join(res.values())




if __name__ == '__main__':
	s = "PAYPALISHIRING"
	rows = 4

	res = convert(s,rows)

	print(res)
        