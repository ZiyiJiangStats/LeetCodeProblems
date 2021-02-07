class Solution:
    def kClosest(self, points, K):
        #we want to partially sort the list of points by the distance. We only want the K closest points 
        self.sort(points, 0, len(points)-1, K)
        #return the closest k points 
        return points[:K]
    
    #sort l to r points 
    def sort(self, points, l, r, K):
        if l < r:
            p = self.partition(points, l, r)
            if p == K:
                return
            elif p < K:
                self.sort(points, p+1, r, K)
            else:
                self.sort(points, l, p-1, K)
      
    #return a pivot 
    def partition(self, points, l, r):
        pivot = points[r]
        a = l
        for i in range(l, r):
            if (points[i][0]**2 + points[i][1]**2) <= (pivot[0]**2 + pivot[1]**2):
                points[a], points[i] = points[i], points[a]
                a += 1
        points[a], points[r] = points[r], points[a]                
        return a
