
# Return even elements followed by odd elements 

#Solution 1 : use built in function sort 
class Solution(object):
    def sortArrayByParity(self, A):
        A.sort(key = lambda x: x % 2)
        return A
      
      
#Time complexity O(NlogN), space complexity O(N) 



#Solution 2: Two pass 

class Solution(object):
    def sortArrayByParity(self, A):
        return ([x for x in A if x % 2 == 0] +  [x for x in A if x % 2 == 1])
      
      
     #Time complexity O(N), space complexity O(N)
    

#Solution 3: In Place 

"""
We want to use quickSort to do sort in place 

We maintain two pointers i and j 

all the elements below i are even 
all the elements above i are odd 

"""
class Solution(object):
    def sortArrayByParity(self, A):
        #set i to the first element; j to the last element 
        i, j = 0, len(A) - 1
        # the loop ends if j<= i 
        while i < j:
            # if A[i] is odd and A[j] is even 
            # we do the swap  
            if A[i] % 2 > A[j] % 2:
                A[i], A[j] = A[j], A[i]
            
            #keep increasing i and decreasing j 
            if A[i] % 2 == 0: i += 1
            if A[j] % 2 == 1: j -= 1

        return A

#Time Complexity: O(N) , Space Complexity O(1) 
