import sys
import pprint

pp = pprint.PrettyPrinter(indent=4).pprint

TARGET = 10


def main():
    result = solve(TARGET)
    print("result is", result)


def solve(target):
    nodes = build_node_list()
    print("nodes")
    pp(nodes)

    overlaps = build_overlap_list(target, nodes)
    print("overlaps")
    pp(overlaps)

    solution = count_overlap_length(overlaps)

    return solution


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
    overlaps = merge_overlaps(overlaps)
    return overlaps


def calculate_overlap(target, node):
    (coord, height) = node
    distance = abs(coord[1] - target)
    if distance < height:
        return False
    width = distance - height
    return (coord[0] - width, coord[0] + width)


def merge_overlaps(overlaps):
    result = []
    current = list(overlaps[0])
    for i in range(len(overlaps)):
        ov = overlaps[i]
        if ov[0] <= current[1] + 1:
            current[1] = max(current[1], ov[1])
        else:
            result.append(ov)
            current = list(ov)
    result.append(current)
    return result


def count_overlap_length(overlaps):
    result = 0
    for ov in overlaps:
        result += ov[1] - ov[0]
    return result


main()
