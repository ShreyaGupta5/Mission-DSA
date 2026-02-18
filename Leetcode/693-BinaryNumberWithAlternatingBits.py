class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = n % 2
        n //= 2
        
        while n:
            curr = n % 2
            if curr == prev:
                return False
            prev = curr
            n //= 2
        
        return True
