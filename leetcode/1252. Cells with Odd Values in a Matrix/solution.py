# https://medium.com/@donic0211/leetcode-1252-cells-with-odd-values-in-a-matrix-2742ec4cffa5
class Solution:
    def oddCells(self, n, m, indices):
        count=0
        matrix=[[0]*m for i in range(n)]
        for c in indices:
            x,y=c[0],c[1]
            for i in range(m):
                matrix[x][i]+=1
            for j in range(n):
                matrix[j][y]+=1
        for i in range(n):
            for j in range(m):
                if matrix[i][j] % 2 !=0:
                    count+=1
        return count