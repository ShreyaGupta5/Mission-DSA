class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # If the requested sum is too large to fit in 'num' digits, it's impossible
        if sum > 9 * num:
            return ""
        
        # Calculate how many 9s we can optimally place
        nines = sum // 9
        
        # Calculate the single leftover digit
        remainder = sum % 9
        
        # Build the greedy string pattern
        ans = "9" * nines
        if remainder > 0:
            ans += str(remainder)
            
        # Pad the rest of the string with zeros to match 'num' length
        ans += "0" * (num - len(ans))
        
        return ans
