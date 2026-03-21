class Solution:
    def findKRotation(self, arr):
        # code here
        b = arr.copy()
        b.sort()
        first = b[0]
        for i in range(len(arr)):
            if (arr[i]==first):
                return 