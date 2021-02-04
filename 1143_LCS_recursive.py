   """
   Recursive solution 
   """
   
   class Solution:
        def longestCommonSubsequence(self, s1: str, s2: str) -> int:
            return self.helper(s1, s2, 0, 0)
            
        def helper(self, s1, s2, i, j):
            if i == len(s1) or j == len(s2):
                return 0
            if s1[i] == s2[j]:
                return 1 + self.helper(s1, s2, i + 1, j + 1)
            else:
                return max(self.helper(s1, s2, i+1, j), self.helper(s1, s2, i, j + 1))

               
               
               
     #memoization    
         
    class Solution:
        def longestCommonSubsequence(self, s1: str, s2: str) -> int:
            m = len(s1)
            n = len(s2)
            memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
            return self.helper(s1, s2, 0, 0, memo)
    
        def helper(self, s1, s2, i, j, memo):
            if memo[i][j] < 0:
                if i == len(s1) or j == len(s2):
                    memo[i][j] = 0
                elif s1[i] == s2[j]:
                    memo[i][j] = 1 + self.helper(s1, s2, i + 1, j + 1, memo)
                else:
                    memo[i][j] = max(
                        self.helper(s1, s2, i + 1, j, memo),
                        self.helper(s1, s2, i, j + 1, memo),
                    )
            return memo[i][j]
