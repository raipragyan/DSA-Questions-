class Solution:
    def findSum(self, n):
        # code here
        sum = 0
        for i in range(n+1):
            sum = sum+i
        return sum
    