chunks = {'(': ')', '[': ']', '{': '}', '<': '>'}
scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
totalscore = 0

while inp := input():
    open_chunks = []
    for char in inp:
        if char in chunks.keys():
            open_chunks.append(char)
        elif not open_chunks or chunks.get(open_chunks[-1], '') != char:
            totalscore += scores[char]
            break
        else:
            open_chunks.pop()

print("***", totalscore, "***")
