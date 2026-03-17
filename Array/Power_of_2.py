class Solution:
    def isPowerofTwo(self, n):
        # code here
        num = n
        if (n==1):
            return True
        if (n==0):
            return False
        if (n%2!=0):
            return False
        while(num!=1):
            if(num%2!=0):
                return False
            num = int(num/2)
        return True