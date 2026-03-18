class Solution:
    def isSorted(self, arr) -> bool:
        # code here
        a = arr.copy()
        a.sort()
        for i in range(len(a)):
            if (arr[i]!=a[i]):
                return False
        return True