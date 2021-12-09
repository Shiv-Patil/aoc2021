locations = []
while inp := input():
    locations.append((10, *map(int, inp), 10))
cols = len(locations[0])
rows = len(locations)
locations += [(10,)*cols, (10,)*cols]
locations.insert(0, (10,)*cols)

sum = 0
for row in range(1, rows+1):
    for el in range(1, cols-1):
        current = locations[row][el]
        left = locations[row][el-1]
        right = locations[row][el+1]
        top = locations[row-1][el]
        bottom = locations[row+1][el]
        if all([current < x for x in (left, right, top, bottom)]):
            sum += current+1

print(sum)
