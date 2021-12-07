# https://adventofcode.com/2021/day/5
# --- Day 5: Hydrothermal Venture - Part 1 ---


def get_line_points(p1, p2):
    startx = p1[0]
    starty = p1[1]
    endx = p2[0]
    endy = p2[1]
    flip = False

    if endx != startx and endy != starty:
        return []

    if endx == startx and endy == starty:
        return [p1]

    if endx == startx:
        flip = True
        startx, starty, endx, endy = starty, startx, endy, endx

    if startx > endx:
        startx, starty, endx, endy = endx, endy, startx, starty

    m = (endy - starty) / (endx - startx)
    b = starty - (m * startx)

    points = []
    for x in range(startx, endx + 1):
        y = (m * x) + b
        if float(round(y)) == y:
            points.append((x, round(y)) if not flip else (round(y), x))

    return points


lines = []
while inp := input():
    lines.append(get_line_points(*map(lambda x: (*map(int, x.split(",")),), inp.split(" -> ")), ))

points = {}
for line in lines:
    for point in line:
        points[point] = points.get(point, 0) + 1

print("***", sum(i > 1 for i in points.values()), "***")
