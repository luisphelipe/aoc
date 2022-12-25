import sys
import pprint

pp = pprint.PrettyPrinter(indent=4).pprint


def main():
    result = solve()
    #  pp(result)


DP = {}


def solve():

    nodes = build_nodes()
    pp(nodes)

    result = dfs(nodes, nodes['AA'], build_meta())
    pp(result)

    global DP
    some_values = list(sorted(DP.items()))[:30]
    pp(some_values)

    return result


def process_tick(meta):
    tmp = {
        'tick': meta['tick'] + 1,
        'rate': meta['rate'],
        'total': meta['total'] + meta['rate'],
        'checked': meta['checked']
    }

    #  print(tmp['tick'], tmp['total'])
    return tmp


def build_meta():
    return {'tick': 0, 'rate': 0, 'total': 0, 'checked': []}


ticks = 30
MAX_TICKS = 30


def dfs(nodes, node, meta):
    key = dpkey(node, meta)
    global DP
    val = DP.get(key, False)
    if val:
        return val + meta['total']

    global ticks
    if meta['tick'] == ticks:
        print(f"step {31 - ticks}/30...")
        ticks -= 1

    global MAX_TICKS
    if meta['tick'] >= MAX_TICKS:
        return meta['total']

    results = check_children(nodes, node, meta)

    if valve_is_not_open(node, meta):
        meta = open_valve(node, meta)
        #  results.extend(check_children(nodes, node, meta))
        results.append(dfs(nodes, node, meta))

    results = max(list(set(results)))
    key = dpkey(node, meta)
    DP[key] = results - meta['total']
    return results


def dpkey(node, meta):
    tick = meta['tick']
    name = node['name']
    checked = ",".join(sorted(meta['checked']))
    return f"{tick}_{name}_with_{checked}"


def open_valve(node, meta):
    tmp = process_tick(dict(meta))
    tmp['rate'] += node['rate']
    checked = list(tmp['checked'])
    checked.append(node['name'])
    tmp['checked'] = checked
    return tmp


def valve_is_not_open(node, meta):
    return node['rate'] > 0 and node['name'] not in meta['checked']


def check_children(nodes, node, meta):
    meta = process_tick(meta)
    results = []
    for child in node['children']:
        res = dfs(nodes, nodes[child], dict(meta))
        results.append(res)
    return results


def build_nodes():
    nodes = {}
    line = sys.stdin.readline()[:-1]
    while line:
        node = build_node(line)
        nodes[node['name']] = node
        line = sys.stdin.readline()[:-1]
    return nodes


def build_node(line):
    name = get_name(line)
    rate = get_rate(line)
    children = get_children(line)
    node = {'name': name, 'rate': rate, 'children': children}
    return node


def get_name(line):
    tmp = line.split(" has")[0]
    tmp = tmp.split("Valve ")[1]
    return tmp


def get_rate(line):
    tmp = line.split("rate=")[1]
    tmp = tmp.split(";")[0]
    return int(tmp)


def get_children(line):
    tmp = line.split("to valves ")
    if len(tmp) == 1:
        tmp = line.split("to valve ")
    tmp = tmp[1]
    return tmp.split(", ")


main()
