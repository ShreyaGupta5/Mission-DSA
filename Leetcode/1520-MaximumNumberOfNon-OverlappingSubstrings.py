class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # Step 1: Record the first and last occurrence of each character
        fst = {c: len(s) - 1 - i for i, c in enumerate(s[::-1])}
        lst = {c: i for i, c in enumerate(s)}
        
        intervals = []
        # Step 2: Find valid substring intervals for each character
        for c in set(s):
            beg, end = fst[c], lst[c]
            bad, idx = False, beg
            while idx <= end:
                # Expand the interval if a character inside has an earlier start
                end = max(end, lst[s[idx]])
                if fst[s[idx]] < beg:
                    bad = True
                    break
                idx += 1
            if not bad:
                intervals.append((end, beg))
                
        # Step 3: Greedy interval scheduling (sort by end time)
        ans, prev = [], -1
        for end, beg in sorted(intervals):
            if beg > prev:
                ans.append(s[beg:end + 1])
                prev = end
                
        return ans
