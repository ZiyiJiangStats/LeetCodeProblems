

class Solution: 
    def topKFrequent(self,words,k): 
        #count the frequency of each word 
        count = collections.Counter(words) 
        candidates = count.keys()  
        
        #sort the words 
        # we used a lambda function here 
        candidates.sort(key=lambda w:(-count[w],w)) 
        
        #take the best k of them 
        return candidate[:k]
