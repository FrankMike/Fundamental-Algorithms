import collections


# Linear Search
# Iterative
def linear_search(list, key):
    for i in range(len(list)):
        if list[i] == key:
            return i
    return -1


# Recursive
def linear_search_rec(list, key, size):
    if size == 0:
        return -1
    elif list[size - 1] == key:
        return size - 1
    else:
        return linear_search_rec(list, key, size - 1)


# Binary Search
# Iterative implementation
def binary_search_iterative(v, x):
    l = 0
    h = len(v) - 1
    while h - l > 1:
        mid = (h + l) // 2
        if v[mid] < x:
            l = mid + 1
        else:
            h = mid
    if v[l] == x:
        print(f'Element found at index {l}')
    elif v[h] == x:
        print(f'Element found at index {h}')
    else:
        print('Element not found')


# Recursive implementation
def binary_search_rec(arr, l, r, x):
    if r >= l:
        mid = l + (r - 1) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search_rec(arr, l, mid-1, x)
        else:
            return binary_search_rec(arr, mid + 1, r, x)
    else:
        return -1


# Breadth First Search
def bfs(graph, root):
    visited, queue = set(), collections.deque([root])
    visited.add(root)
    while queue:
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


# Depth First Search
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited
