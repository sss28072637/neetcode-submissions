class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}

        def dfs(n):
            if n <= 2:
                return n
            if n in mem:
                return mem[n]

            mem[n] = dfs(n-1)+dfs(n-2)
            return mem[n]

        return dfs(n)