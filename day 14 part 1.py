template = input()
input()
pairs = dict()
while inp := input():
    _ = inp.split(" -> ")
    pairs[_[0]] = _[1]

for step in range(10):
    new_template = template[0]
    for x in range(1, len(template)):
        new_template += pairs.get(template[x-1]+template[x], "")+template[x]
    template = new_template

counts = {template.count(i) for i in template}
print("***", max(counts)-min(counts), "***")
