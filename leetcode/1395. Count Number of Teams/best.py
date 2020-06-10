from bisect import bisect

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        def insert(x):
            i = bisect(tmp, x)
            tmp.insert(i, x)
            return i

        tmp = []
        l = list(map(insert, rating))

        tmp = []
        g = list(map(insert, rating[::-1]))
        g.reverse()
        
        counter = 0
        
        length1 = len(rating)
        length2 = length1 - 1

        
        
        for i in range(length1):
            counter += l[i] * (length2 - i - g[i])
            counter += g[i] * (i - l[i])
            
        return counter
