import sys
import pprint

pp = pprint.PrettyPrinter(indent=4).pprint

TARGET = 4_000_000


def main():
    nodes = build_node_list()
    for x in range(TARGET + 1):
        # x = 3_204_480
        sol = solve(x, nodes)
        if len(sol) > 1 or sol[0][0] > 0 or sol[-1][1] < TARGET:
            coord = [x, sol[0][1] + 1]
            tuning_frequency = calculate_tuning_frequency(coord)
            print(x, sol)
            print(coord, tuning_frequency)


def solve(target, nodes):
    overlaps = build_overlap_list(target, nodes)
    # print(target, end=" ")
    # pp(overlaps)
    return overlaps


def build_node_list():
    nodes = []
    line = sys.stdin.readline()[:-1]
    while line:
        nodes.append(build_node(line))
        line = sys.stdin.readline()[:-1]
    return nodes


def build_node(line):
    coord = get_coord(line)
    distance = get_distance(coord, line)
    return (coord, distance)


def get_coord(line):
    tmp = line.split(":")[0]
    tmp = tmp.split("at x=")[1]
    tmp = tmp.split(", y=")
    coord = tuple([int(x) for x in tmp])
    return coord


def get_distance(coord, line):
    tmp = line.split(":")[1]
    tmp = tmp.split("at x=")[1]
    tmp = tmp.split(", y=")
    tmp = tuple([int(x) for x in tmp])
    distance = abs(tmp[0] - coord[0]) + abs(tmp[1] - coord[1])
    return distance


def build_overlap_list(target, nodes):
    overlaps = []
    for node in nodes:
        overlap = calculate_overlap(target, node)
        if overlap:
            overlaps.append(overlap)
    overlaps.sort()
    # pp(overlaps)
    overlaps = merge_overlaps(overlaps)
    return overlaps


def calculate_overlap(target, node):
    (coord, height) = node
    distance = abs(coord[0] - target)
    # print("distance", distance)
    if distance > height:
        return False
    width = height - distance
    return (coord[1] - width, coord[1] + width)


def merge_overlaps(overlaps):
    result = []
    current = list(overlaps[0])
    for i in range(len(overlaps)):
        ov = overlaps[i]
        if ov[0] <= current[1] + 1:
            current[1] = max(current[1], ov[1])
        else:
            result.append(list(current))
            current = list(ov)
    result.append(current)
    return result


def calculate_tuning_frequency(coord):
    return 4_000_000 * coord[0] + coord[1]


main()
