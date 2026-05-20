class Solution:
    def findThePrefixCommonArray(self, A, B):
        n = len(A)
        
        seen = set()
        ans = []
        common = 0
        
        for i in range(n):
            # Process A[i]
            if A[i] in seen:
                common += 1
            else:
                seen.add(A[i])
            
            # Process B[i]
            if B[i] in seen:
                common += 1
            else:
                seen.add(B[i])
            
            ans.append(common)
        
        return ans
