original_segments = ("abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg")
lengths = (6, 2, 5, 5, 4, 5, 6, 3, 7, 6)
entries = []
while inp := input():
    entries.append((*map(lambda x: (*x.split(), ), inp.split(" | ")), ))

total = 0
for entry in entries:
    segments_changed = dict()

    for signal in entry[0]:
        segments_changed[len(signal)] = segments_changed.get(len(signal), set("abcdefg")).intersection(set(signal))

    # segment_changed contains 6 sets:
    # intersection of 5 segment numbers (2, 3, 5) = a d g
    # intersection of 6 segment numbers (0, 6, 9) = a b f g
    # segments at 1, 4, 7, 8 respectively = cf, bcdf, acf, abcdefg
    # matching these sets give all individual segments, as given below: (lines 21-31)

    a = segments_changed[3].difference(segments_changed[2])
    c = segments_changed[2].difference(segments_changed[6])
    eg = segments_changed[7].difference(segments_changed[4].union(segments_changed[3]))
    bd = segments_changed[4].difference(segments_changed[2])
    dg = segments_changed[5].difference(a)
    cf = segments_changed[2].intersection(segments_changed[3])
    f = cf.difference(c)
    g = eg.intersection(dg)
    e = eg.difference(g)
    d = dg.difference(g)
    b = bd.difference(d)

    new_segments = {a.pop(): "a", b.pop(): "b", c.pop(): "c",  d.pop(): "d", e.pop(): "e", f.pop(): "f", g.pop(): "g"}
    # ^ (key: value) = (new_segment: old_segment)
    print(new_segments)
    digits = ""
    for digit in entry[1]:
        digits += str(original_segments.index(''.join(sorted(map(lambda x: new_segments[x], digit)))))
    total += int(digits)

print("***", total, "***")
