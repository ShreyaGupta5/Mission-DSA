class Solution:
    def separateDigits(self, nums):
        result = []
        
        for num in nums:
            # Convert number into string and add each digit
            for digit in str(num):
                result.append(int(digit))
        
        return result
