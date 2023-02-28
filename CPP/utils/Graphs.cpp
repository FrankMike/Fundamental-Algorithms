//
// Created by Francesco Micheli on 06/02/23.
//

#include "Graphs.h"

Graphs::Graphs(int V) {
    parent = new int[V];
    for (int i = 0; i < V; i++)
        parent[i] = i;
    G.clear();
    T.clear();
}

void Graphs::AddWeightedEdge(int u, int v, int w) {
    G.emplace_back(w, edge(u, v));
}

int Graphs::find_set(int i) {
    if (i == parent[i])
        return i;
    else
        return find_set(parent[i]);
}

void Graphs::union_set(int u, int v) {
    parent[u] = parent[v];
}

void Graphs::kruskal() {
    int i, uRep, vRep;
    sort(G.begin(), G.end());
    for (i = 0; i < G.size(); i++) {
        uRep = find_set(G[i].second.first);
        vRep = find_set(G[i].second.second);
        if (uRep != vRep) {
            T.push_back(G[i]);
            union_set(uRep, vRep);
        }
    }
}

void Graphs::print() {
    cout << "Edge: " << " Weight: " << endl;
    for (auto & i : T)
        cout << i.second.first << " - " << i.second.second << " : " << i.first << endl;

}

void Graphs::dijkstra(int graph[][]) {

}
