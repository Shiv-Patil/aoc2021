positions = [*map(int, input().split(","))]
positions.sort()
n = len(positions)
median = (round(sum(positions[n//2-1:n//2+1])/2), positions[n//2])[n % 2]
fuel = 0
for crab in positions:
    fuel += abs(crab-median)
print("***", fuel, "***")
