grid = []
while inp := input():
    grid.append([*map(int, inp)])
rows = len(grid)
cols = len(grid[0]) if rows else 0


def flash(grid, current, flashed, rows, cols):
    row, col = current
    flashed.append(current)
    grid[row][col] = 0
    adjacent = (
        (row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
        (row, col - 1), (row, col + 1),
        (row + 1, col - 1), (row + 1, col), (row + 1, col + 1),
    )
    adjacent = (*filter(lambda x: rows > x[0] >= 0 and cols > x[1] >= 0, adjacent),)
    for i in range(len(adjacent)):
        value = grid[adjacent[i][0]][adjacent[i][1]]
        if value >= 9 and adjacent[i] not in flashed:
            flash(grid, adjacent[i], flashed, rows, cols)
        elif adjacent[i] not in flashed:
            grid[adjacent[i][0]][adjacent[i][1]] += 1


steps = 0
while True:
    steps += 1
    flashed = []
    for row in range(rows):
        for col in range(cols):
            current = (row, col)
            if grid[row][col] >= 9 and current not in flashed:
                flash(grid, current, flashed, rows, cols)
            elif current not in flashed:
                grid[row][col] += 1
    if len(flashed) == rows*cols:
        break

print("***", steps, "***")
