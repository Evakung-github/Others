class Solution:
    def longestIncreasingPath(self, matrix):
        
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        
        seen =[[0 for i in range(n)] for j in range(m)]
        self.max_ = 0
        def search(r,c):
            
            if seen[r][c] >= 1:
                return seen[r][c]
            max_ = 1
            if matrix[r][c]<matrix[max(0,r-1)][c]:
                max_ = max(search(max(0,r-1),c)+1,max_)
            if matrix[r][c]<matrix[min(m-1,r+1)][c]:
                max_ = max(search(min(m-1,r+1),c)+1,max_)
            if matrix[r][c]<matrix[r][max(0,c-1)]:
                max_ = max(search(r,max(0,c-1))+1,max_)
            if matrix[r][c]<matrix[r][min(n-1,c+1)]:
                max_ = max(search(r,min(n-1,c+1))+1,max_)

            seen[r][c] = max_
            self.max_ = max(self.max_,max_)

            return max_
        
        for i in range(m):
            for j in range(n):
                if seen[i][j] < 1:
                    search(i,j)   
            
        
        return self.max_ 
