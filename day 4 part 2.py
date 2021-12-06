num_order = [*map(int, input().split(","))]
boards = []
boards_left = []
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
        boards_left.append(current_board)


def check_win(_board, _marker):
    size = round(len(_board) ** 0.5)
    for i in range(size):
        if [_marker] * size in (
            _board[i * size:(i + 1) * size],
            [_board[x] for x in [size * _ + i for _ in range(size)]]
        ):
            return True
    return False


def get_remaining(_boards_left):
    count = 0
    for ele in _boards_left:
        if ele is not None:
            count += 1
    return count


run = True
for num in num_order:
    for board_index in range (len(boards)):
        i = boards[board_index].index(num) if num in boards[board_index] else None
        if i is not None:
            boards[board_index][i] = marker
        if check_win(boards[board_index], marker):
            boards_left[board_index] = None
            if get_remaining(boards_left) == 0:
                run = False
                print("***", sum([n if n != marker else 0 for n in boards[board_index]]) * num, "***")
                break
    if not run:
        break
