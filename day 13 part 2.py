dots = set()
while inp := input():
    dots.add((*map(int, inp.split(",")),))

while inp := input():
    fold_line = inp.split("=")
    fold_line = (0 if fold_line[0][-1] == 'x' else 1, int(fold_line[1]))
    dots_to_fold = {dot for dot in dots if dot[fold_line[0]] > fold_line[1]}
    dots = dots.difference(dots_to_fold)
    for dot in dots_to_fold:
        folded_dot = []
        folded_dot.insert(fold_line[0] ^ 1, dot[fold_line[0] ^ 1])
        folded_dot.insert(fold_line[0], fold_line[1] * 2 - dot[fold_line[0]])
        dots.add(tuple(folded_dot))

dots = list(dots)
rows = max([x[1] for x in dots]) + 1
cols = max([x[0] for x in dots]) + 1

for row in range(rows):
    for col in range(cols):
        print("▉" if (col, row) in dots else " ", end="")
    print()
