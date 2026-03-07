#User function Template for python3

class Solution:
     def reverseString(self, s: str) -> str:
        # code here
        new = ""
        for i in range(len(s),0,-1):
            new = new + s[i-1]
            
        return new
            