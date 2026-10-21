class Solution:
    def minOperations(self, s: str) -> int:
        if s == ''.join(sorted(s)):
            return 0

        if len(s) == 2:
            return -1

        if s[0] == min(s) or s[-1] == max(s):
            return 1

        if s.count(max(s)) == 1 and s.count(min(s)) == 1:
            if s[0] == max(s) and s[-1] == min(s):
                return 3

        return 2
