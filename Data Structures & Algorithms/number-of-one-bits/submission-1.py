class Solution:
    def hammingWeight(self, n: int) -> int:
        # return str(bin(n)).count('1')
        res = 0
        for i in range(32):
            if (1 << i) & n:
                res += 1
        
        return res