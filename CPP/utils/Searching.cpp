//
// Created by Francesco Micheli on 27/01/23.
//

#include "Searching.h"

int Searching::linearSearch(int arr[], int N, int x) {
    int i;
    for (i = 0; i < N; i++)
        if (arr[i] == x)
            return i;
    return -1;
}

int Searching::binarySearch(int *arr, int x, int low, int high) {
    while (low <= high) {
        int mid = low + (high-low) / 2;
        if (arr[mid]==x)
            return mid;
        if (arr[mid]<x)
            low = mid + 1;
        else
            high = mid-1;
    }
    return -1;
}


Graph::Graph(int vertices) {
    numVertices = vertices;
    adjLists = new list<int>[vertices];
    visited = new bool[vertices];
}

void Graph::addEdge(int src, int dest) {
    adjLists[src].push_back(dest);
}

void Graph::BFS(int startVertex) {
    visited = new bool[numVertices];
    for (int i = 0; i < numVertices; ++i)
        visited[i] = false;
    list<int> queue;
    visited[startVertex] = true;
    queue.push_back(startVertex);
    list<int>::iterator i;
    while (!queue.empty()) {
        int currVertex = queue.front();
        cout << "Visited " << currVertex << " ";
        queue.pop_front();
        for(i=adjLists[currVertex].begin(); i!=adjLists[currVertex].end(); ++i) {
            int adjVertex = *i;
            if (!visited[adjVertex]) {
                visited[adjVertex] = true;
                queue.push_back(adjVertex);
            }
        }
    }
}

void Graph::DFS(int vertex) {
    visited[vertex] = true;
    list<int> adjList = adjLists[vertex];
    cout << vertex << " ";
    list<int>::iterator i;
    for (i = adjList.begin(); i != adjList.end(); ++i)
        if (!visited[*i])
            DFS(*i);
}