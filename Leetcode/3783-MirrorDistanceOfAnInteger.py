class Solution:
    def mirrorDistance(self, n: int) -> int:
        # Convert integer to string, reverse it, and convert back to int
        reversed_n = int(str(n)[::-1])
        # Return the absolute difference
        return abs(n - reversed_n)
