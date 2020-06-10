class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = collections.deque(range(1, m + 1))
        ret = list()
        
        for q in queries:
            p = P.index(q)
            del P[p]
            P.appendleft(q)
            ret.append(p)
        
        return ret