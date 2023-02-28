//
// Created by Francesco Micheli on 06/02/23.
//

#ifndef CPP_GRAPHS_H
#define CPP_GRAPHS_H

#include <algorithm>
#include <iostream>
#include <vector>
#include <climits>

using namespace std;

#define edge pair<int, int>

class Graphs {
private:
    vector<pair<int, edge>> G; //   Graph
    vector<pair<int, edge>> T; //   MST
    int *parent;
    int V;
public:
    explicit Graphs(int V);

    // Kruskal
    void AddWeightedEdge(int u, int v, int w);
    int find_set(int i);
    void union_set(int u, int v);
    void kruskal();

    // Dijkstra
    void dijkstra();

    // Utils
    void print();
};




#endif //CPP_GRAPHS_H
