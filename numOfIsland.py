def numberOFIslands(grid):
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    number_of_islands = 0

    def bfs(r, c):
        queue = [(r,c)]

        grid[r][c] = '0'
        while queue:
            row, col = queue.pop(0)
            for dr, dc in [(0,1), (1,0), (0,-1), (-1, 0)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                    queue.append((nr, nc))
                    grid[nr][nc] = '0'
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                number_of_islands += 1
                bfs(r,c)
    return number_of_islands

grid = [
  ['1','1','0','0','0'],
  ['1','1','0','0','0'],
  ['0','0','1','0','0'],
  ['0','0','0','1','1']
]

print(numberOFIslands(grid))