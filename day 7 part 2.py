positions = [*map(int, input().split(","))]
n = len(positions)
mean_floor = sum(positions) // n
mean_ceil = -(-sum(positions) // n)
fuel1 = 0
fuel2 = 0
for crab in positions:
    move1 = abs(mean_floor - crab)
    fuel1 += round((move1 / 2) * (move1 + 1))
    move2 = abs(mean_ceil - crab)
    fuel2 += round((move2 / 2) * (move2 + 1))

print("***", min(fuel1, fuel2), "***")
