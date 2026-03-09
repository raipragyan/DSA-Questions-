class Solution:
    def leaders(self, arr):
        # code here
        res=[]
        m_n=arr[-1]
        for i in range(len(arr)-1,-1,-1):
            if arr[i]>=m_n:
                m_n=arr[i]
                res.append(arr[i])
        return res[::-1]