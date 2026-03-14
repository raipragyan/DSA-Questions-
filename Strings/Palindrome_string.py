class Solution:
    def isPalindrome(self, s):
        # code here
        if s[::-1]==s:
            return True
        else:
            return False