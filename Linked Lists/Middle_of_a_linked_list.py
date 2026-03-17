'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''

class Solution:
    def getMiddle(self, head):
        # code here
        curr = head
        count = 0
        while curr!=None:
            curr = curr.next
            count += 1
        i = 1
        curr = head
        while (i<(int(count/2)+1)):
            curr = curr.next
            i += 1
        return curr.data