import math
from itertools import cycle

starting_nodes = []

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree(input_string):
    node_map = {}

    for x in input_string:
        node_name, children_str = x.split(' = ')
        node_name = node_name.strip()

        if node_name[-1] == 'A':
            starting_nodes.append(node_name)

        children_str = children_str.strip()[1:-1]

        # Create the node if not exists
        if node_name not in node_map:
            node_map[node_name] = TreeNode(node_name)

        # Parse children and connect to parent
        children_names = children_str.split(', ')
        for child_name in children_names:
            child_name = child_name.strip()
            if child_name not in node_map:
                node_map[child_name] = TreeNode(child_name)

        node_map[node_name].left = node_map[children_names[0]]
        node_map[node_name].right = node_map[children_names[1]]

    return node_map


file = open("input_2").read().strip().split("\n\n")
transverse_pattern = file[0]
tree_structure = file[1].split('\n')

nodes_transversed = 0
tree = build_tree(tree_structure)

current_nodes = [tree[x] for x in starting_nodes]

def solve(node, i=0):
    while not node.value.endswith('Z'):
        d = transverse_pattern[i % len(transverse_pattern)]
        if d == 'R':
            node = node.right
        else:
            node = node.left
        i += 1
    return i

res = math.lcm(*map(solve, current_nodes))
print(res)
