num_order = [*map(int, input().split(","))]
boards = []
marker = "X"
run_input = True
while run_input:
    input()
    current_board = []
    for _ in range(5):
        i = input()
        if not i:
            run_input = False
            break
        current_board.extend([*map(int, i.split())])
    if current_board:
        boards.append(current_board)


def check_win(_board, _marker):
    size = round(len(_board) ** 0.5)
    for i in range(size):
        if [_marker] * size in (
            _board[i * size:(i + 1) * size],
            [_board[x] for x in [size * _ + i for _ in range(size)]]
        ):
            return True
    return False


run = True
for num in num_order:
    for board in boards:
        i = board.index(num) if num in board else None
        if i is not None:
            board[i] = marker
        if check_win(board, marker):
            print("**", sum([n if n != marker else 0 for n in board]), num, "**")
            print("***", sum([n if n != marker else 0 for n in board]) * num, "***")
            run = False
            break
    if not run:
        break
