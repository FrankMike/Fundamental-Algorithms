import utils.searching as searching
import utils.list_tools as listtools
import utils.sorting as sorting
import utils.graph as graph
import utils.tree as tree
import utils.arrays as arrays
import utils.basics as basics

if __name__ == '__main__':
    print('Python fundamentals algorithms\n')

    # Searching Algorithms
    print('### Searching Algorithms ###\n')

    # Linear Search
    print('# Linear Search #\n')
    arr = [2, 3, 4, 10, 40]
    key = 10
    print(f'Array: {listtools.list_to_string(arr)}')
    print(f'Key: {key}')
    print('Iterative Implementation')
    linear_search_result = searching.linear_search(arr, key)
    if linear_search_result == -1:
        print('Key not found!')
    else:
        print(f'Key found at index {linear_search_result}')
    print('Recursive implementation')
    linear_search_result_rec = searching.linear_search_rec(arr, key, len(arr))
    if linear_search_result_rec == -1:
        print('Key not found!')
    else:
        print(f'Key found at index {linear_search_result_rec}')

    # Binary Search
    print('\n\n# Binary Search #\n')
    arr = [2, 3, 4, 10, 40]
    key = 10
    size = len(arr) / arr[0]
    result = searching.binary_search_rec(arr, 0, len(arr) - 1, key)
    print('Recursive Implementation')
    if result != -1:
        print(f'Element is present at index {result}')
    else:
        print(f'Element is not present in array')
    print('Iterative Implementation')
    searching.binary_search_iterative(arr, key)

    # Breadth First Search (BFS)
    print('\n\n# Breadth First Search (BFS) #')
    g = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("Breadth First Traversal: ")
    searching.bfs(g, 0)

    # Depth First Search (DFS)
    print('\n\n# Depth First Search (DFS) #')
    g = {'0': {'1', '2'},
         '1': {'0', '3', '4'},
         '2': {'0'},
         '3': {'1'},
         '4': {'2', '3'}}
    searching.dfs(g, '0')

    # Sorting Algorithms
    print('\n\n### Sorting Algorithms ###\n')

    # Insertion Sort
    print('# Insertion Sort #')
    array = [9, 5, 1, 4, 3]
    print(f'Unsorted array: {array}')
    sorting.insertion_sort(array)
    print(f'Sorted array in ascending order: {array}')

    # Heap Sort
    print('\n\n# Heap Sort #')
    array = [1, 12, 9, 5, 6, 10]
    print(f'Unsorted array: {array}')
    sorting.heap_sort(array)
    print(f'Sorted array is: {array}')

    # Selection Sort
    print('\n\n# Selection Sort #')
    array = [-2, 45, 0, 11, -9]
    print(f'Unsorted array: {array}')
    sorting.selection_sort(array)
    print(f'Sorted array: {array}')

    # Merge Sort
    print('\n\n# Merge Sort #')
    array = [6, 5, 12, 10, 9, 1]
    print(f'Unsorted array: {array}')
    sorting.merge_sort(array)
    print(f'Sorted array: {array}')

    # Counting Sort
    print('\n\n# Counting Sort #')
    array = [4, 2, 2, 8, 3, 3, 1]
    print(f'Unsorted array: {array}')
    sorting.counting_sort(array)
    print(f'Sorted array: {array}')

    # Quick Sort
    print('\n\n# Quick Sort #')
    array = [8, 7, 2, 1, 0, 9, 6]
    print(f'Unsorted array: {array}')
    sorting.quick_sort(array, 0, len(array) - 1)
    print(f'Sorted array: {array}')

    # Graph Algorithms
    print('\n\n### Graph Algorithms ###\n')

    # Kruskal's Algorithm (MST Minimum Spanning Tree)
    print('# Kruskal\'s Algorithm (MST Minimum Spanning Tree) #')
    vertices = 6
    g = graph.Graph(6, 0)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 2)
    g.add_edge(1, 0, 4)
    g.add_edge(2, 0, 4)
    g.add_edge(2, 1, 2)
    g.add_edge(2, 3, 3)
    g.add_edge(2, 5, 2)
    g.add_edge(2, 4, 4)
    g.add_edge(3, 2, 3)
    g.add_edge(3, 4, 3)
    g.add_edge(4, 2, 4)
    g.add_edge(4, 3, 3)
    g.add_edge(5, 2, 2)
    g.add_edge(5, 4, 3)
    g.kruskal()

    # Dijkstra's Algorithm
    print('\n\n# Dijkstra\'s Algorithm #')
    vertices = [[0, 0, 1, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 1, 0],
                [1, 1, 0, 1, 1, 0, 0],
                [1, 0, 1, 0, 0, 0, 1],
                [0, 0, 1, 0, 0, 1, 0],
                [0, 1, 0, 0, 1, 0, 1],
                [0, 0, 0, 1, 0, 1, 0]]

    edges = [[0, 0, 1, 2, 0, 0, 0],
             [0, 0, 2, 0, 0, 3, 0],
             [1, 2, 0, 1, 3, 0, 0],
             [2, 0, 1, 0, 0, 0, 1],
             [0, 0, 3, 0, 0, 2, 0],
             [0, 3, 0, 0, 2, 0, 1],
             [0, 0, 0, 1, 0, 1, 0]]
    g.dijkstra(vertices, edges)

    # Bellman Ford Algorithm
    print('\n\n# Bellman Ford Algorithm #')
    g = graph.Graph(5, 0)
    g.add_edge(0, 1, 5)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 3, 3)
    g.add_edge(2, 1, 6)
    g.add_edge(3, 2, 2)
    g.bellman_ford(0)

    # Floyd Warshall Algorithm
    print('\n\n# Floyd Warshall Algorithm #')
    INF = 999
    gfw = [[0, 3, INF, 5],
           [2, 0, INF, 4],
           [INF, 1, 0, INF],
           [INF, INF, 2, 0]]
    g = graph.Graph(4, 0)
    print("\nMatrix shows the shortest path")
    g.floyd_warshall(gfw, 4)

    # Topological Sort Algorithm
    print('\n\n# Topological Sort Algorithm #')
    g = graph.Graph(6, 0)
    g.add_edge(5, 2, 0)
    g.add_edge(5, 0, 0)
    g.add_edge(4, 0, 0)
    g.add_edge(4, 1, 0)
    g.add_edge(2, 3, 0)
    g.add_edge(3, 1, 0)
    print("\nTopological sort of the graph")
    g.topological_sort()

    # Flood Fill Algorithm
    print('\n\n# Flood Fill Algorithm #')
    g = graph.Graph(0, 0)
    screen = [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 0],
        [1, 0, 0, 1, 1, 0, 1, 1],
        [1, 2, 2, 2, 2, 0, 1, 0],
        [1, 1, 1, 2, 2, 0, 1, 0],
        [1, 1, 1, 2, 2, 2, 2, 0],
        [1, 1, 1, 1, 1, 2, 1, 1],
        [1, 1, 1, 1, 1, 2, 2, 1],
    ]
    m = len(screen)  # rows
    n = len(screen[0])  # columns
    print("Given array: ")
    for i in range(m):
        for j in range(n):
            print(screen[i][j], end=" ")
        print()
    x = 4
    y = 4
    prevc = screen[x][y]
    newc = 3
    print("\nSolution: ")
    g.flood_fill(screen, m, n, x, y, prevc, newc)

    # Lee Algorithm
    print('\n\n# Lee Algorithm #')
    src = graph.Pair(0, 0)
    dest = graph.Pair(3, 4)
    mat = [[1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
           [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
           [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
           [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
           [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
           [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
           [1, 1, 0, 0, 0, 0, 1, 0, 0, 1]
           ]
    print()
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end=" ")
        print()

    dist = graph.find_shortest_path_length(mat, src, dest)
    if dist != -1:
        print(f"Shortest path is: {dist}")
    else:
        print("Shortest path doesn't exist")

    # Kahn's Topological Sort Algorithm
    print('\n\n# Kahn\'s Topological Sort Algorithm #')
    g = graph.Graph(6, 0)
    g.add_edge(5, 2, 0)
    g.add_edge(5, 0, 0)
    g.add_edge(4, 0, 0)
    g.add_edge(4, 1, 0)
    g.add_edge(2, 3, 0)
    g.add_edge(3, 1, 0)
    g.kahn_topological_sort()

    # Tree Traversals Algorithms
    print('\n\n### Tree Traversals ###\n')
    # initializing tree
    root = tree.Node(1)
    root.left = tree.Node(2)
    root.right = tree.Node(3)
    root.left.left = tree.Node(4)
    root.left.right = tree.Node(5)

    # Inorder
    print("\n\n# In Order #")
    tree.inorder(root)

    # Preorder
    print("\n\n# Pre Order #")
    tree.preorder(root)

    # Postorder
    print("\n\n# Post Order #")
    tree.postorder(root)

    # Arrays Algorithms
    print('\n\n### Arrays ###\n')

    # Kadane's Algorithm
    print('\n# Kadane\'s Algorithm #')
    a = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(f'Array: {a}')
    arrays.kadane(a, len(a))
    
    # Floyd's Cycle Detection Algorithm
    print('\n# Floyd\'s Cycle Decection Algorithm #')
    head = arrays.Node(10)
    head.next = arrays.Node(20)
    head.next.next = arrays.Node(30)
    head.next.next.next = arrays.Node(40)
    head.next.next.next.next = arrays.Node(50)
    print("Given Linked List")
    ptr = head
    while ptr:
        print(str(ptr.data), end=' ')
        ptr = ptr.next
    print()
    arrays.floyd_cycle_detection(head)

    # KMP Algorithm
    print('\n# KMP Algorithm #')
    txt = "ABABDABACDABABCABAB"
    pat = "ABABCABAB"
    print(txt)
    print(pat)
    arrays.kmp(pat, txt)

    # Quick select Algorithm
    print('\n# Quick Select Algorithm #')
    arr = [ 10, 4, 5, 8, 6, 11, 26 ]
    n = len(arr)
    k = 3
    print(f'Given array: {arr}')
    print(f'K: {k}')
    print(f'K-th smallest element is {arrays.quick_select(arr, 0, n-1, k)}')

    # Boyer-Moore Majority Vote Algorithm
    print('\n# Boyer-Moor Majority Vote Algorithm #')
    arr = [1, 1, 1, 1, 2, 3, 4]
    print(f'Given Array: {arr}')
    n = len(arr)
    majority = arrays.boyer_moore(arr, n)
    print(f"The majority element is {majority}")

    # Basics Algorithms
    print('\n\n### Basics ###\n')

    # Huffman Coding Compression Algorithm
    print('\n# Huffman Coding Compression Algorithm #')
    chars = ['a', 'b', 'c', 'd', 'e', 'f']  # characters for huffman tree
    freq = [5, 9, 12, 13, 16, 45]   # frequency of characters
    print(f'Chars: {chars}')
    print(f'Frequencies: {freq}')
    basics.huffman(chars, freq)

    # Union Find Algorithm
    print('\n# Union Find Algorithm #')
    g = basics.Graph(3)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    # TODO: Print Graph
    if g.is_cyclic():
        print("Graph contains cycle")
    else:
        print("Graph does not conain cycle")

    # Euclid's Algorithm
    print('\n# Euclid\'s Algorithm #')
    print("Basic algorithm")
    a = 10
    b = 15
    gcd = basics.euclid(a, b)
    print(f"GCD: {a}, {b} = {gcd}")
    print("Extended Algorithm")
    a, b = 35, 15
    g, x, y = basics.euclid_extended(a, b)
    print(f'GCD({a}, {b}) = {g}')

