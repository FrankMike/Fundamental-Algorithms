#include <iostream>
#include <vector>
#include "utils/Utilities.h"
#include "utils/Searching.h"
#include "utils/Sorting.h"
#include "utils/Graphs.h"

using namespace std;

int main() {
    cout << "Fundamentals Algorithms in C++"<< endl;
    
    // Searching Algorithms
    cout << "\n### Searching Algorithms ###" << endl;
    Searching searching{};

    // Linear Search
    cout << "\n# Linear Search #" << endl;
    int arr[] = {2, 3, 4, 10, 40};
    int x = 10;
    int arraySize = sizeof(arr) / sizeof(arr[0]);
    int result = searching.linearSearch(arr, arraySize, x);
    cout << "Given array: ";
    Utilities::printArray(arr, arraySize);
    cout << "\nSearch key: " << x << endl;
    (result == -1)
        ? cout << "Element is not present in array"
        : cout << "Element is present at index " << result << endl;

    // Binary Search
    cout << "\n# Binary Search #" << endl;
    int arrBS[] = {3, 4, 5, 6, 7, 8, 9};
    x = 4;
    arraySize = sizeof(arrBS)/sizeof(arrBS[0]);
    result = searching.binarySearch(arrBS, x, 0, arraySize-1);
    if (result == -1)
        cout << "Element is not present in array";
    else
        cout << "Element is present at index " << result << endl;

    // BFS Breadth First Search
    cout << "\n# BFS Breadth First Search #" << endl;
    Graph g(4);
    g.addEdge(0,1);
    g.addEdge(0,2);
    g.addEdge(1,2);
    g.addEdge(2,0);
    g.addEdge(2,3);
    g.addEdge(3,3);
    g.BFS(2);

    // DFS Depth First Search
    cout << "\n# DFS Depth First Search #" << endl;
    Graph g2(4);
    g2.addEdge(0,1);
    g2.addEdge(0,2);
    g2.addEdge(1,2);
    g2.addEdge(2,0);
    g2.addEdge(2,3);
    g2.addEdge(3,3);
    g2.DFS(2);
    cout << endl;

    // Sorting Algorithms
    cout << "\n### Sorting Algorithms ###" << endl;
    Sorting sorting;

    // Insertion Sort
    cout << "\n# Insertion Sort #" << endl;
    int data[] = {9,5,1,4,3};
    int size = sizeof(data) / sizeof(data[0]);
    cout << "Given Array: ";
    Utilities::printArray(data, size);
    sorting.insertionSort(data, size);
    cout << "\nSorted Array: ";
    Utilities::printArray(data, size);
    cout << endl;


    // Heap Sort
    cout << "\n# Heap Sort #" << endl;
    int arrHS[] = {1, 12, 9, 5, 6, 10};
    int sizeHS = sizeof(arrHS) / sizeof(arrHS[0]);
    cout << "Given Array: ";
    Utilities::printArray(arrHS, sizeHS);
    sorting.heapSort(arrHS, sizeHS);
    cout << "\nSorted Array: ";
    Utilities::printArray(arrHS, sizeHS);
    cout << endl;

    // Selection Sort
    cout << "\n# Selection Sort #" << endl;
    int arraySS[] = {20,12,10,15,2};
    int sizeSS = sizeof(arraySS)/sizeof(arraySS[0]);
    cout << "Unsorted array: ";
    Utilities::printArray(arraySS, sizeSS);
    sorting.selectionSort(arraySS, sizeSS);
    cout << "\nSorted array: ";
    Utilities::printArray(arraySS, sizeSS);
    cout << endl;

    // Merge Sort
    cout << "\n# Merge Sort #" << endl;
    int arrMS[] = {6,5,12,10,9,1};
    int sizeMS = sizeof(arrMS)/sizeof(arrMS[0]);
    cout << "Unsorted array: ";
    Utilities::printArray(arrMS, sizeMS);
    sorting.mergeSort(arrMS, 0, sizeMS-1);
    cout << "\nSorted array: ";
    Utilities::printArray(arrMS, sizeMS);
    cout << endl;

    // Counting Sort
    cout << "\n# Counting Sort #" << endl;
    vector<int> arrCS = {-5,-10,0,-3,8,5,-1,10};
    cout << "Unsorted array: ";
    Utilities::printVector(arrCS);
    sorting.countingSort(arrCS);
    cout << "Sorted array: ";
    Utilities::printVector(arrCS);
    cout << endl;

    // Quick Sort
    cout << "\n# Quick Sort #" << endl;
    int arrQS[] = {10,7,8,9,1,5};
    int sizeQS = sizeof(arrQS)/sizeof(arrQS[0]);
    cout << "Unsorted array: ";
    Utilities::printArray(arrQS, sizeQS);
    sorting.quickSort(arrQS, 0, sizeQS-1);
    cout << "\nSorted array: ";
    Utilities::printArray(arrQS, sizeQS);
    cout << endl;

    // Graph Algorithms
    cout << "\n### Graph Algorithms ###" << endl;

    // Kruskal
    cout << "\n# Kruskal Algorithm #" << endl;
    Graphs graphs(6);
    graphs.AddWeightedEdge(0, 1, 4);
    graphs.AddWeightedEdge(0, 2, 4);
    graphs.AddWeightedEdge(1, 2, 2);
    graphs.AddWeightedEdge(1, 0, 4);
    graphs.AddWeightedEdge(2, 0, 4);
    graphs.AddWeightedEdge(2, 1, 2);
    graphs.AddWeightedEdge(2, 3, 3);
    graphs.AddWeightedEdge(2, 5, 2);
    graphs.AddWeightedEdge(2, 4, 4);
    graphs.AddWeightedEdge(3, 2, 3);
    graphs.AddWeightedEdge(3, 4, 3);
    graphs.AddWeightedEdge(4, 2, 4);
    graphs.AddWeightedEdge(4, 3, 3);
    graphs.AddWeightedEdge(5, 2, 2);
    graphs.AddWeightedEdge(5, 4, 3);
    graphs.kruskal();
    graphs.print();

    // Dijkstra

    // Bellman Ford

    // Floyd Warshall

    // Topological Sort

    // Flood Fill

    // Lee

    // Kahn's Topological Sort

    // Tree Traversals
    // In order

    // Pre order

    // Post order

    // Arrays Algorithms
    // Kadane

    // Floyd's Cycle Detection

    // KMP

    // Quick select

    // Boyer-Moore Majority Vote

    // Basics
    // Huffman Coding Compression

    // Union Find

    // Euclid's Algorithm

    return 0;
}
