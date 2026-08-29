class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        islandCount = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    islandCount += 1
        return islandCount


    def dfs(self, grid: List[List[str]], r:int, c:int) -> None:
        if r < 0 or r >= len(grid) or c< 0 or c >= len(grid[0]) or grid[r][c] != '1':
            return
        grid[r][c] = "#"
        self.dfs(grid, r+1, c)
        self.dfs(grid, r-1, c)
        self.dfs(grid, r, c+1)
        self.dfs(grid, r, c-1)
            
                
        