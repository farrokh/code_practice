class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        #set the p aray:
        #go through the lst and find each item at loop index
        #lookup the item in the p array
        #return the indext of the item in p array
        #store it in a new list
        #move that item in p to the beginning of the p array
        
        p = [i for i in range(1,m+1)]  #more pythonic p = [*range(1,m+1)]!
        result = []
        for item in queries:
            pIndex = p.index(item)
            result.append(pIndex)
            del p[pIndex]
            p.insert(0, item) 
            
        return result