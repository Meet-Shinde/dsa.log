#My approach: 
#Couldnt think of an approach.

#Optimal solution: (Using recursion.)
class Solution:
    def floodFill(image, sr, sc, color):
        m, n=len(image), len(image[0])
        start_color=image[sr][sc]
        if start_color==color:
            return image
        def dfs(i, j):
            if i<0 or i>=m or j<0 or j>=n or \
            start_color!=image[i][j]:
                return
            image[i][j]=color
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
        dfs(sr, sc)
        return image

'''Note: Make your basics stronger.'''