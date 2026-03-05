class Solution:
    def minOperations(self, s: str) -> int:
        change1 = 0  # pattern starting with '0'
        change2 = 0  # pattern starting with '1'

        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] != '0':
                    change1 += 1
                if s[i] != '1':
                    change2 += 1
            else:
                if s[i] != '1':
                    change1 += 1
                if s[i] != '0':
                    change2 += 1

        return min(change1, change2)
