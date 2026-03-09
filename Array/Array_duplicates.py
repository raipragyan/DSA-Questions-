class Solution:
    def findDuplicates(self, arr):
        # code here
        duplicates = set()
        seen = set()
        for num in arr:
            if num in seen:
                duplicates.add(num)
            else:
                seen.add(num)
        return list(duplicates)
        