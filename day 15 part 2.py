grid = []
while inp := input():
    grid.append(list(map(int, inp)))

rows = len(grid)
cols = len(grid[0])
points = [(row, col, grid[row][col]) for row in range(rows) for col in range(cols)]
grid = [[0 for i in range(cols*5)] for j in range(rows*5)]
for _row, _col in [(i // 5, i % 5) for i in range(25)]:
    for __row, __col, risk in points:
        grid[__row + _row * rows][__col + _col * cols] = ((risk - 1 + _row + _col) % 9) + 1

rows = len(grid)
cols = len(grid[0])
cost = 0
caves = [(0, 0, cost)]
visited = set()
running = True
while len(caves) and running:
    caves.sort(key=lambda el: el[2])
    _row, _col, cost = caves.pop(0)
    adjacent = (
        (_row - 1, _col),
        (_row, _col - 1), (_row, _col + 1),
        (_row + 1, _col)
    )
    adjacent = (*filter(lambda el: rows > el[0] >= 0 and cols > el[1] >= 0, adjacent),)
    for row, col in adjacent:
        if row == rows - 1 and col == cols - 1:
            cost += int(grid[row][col])
            running = False
            break
        if (row, col) not in visited:
            visited.add((row, col))
            caves.append((row, col, cost+grid[row][col]))

print(cost)
