locations = []
while inp := input():
    locations.append(('9' + inp + '9'))
cols = len(locations[0])
locations.append('9' * cols)
locations.insert(0, '9' * cols)
rows = len(locations)


def get_connected_points(connected, grid, _row, _col, sep):
    left = (_row, _col - 1)
    right = (_row, _col + 1)
    top = (_row - 1, _col)
    bottom = (_row + 1, _col)
    for connection in filter(lambda x: x not in connected and grid[x[0]][x[1]] != sep, (left, right, top, bottom)):
        connected.append(connection)
        get_connected_points(connected, grid, connection[0], connection[1], sep)
    return connected


basins = []
for row in range(1, rows-1):
    for col in range(1, cols-1):
        current = (row, col)
        if locations[row][col] != '9' and current not in [j for sub in basins for j in sub]:
            basins.append(get_connected_points([current], locations, row, col, '9'))

sizes = sorted(map(len, basins))
print("***", sizes[-1]*sizes[-2]*sizes[-3], "***")
