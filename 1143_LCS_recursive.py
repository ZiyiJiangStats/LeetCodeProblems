   """
   Recursive solution 
   """
   
   class Solution:
        def longestCommonSubsequence(self, s1: str, s2: str) -> int:
            return self.helper(s1, s2, 0, 0)
         
         #We start by assigning i=0, j=0 
         #then we increment i,j by 1 every time we call the helper function again
        def helper(self, s1, s2, i, j):
            #if we reach the end of the string, there is no matching between the s1 and s2, return 0 
            if i == len(s1) or j == len(s2):
                return 0
            # if we have a match at current position, we increase the LCS value 
            if s1[i] == s2[j]:
                return 1 + self.helper(s1, s2, i + 1, j + 1)
               
            # if this is not a match, we move to the next character of either s1 or s2. 
            # We return the maximum of the two scenarios 
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
