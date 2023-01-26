import sys
from collections import defaultdict

INF = 999


class Graph:
    def __init__(self, vertices, edges):
        self.V = vertices
        self.E = edges
        self.graph = []
        self.adjacencies = defaultdict(list)

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
        self.adjacencies[u].append(v)

    # Search function

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # Print function
    def print_solution(self, dist):
        print("Vertex distance from source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    # Kruskal algorithm
    def kruskal(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))

    # Dijkstra Algorithm
    def dijkstra(self, vertices, edges):
        visited_and_distance = [[0, 0]]
        for i in range(len(vertices)-1):
            visited_and_distance.append([0, sys.maxsize])
        for vertex in range(len(vertices)):
            # Find vertex to be visited next
            to_visit = -10
            for index in range(len(vertices)):
                if visited_and_distance[index][0] == 0 and (to_visit < 0 or
                                                            visited_and_distance[index][1] <= visited_and_distance[to_visit][1]):
                    to_visit = index
            for neighbor_index in range(len(vertices)):
                if vertices[to_visit][neighbor_index] == 1 and visited_and_distance[neighbor_index][0] == 0:
                    new_distance = visited_and_distance[to_visit][1] + \
                        edges[to_visit][neighbor_index]
                    if visited_and_distance[neighbor_index][1] > new_distance:
                        visited_and_distance[neighbor_index][1] = new_distance
                visited_and_distance[to_visit][0] = 1
        i = 0
        # Print the distance
        for distance in visited_and_distance:
            print("Distance of ", chr(ord('a') + i),
                  " from source vertex: ", distance[1])
            i = i + 1

    # Bellman Ford Algorithm
    def bellman_ford(self, src):
        dist = [float("Inf")] * self.V
        dist[src] = 0
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return
        self.print_solution(dist)

    # Floyd Warshall Algorithm
    def floyd_warshall(self, G, V):
        distance = list(map(lambda i: list(map(lambda j: j, i)), G))
        for k in range(V):
            for i in range(V):
                for j in range(V):
                    distance[i][j] = min(
                        distance[i][j], distance[i][k] + distance[k][j])
        for i in range(V):
            for j in range(V):
                if (distance[i][j] == INF):
                    print("INF", end=" ")
                else:
                    print(distance[i][j], end=" ")
            print(" ")

    # Topological Sort Algorithm
    def topological_sort(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topological_sort_util(i, visited, stack)
        print(stack)

    def topological_sort_util(self, v, visited, stack):
        visited[v] = True
        for i in self.adjacencies[v]:
            if visited[i] == False:
                self.topological_sort_util(i, visited, stack)
        stack.insert(0, v)

    # Flood Fill Algorithm
    def is_valid(self, screen, m, n, x, y, prevc, newc):
        if x < 0 or x >= m or y < 0 or y >= n or screen[x][y] != prevc or screen[x][y] == newc:
            return False
        return True

    def flood_fill(self, screen, m, n, x, y, prevc, newc):
        queue = []
        queue.append([x, y])
        screen[x][y] = newc
        while queue:
            curr_node = queue.pop()
            posx = curr_node[0]
            posy = curr_node[1]
            if self.is_valid(screen, m, n, posx+1, posy, prevc, newc):
                screen[posx+1][posy] = newc
                queue.append([posx+1, posy])
            if self.is_valid(screen, m, n, posx-1, posy, prevc, newc):
                screen[posx-1][posy] = newc
                queue.append([posx-1, posy])
            if self.is_valid(screen, m, n, posx, posy+1, prevc, newc):
                screen[posx][posy+1] = newc
                queue.append([posx, posy+1])
            if self.is_valid(screen, m, n, posx, posy-1, prevc, newc):
                screen[posx][posy-1] = newc
                queue.append([posx, posy-1])
        for i in range(m):
            for j in range(n):
                print(screen[i][j], end=" ")
            print()

    # Kahn's Topological Sorting Algorithm
    def kahn_topological_sort(self):
        in_degree = [0]*(self.V)
        for i in self.adjacencies:
            for j in self.adjacencies[i]:
                in_degree[j] += 1
        queue = []
        for i in range(self.V):
            if in_degree[i] == 0:
                queue.append(i)
        cnt = 0
        top_order = []
        while queue:
            u = queue.pop(0)
            top_order.append(u)
            for i in self.adjacencies[u]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)

            cnt += 1
        if cnt != self.V:
            print("There exists a cycle in the graph")
        else:
            print("Topological Sort using Khan's Algorithm")
            print(top_order)


class Pair:
    def __init__(self, x, y) -> None:
        self.first = x
        self.second = y


# Lee's Algorithm
def is_safe(mat, visited, x, y):
    return (x >= 0 and x < len(mat) and y >= 0 and y < len(mat[0]) and mat[x][y] == 1 and (not visited[x][y]))


def find_shortest_path(mat, visited, i, j, x, y, min_dist, dist):
    if i == x and j == y:
        min_dist = min(dist, min_dist)
        return min_dist
    visited[i][j] = True
    if is_safe(mat, visited, i+1, j):
        min_dist = find_shortest_path(
            mat, visited, i+1, j, x, y, min_dist, dist+1)
    if is_safe(mat, visited, i, j+1):
        min_dist = find_shortest_path(
            mat, visited, i, j+1, x, y, min_dist, dist+1)
    if is_safe(mat, visited, i-1, j):
        min_dist = find_shortest_path(
            mat, visited, i-1, j, x, y, min_dist, dist+1)
    if is_safe(mat, visited, i, j-1):
        min_dist = find_shortest_path(
            mat, visited, i, j-1, x, y, min_dist, dist+1)
    visited[i][j] = False
    return min_dist


def find_shortest_path_length(mat, src, dest):
    if len(mat) == 0 or mat[src.first][dest.second] == 0 or mat[dest.first][dest.second] == 0:
        return -1
    row = len(mat)
    col = len(mat[0])
    visited = []
    for i in range(row):
        visited.append([None for _ in range(col)])
    dist = sys.maxsize
    dist = find_shortest_path(mat, visited, src.first,
                              src.second, dest.first, dest.second, dist, 0)
    if dist != sys.maxsize:
        return dist
    return -1
