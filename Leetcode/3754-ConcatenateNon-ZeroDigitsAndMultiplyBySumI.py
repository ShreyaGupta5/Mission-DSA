class Solution:
    def sumAndMultiply(self, n: int) -> int:
        place = 1
        x = 0
        digit_sum = 0

        while n > 0:
            digit = n % 10
            if digit != 0:
                x += digit * place
                place *= 10
                digit_sum += digit
            n //= 10

        return x * digit_sum
