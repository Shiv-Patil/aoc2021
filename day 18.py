def parse_input(inp):  # Stores the numbers in the form (start, close, value, nests)
    current_number = []
    # start = number of open brackets before current number
    # close = number of close brackets after previous number
    # nests = total number of currently open brackets at current number
    nests = start = close = 0
    for char in range(len(inp)):
        if inp[char] == "[":
            start += 1
            nests += 1
        elif inp[char] == "]":
            close += 1
            nests -= 1
        elif inp[char] != ",":
            current_number.append((start, close, int(inp[char]), nests))
            start = close = 0
    current_number.append((0, close, 0, 0))
    return current_number


def parse_number(num):  # Convert to array
    string = ""
    for i in range(len(num) - 1):
        string += "[" * num[i][0] + str(num[i][2]) + "]" * num[i + 1][1] + ","
    return string[:-1]


def explode(num, left, right):
    if left > 0:  # Is not the left-most number
        _ = num[left - 1]
        num[left - 1] = (_[0], _[1], _[2] + num[left][2], _[3])  # Adds the value of pair's left value to previous num
    if right < len(num) - 1:  # Is not the right-most number
        _ = num[right + 1]
        num[right + 1] = (_[0], _[1], _[2] + num[right][2], _[3])  # Adds the value of pair's right value to next num
    _ = num[right + 1]
    num[right + 1] = (_[0], _[1] - 1, _[2], _[3])  # Removes one closing bracket after pair's right value
    if _[1] > 1:  # If pair being exploded is the right value of parent pair
        num[right] = (0, 0, 0, num[right][3] - 1)
        num.pop(left)  # pop pair's left value and set right value to 0, decrement nests by 1
    else:  # If pair being exploded is the left value of parent pair
        num[left] = (num[left][0] - 1, num[left][1], 0, num[right][3] - 1)  # set left value to 0,
        num.pop(right)  # decrement nests by 1, removes one opening bracket from the pair's left value


def split(num, index):
    _ = num[index]
    left = (_[0] + 1, _[1], _[2] // 2, _[3] + 1)  # floor division, adds 1 opening bracket for the new pair
    right = (0, 0, -(-_[2] // 2), _[3] + 1)  # inverse floor (ceil) division
    _ = num[index + 1]
    num[index + 1] = (_[0], _[1] + 1, _[2], _[3])  # adds 1 closing bracket for closing the new pair
    num[index] = right
    num.insert(index, left)


def check_explodes(num):
    for i in range(len(num) - 1):
        if num[i][3] > 4:  # nests greater than 4, i.e, explode
            explode(num, i, i+1)
            return True
    return False


def check_splits(num):
    for i in range(len(num) - 1):
        if num[i][2] > 9:  # value 10 or greater, i.e, split
            split(num, i)
            return True
    return False


def reduce(num):
    while check_explodes(num) or check_splits(num):
        pass
    return num


def add_numbers(n1, n2):
    n1, n2 = n1[:], n2[:]
    n1[0] = (n1[0][0] + 1, n1[0][1], n1[0][2], n1[0][3])  # adds 1 opening bracket at the start
    n2[0] = (n2[0][0], n1[-1][1], n2[0][2], n2[0][3])  # no. of closing brackets of the last value of first number
    n2[-1] = (n2[-1][0], n2[-1][1] + 1, n2[-1][2], n2[0][3])  # adds 1 closing bracket at the end
    for i in range(len(n1)-1):
        n1[i] = (n1[i][0], n1[i][1], n1[i][2], n1[i][3] + 1)  # increments nest value for all numbers
    for i in range(len(n2)-1):
        n2[i] = (n2[i][0], n2[i][1], n2[i][2], n2[i][3] + 1)
    added = n1[:-1] + n2
    return reduce(added)


numbers = []
n = parse_input(input())
numbers.append(n[:])
while inp := input():
    inp = parse_input(inp)
    n = add_numbers(n, inp)
    numbers.append(inp[:])


def magnitude(arr):
    if type(arr) == int:
        return arr
    return 3 * magnitude(arr[0]) + 2 * magnitude(arr[1])


print("Part 1:", magnitude(eval(parse_number(n))))

max_mag = 0
for j in numbers:
    for k in numbers:
        if j != k:
            mag = magnitude(eval(parse_number(add_numbers(j, k))))
            if mag > max_mag:
                max_mag = mag

print("Part 2:", max_mag)
