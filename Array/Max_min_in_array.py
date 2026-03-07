class Solution:
    def getMinMax(self, arr):
        # code here
        min, max =arr[0],arr[0]
        for item in arr:
            if(item>max):
                max = item
            if (item<min):
                min  = item
        return min,max