//
// Created by Francesco Micheli on 27/01/23.
//

#ifndef CPP_SEARCHING_H
#define CPP_SEARCHING_H

#include <iostream>
#include <list>

using namespace std;

class Searching {
    int numVertices;
    list<int>* adjLists;
    bool* visited;
public:
    int linearSearch(int arr[], int N, int x);
    int binarySearch(int arr[], int x, int low, int high);
};

class Graph {
    int numVertices;
    list<int>* adjLists;
    bool* visited;
public:
    Graph(int vertices);
    void addEdge(int src, int dest);
    void BFS(int startVertex);
    void DFS(int vertex);
};

#endif //CPP_SEARCHING_H
