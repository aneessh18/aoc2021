import sys

instructions = []
filename = sys.argv[1]

def compute_final_position(instructions):
    x = 0
    y = 0
    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1])
        if direction == "forward":
            x += distance
        else:
            y += distance if direction == "down" else -1*distance

    return x*y

def compute_final_position_part2(instructions):
    x = 0
    y = 0
    aim = 0
    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1])
        if direction == "forward":
            x += distance
            y += aim*distance
        else:
            aim += distance if direction == "down" else -1*distance
    return x*y

with open(filename) as file:
    instructions= file.readlines()
    instructions = [instruction.split(" ") for instruction in instructions]

print(compute_final_position(instructions))
print(compute_final_position_part2(instructions))
