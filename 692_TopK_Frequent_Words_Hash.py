

#count frequency of words and add words to heap to store the best k candidates 


class Solution: 

    def topKFrequent(self,words,k): 
        count = collections.Counter(words) 
        
        #list comprehension  
        #we use negative sign so that the heap puts the most frequent candidates on top  
       
        heap = [(-freq,word) for word,freq in count.items()]  
        
        #turn a list into a heap in linear time 
        heapq.heapify(heap) 
        
        #pop the heap for k times 
        return [heapq.heappop(heap)[1] for _ in xrange(k)] 
