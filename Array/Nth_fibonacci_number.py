class Solution:
    def nthFibonacci(self, n: int) -> int:
        # code here
        def fib(i):
            if (i==0):
                return 0
            elif (i==1):
                return 1
            else:
                return fib(i-1) + fib(i-2)
        return fib(n)