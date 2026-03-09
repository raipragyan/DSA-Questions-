class Solution:
    def findTwoElement(self, arr):
        # code here
        arr.sort()
        for i in range(len(arr)-1):
            if(arr[i]==arr[i+1]):
                repeat = arr[i]
                break
        arr = set(arr)
        new = list(arr)
        new.sort()
        for i in range(1,len(new)+2):
            if i not in arr:
                miss = i
                break
            else:
                miss = i+2
        return repeat, miss