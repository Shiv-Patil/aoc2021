unique = (2, 4, 3, 7)
entries = []
while inp := input():
    entries.append((*map(lambda x: (*x.split(), ), inp.split(" | ")), ))

count = 0
for entry in entries:
    for output_value in entry[1]:
        if len(output_value) in unique:
            count+=1

print(count)
