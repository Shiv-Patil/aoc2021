inp = input()[15:].split(", ")
target_x = (*map(int, inp[0].split("..")),)
target_y = (*map(int, inp[1][2:].split("..")),)
x1, x2, y1, y2 = min(target_x), max(target_x), min(target_y), max(target_y)


def does_reach(vel_x, vel_y, x1, x2, y1, y2):
    x = y = 0
    while y > y1:
        x += (vel_x := vel_x - 1 if vel_x > 0 else vel_x)
        y += (vel_y := vel_y - 1)
        if x1 <= x <= x2 and y1 <= y <= y2:
            return 1
    return 0


print("***",
      sum(does_reach(vel_x, vel_y, x1, x2, y1, y2) for vel_x in range(1, x2 + 2) for vel_y in range(y1, -y1 + 1)),
      "***")
