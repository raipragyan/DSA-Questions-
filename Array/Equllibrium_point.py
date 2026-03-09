class Solution:
    def findEquilibrium(self, arr):
        # code here
        sum = 0
        for item in arr:
            sum = sum + item
        newsum = 0
        for i in range(len(arr)):
            if (sum-newsum-arr[i] == newsum):
                return i
            newsum = newsum + arr[i]
        return -1