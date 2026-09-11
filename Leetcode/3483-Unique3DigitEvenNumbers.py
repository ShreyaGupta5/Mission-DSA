class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = 0

        for a in range(1, 10):
            for b in range(10):
                for c in range(0, 10, 2):

                    num = [a, b, c]

                    temp = digits.copy()

                    possible = True

                    for digit in num:
                        if digit in temp:
                            temp.remove(digit)
                        else:
                            possible = False
                            break

                    if possible:
                        count += 1

        return count
