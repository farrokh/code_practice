class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = [*range(1,m+1)]
        output= []
        for i in range(len(queries)):
            currentInt = queries[i]
            getIndex = P.index(currentInt)
            output.append(getIndex)
            P.remove(currentInt)
            P.insert(0,currentInt)
        return output