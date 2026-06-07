class Solution:
    def reverseBits(self, n: int) -> int:
        binary = str(bin(n))[2:]
        binary = binary[::-1]
        for i in range(len(binary), 32):
            binary += '0'
        
        return int(binary, 2)