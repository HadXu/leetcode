class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = cur = ListNode(0)
        carry = 0
       	while l1 or l2 or carry:
       		if l1:
       			carry += l1.val
       			l1 = l1.next
       		if l2:
       			carry += l2.val
       			l2 = l2.next
       		carry,val = divmod(carry,10)
       		cur.next = ListNode(val)
       		cur = cur.next
       	return dummy.next

if __name__ == '__main__':
	l1 = ListNode(2)
	l2 = ListNode(3)
	l1.next = l2
	l3 = ListNode(4)
	l2.next = l3
	s = Solution()
	res = s.addTwoNumbers(l1,l1)
	while res:
		print(res.val)
		res = res.next