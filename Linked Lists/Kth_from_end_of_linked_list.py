'''
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
class Solution:
    def getKthFromLast(self, head, k):
        #code here
        curr = head
        count = 0
        while (curr!=None):
            curr = curr.next
            count += 1
        if(k>count):
            return -1
        n = count - k
        curr = head
        num = 0
        if n==0:
            return head.data
        for i in range(1,n+1):
            curr = curr.next
            num = curr
        return num.data
