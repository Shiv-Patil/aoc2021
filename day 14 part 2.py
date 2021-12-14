template = input()
input()
pairs = dict()
while inp := input():
    _ = inp.split(" -> ")
    pairs[_[0]] = _[1]

counts = dict()
for x in range(1, len(template)):
    a = template[x - 1]
    b = template[x]
    counts[a+b] = counts.get(a+b, 0) + 1

for x in range(40):
    new_counts = dict()
    for i in counts.keys():
        new_counts[i[0]+pairs[i]] = new_counts.get(i[0]+pairs[i], 0) + counts[i]
        new_counts[pairs[i]+i[1]] = new_counts.get(pairs[i]+i[1], 0) + counts[i]
    counts = new_counts

final_counts = dict()
for x in counts.keys():
    final_counts[x[0]] = final_counts.get(x[0], 0) + counts[x]
final_counts[template[-1]] = final_counts.get(template[-1], 0) + 1

print("***", max(final_counts.values())-min(final_counts.values()), "***")
