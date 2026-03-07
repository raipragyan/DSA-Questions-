from typing import List

class Solution:
    def search(self, k: int, arr: List[int]) -> int:
        # code here
        for i in range(len(arr)):
            if(k==arr[i]):
                return i+1
        return -1