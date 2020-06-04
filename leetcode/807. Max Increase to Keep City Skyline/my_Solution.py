class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        topBottom = {}
        leftRight = []
        
        for i in grid:
            for indJ,j in enumerate(i):
                if indJ in topBottom:
                    if topBottom[indJ] < j:
                        topBottom[indJ] = j
                else:
                    topBottom[indJ] = j
                    
            leftRight.append(max(i))

        topBottom = list(topBottom.values())
        sum = 0
        for indI,i in enumerate(grid):
            for indJ,j in enumerate(i):
                sum += min(topBottom[indJ],leftRight[indI]) - j
        return sum