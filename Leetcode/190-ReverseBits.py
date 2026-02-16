class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        
        for _ in range(32):
            result = result << 1      # Shift result left
            result = result | (n & 1) # Add last bit of n
            n = n >> 1               # Shift n right
        
        return result
