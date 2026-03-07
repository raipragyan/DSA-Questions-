class Solution:
    def search(self, arr, x):
        # code here
        count = 0
        for i in range(len(arr)):
            if(arr[i]==x):
                count = count+1
                return i
                break
        return -1