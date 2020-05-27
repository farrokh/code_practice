class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        cp = np = []
        steps = 0
        for i,point in enumerate(points):
            cp = point
            if i+1<len(points):
                np = points[i+1]
                vtc = [np[0]-cp[0], np[1]-cp[1]]
                steps += max(abs(vtc[0]),abs(vtc[1]))
    
        return steps
            