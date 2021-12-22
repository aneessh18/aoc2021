import sys

filename = sys.argv[1]


def compute_fuel_consumption(horizontal_positions, position):
    return sum([abs(position - horizontal_position)for horizontal_position in horizontal_positions])


def compute_fuel_consumption_part2(horizontal_positions, position):
    return sum([(abs(position - horizontal_position)*(abs(position - horizontal_position)+1))/2 for horizontal_position in horizontal_positions])

with open(filename) as file:
    lines = file.readlines()
    horizontal_positions = list(map(int, lines[0].rstrip().split(",")))
    min_position = min(horizontal_positions)
    max_position = max(horizontal_positions)
    min_fuel_req = 10 ** 10
    min_fuel_req_2 = 10 ** 10

    for position in range(min_position, max_position + 1):
        min_fuel_req = min(min_fuel_req,compute_fuel_consumption(horizontal_positions, position))
    for position in range(min_position, max_position + 1):
        min_fuel_req_2 = min(min_fuel_req_2, compute_fuel_consumption_part2(horizontal_positions, position))
    print(min_fuel_req)
    print(min_fuel_req_2)
