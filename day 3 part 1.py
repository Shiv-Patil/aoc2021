# https://adventofcode.com/2021/day/3
# --- Day 3: Binary Diagnostic - Part 1 ---

inputs = []
gamma = ''
epsilon = ''

while inp := input():
    inputs.append(inp)

for _ in range(len(inputs[0])):
    lst = [k[_] for k in inputs]

    gamma += max(set(lst), key=lst.count)
    epsilon += min(set(lst), key=lst.count)

print("***", int(gamma, 2) * int(epsilon, 2), "***")
