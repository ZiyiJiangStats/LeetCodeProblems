

#Bottom up dynamic programming 


class Solution: 
    
    def longestCommonSubsequence(self,s1:str,s2:str) -> int : 
        m = len(s1) 
        n = len(s2) 
        memo = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for row in range(1,m+1): 
            for col in range(1,n+1): 
                if s1[row-1] == s2[col-1]: 
                    memo[row][col]= 1+ memo[row-1][col-1] 
                else: 
                    memo[row][col] = max(memo[row][col-1],memo[row-1][col]) 
         
         return memo[m][n] 

      # Time complexity O(mn),   space complexity: O(mn) 
    
    
    #Reduced space complexity 
    
    
class Solution: 
    def longestCommonSubsequence(self,s1:str, s2:str) -> int: 
        m = len(s1) 
        n = len(s2) 
        if m<n: 
            return self.longestCommonSubsequence(s2,s1) 
        
        memo = [[0 for _ in range(n+1)] for _ in range(2)]
        
        for i in range(m): 
            for j in range(n): 
                if s1[i] == s2[j]: 
                    memo[1-i%2][j+1] = 1 + memo[i%2][j] 
                    
                 else: 
                    memo[1-i%2][j+1] = max(memo[1-i%2][j],memo[i%2][j+1])
                    
         return memo[m%2][n]
                    
     # time complexity O(mn),   space complexity O(min(m,n))            
        
