import heapq
from collections import defaultdict


class Graph:
    def __init__(self, vertices) -> None:
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def find_parent(self, parent, i):
        if parent[i] == i:
            return i
        if parent[i] != i:
            return self.find_parent(parent, parent[i])

    def __repr__(self):
        repr_str = ""
        for vertex, edges in self.graph.items():
            repr_str += f"{vertex}: {', '.join(str(edge) for edge in edges)}\n"
        return repr_str

    # Union Find Algorithm
    def union(self, parent, x, y):
        parent[x] = y

    def is_cyclic(self):
        parent = [0] * self.V
        for i in range(self.V):
            parent[i] = i
        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(parent, i)
                y = self.find_parent(parent, j)
                if x == y:
                    return True
                self.union(parent, x, y)


class TreeNode:
    def __init__(self, freq, symbol, left=None, right=None):
        # frequency of symbol
        self.freq = freq
        # symbol name (character)
        self.symbol = symbol
        # node left of current node
        self.left = left
        # node right of current node
        self.right = right
        # tree direction (0/1)
        self.huff = ''

    def __lt__(self, nxt):
        return self.freq < nxt.freq


# print_nodes function
def print_nodes(node, val=''):
    newVal = val + str(node.huff)
    if node.left:
        print_nodes(node.left, newVal)
    if node.right:
        print_nodes(node.right, newVal)
    if not node.left and not node.right:
        print(f"{node.symbol} -> {newVal}")


def huffman(chars, freq):
    nodes = []
    for x in range(len(chars)):
        heapq.heappush(nodes, TreeNode(freq[x], chars[x]))

    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        left.huff = 0
        right.huff = 1
        newNode = TreeNode(left.freq+right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(nodes, newNode)
    print_nodes(nodes[0])


# Euclid's Algorithm
# Basic Algorithm
def euclid(a, b):
    r = a % b
    while 1:
        r = a % b
        if not r:
            break
        a = b
        b = r
    return b


# Extended Algorithm
def euclid_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = euclid_extended(b % a, a)
    x = y1-(b//a)*x1
    y = x1
    return gcd, x, y


# Fermat Little Theorem
def fermat_modular_exponentiation(a, b, mod):
    res = 1
    a = a % mod
    while b > 0:
        if b % 2 != 0:
            res = res * a % mod
        a = (a * a) % mod
        b = b / 2
    return res


# m must be a prime number
# a = 0
# m = 0
# print(fermat_modular_exponentiation(a, m-2, m))
