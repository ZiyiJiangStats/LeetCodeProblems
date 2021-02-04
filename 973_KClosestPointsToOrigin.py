
#Sort 

class Solution: 
    def kClosest(self,points,k): 
        #sort the list of points based on the euclidean distance to the origin 
        points.sort(key = lambda p:p[0]**2 + p[1]**2)  
        return points[:k] 

    
#Time Complexity O(nlogn),   space complexity O(n)
