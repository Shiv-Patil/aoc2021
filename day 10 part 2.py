chunks = {'(': ')', '[': ']', '{': '}', '<': '>'}
scores = {')': 1, ']': 2, '}': 3, '>': 4}
totalscores = []

while inp := input():
    open_chunks = []
    score = 0
    for char in inp:
        if char in chunks.keys():
            open_chunks.insert(0, char)
        elif char != chunks[open_chunks[0]]:
            open_chunks = []
            break
        else:
            open_chunks.pop(0)
    if not open_chunks:
        continue
    for to_close in open_chunks:
        score *= 5
        score += scores[chunks[to_close]]
    totalscores.append(score)

totalscores.sort()
print("***", totalscores[len(totalscores)//2], "***")
