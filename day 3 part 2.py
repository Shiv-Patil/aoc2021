# https://adventofcode.com/2021/day/3
# --- Day 3: Binary Diagnostic - Part 2 ---

o2gen = []
co2scrub = []
while inp := input():
    o2gen.append(inp)
    co2scrub.append(inp)

for i in range(len(o2gen[0])):
    if len(o2gen) == 1:
        break
    ones = []
    zeroes = []
    bits = [k[i] for k in o2gen]
    for k in range(len(bits)):
        if bits[k] == "1":
            ones.append(k)
        else:
            zeroes.append(k)
    if len(ones) > len(zeroes) or len(ones) == len(zeroes):
        o2gen = [o2gen[_] for _ in ones]
    else:
        o2gen = [o2gen[_] for _ in zeroes]

for i in range(len(co2scrub[0])):
    if len(co2scrub) == 1:
        break
    ones = []
    zeroes = []
    bits = [k[i] for k in co2scrub]
    for k in range(len(bits)):
        if bits[k] == "1":
            ones.append(k)
        else:
            zeroes.append(k)
    if len(ones) > len(zeroes) or len(ones) == len(zeroes):
        co2scrub = [co2scrub[_] for _ in zeroes]
    else:
        co2scrub = [co2scrub[_] for _ in ones]

print("***", int(o2gen[0], 2) * int(co2scrub[0], 2), "***")
