import sys

filename = sys.argv[1]


def is_opening(char):
    return char == '[' or char == '{' or char == '(' or char == '<'


def get_illegal_char_in_chunk(chunk):
    stack = []
    closing_char_dict = {
        '[': ']',
        '{': '}',
        '(': ')',
        '<': '>'
    }
    for char in chunk:
        if len(stack) == 0 or is_opening(char):
            stack.append(char)
        else:
            top_char = stack.pop()
            # print(top_char, char)
            if closing_char_dict[top_char] != char:
                return char
    return [closing_char_dict[ele] for ele in stack[::-1]]


with open(filename) as file:
    lines = file.readlines()
    chunks = [line.rstrip() for line in lines]
    illegal_char_score = {
        "": 0,
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    incomplete_char_score = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    syntax_error_score = 0
    incomplete_chunk_scores = []
    for chunk in chunks:
        illegal_char = get_illegal_char_in_chunk(chunk)
        syntax_error_score += illegal_char_score[illegal_char if type(illegal_char) == str else ""]
        if type(illegal_char) == list:
            incomplete_chars = illegal_char
            score = 0
            print(incomplete_chars)
            for incomplete_char in incomplete_chars:
                score = score*5 + incomplete_char_score[incomplete_char]
            incomplete_chunk_scores.append(score)

    incomplete_chunk_scores.sort()
    print(syntax_error_score)
    print(incomplete_chunk_scores[len(incomplete_chunk_scores)/2])
