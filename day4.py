import sys
from collections import defaultdict
import re


def did_the_board_win(board, board_markings):
    # print(board)
    for i in range(5):  # column hunting
        marked = [board[i][j] for j in range(5) if board_markings[board[i][j]]]
        if len(marked) == 5:
            return True
    for j in range(5):  # row hunting
        marked = [board[i][j] for i in range(5) if board_markings[board[i][j]]]
        if len(marked) == 5:
            return True

    return False


def compute_score(number_stream, boards):
    boards_markings = [defaultdict(bool) for _ in boards]
    for i, number in enumerate(number_stream):
        for j, board in enumerate(boards):
            current_board_marking = boards_markings[j]
            current_board_marking[number] = True
            if did_the_board_win(board, current_board_marking):
                unmarked = [board[k][l] for k in range(5) for l in range(5) if not current_board_marking[board[k][l]]]
                print(number)
                print(board)
                return sum(unmarked) * number


def compute_score_part2(number_stream, boards):
    boards_markings = [defaultdict(bool) for _ in boards]
    last_winning_board_index = -1
    last_winning_num = 0
    ranks = [0 for _ in boards]
    for i, number in enumerate(number_stream):
        for j, board in enumerate(boards):
            current_board_marking = boards_markings[j]
            current_board_marking[number] = True
            if did_the_board_win(board, current_board_marking):
                ranks[j] = 1
                if sum(ranks) == len(ranks):
                    unmarked = [board[i][j] for i in range(5) for j in range(5) if not current_board_marking[board[i][j]]]
                    return sum(unmarked) * number


filename = sys.argv[1]
boards = []
with open(filename) as file:
    lines = file.readlines()
    number_stream = list(map(int, lines[0].split(",")))
    no_of_lines = len(lines)
    l = 2
    while l < no_of_lines:
        if lines[l] == "\n":
            l += 1
        else:
            board = [list(map(int, filter(lambda x: x != "", re.split(r'\s+', line.rstrip())))) for line in
                     lines[l:l + 5]]
            boards.append(board)
            l += 5
    print(boards)
    print(compute_score(number_stream, boards))
    print(compute_score_part2(number_stream, boards))