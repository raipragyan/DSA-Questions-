#User function Template for python3

class Solution:
    def evenlyDivides(self, n):
        # code here
        num = n
        count = 0
        while (num!=0):
            rem = num % 10
            if (rem!=0 and n%rem==0):
                count += 1
            num = int(num/10)
        return count