class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting_color = image[sr][sc]
        visits = [[True for _ in range(len(image[0]))] for _ in range(len(image))]
        self.dfs(image, sr, sc, color, starting_color, visits)
        print(visits)
        return image
    
    
    def dfs(self, image, sr, sc, color, starting_color, visits):
        if image[sr][sc]!=starting_color:
            return
        image[sr][sc] = color
        visits[sr][sc] = False
        if 1<=sr and visits[sr-1][sc]:
            self.dfs(image, sr-1, sc, color, starting_color, visits)
        if sr+1<len(image) and visits[sr+1][sc]:
            self.dfs(image, sr+1, sc, color, starting_color, visits)
        if sc+1<len(image[0]) and visits[sr][sc+1]:
            self.dfs(image, sr, sc+1, color, starting_color, visits)
        if 1<=sc and visits[sr][sc-1]:
            self.dfs(image, sr, sc-1, color, starting_color, visits)
        
        