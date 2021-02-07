"""
We want to do it in a way faster than O(nlogn) 

We can use a maxHeap
"""


import heapq

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        #we want to maintain a heap of size K 
        heap = []
        #heap is by default minheap in python 
        for (x, y) in points:
            #set it to negative. So the furthest points are stored on top of the heap
            #we pop all the furthest points and only keep the closest K points in the heap. Then flatten the heap to a list 
            dist = -(x*x + y*y)
            #if heap is full, we push the item onto the heap. We then pop and return the smallest item on the heap
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, x, y))
                
            # if not full, we keep push onto the heap 
            else:
                heapq.heappush(heap, (dist, x, y))
        
        return [(x,y) for (dist,x, y) in heap]
    
    # Time complexity O(NlogK),  space complexity O(K)
