class Solution:    
    def findUnion(self, a, b):
        # code here
        new = a+b
        removed = set(new)
        return removed