class Solution:
    def largest(self, arr):
        # code here
        max = 0
        for item in arr:
           if (item > max):
               max = item
        return max