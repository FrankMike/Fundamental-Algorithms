//
// Created by Francesco Micheli on 31/01/23.
//

#ifndef CPP_SORTING_H
#define CPP_SORTING_H

#include <iostream>
#include <vector>
#include "Utilities.h"

using namespace std;


class Sorting {
    void heapify(int arr[], int n, int i);
    void merge(int arr[], int p, int q, int r);
    int partition(int arr[], int low, int high);
public:
    void insertionSort(int array[], int size);
    void heapSort(int arr[], int n);
    void selectionSort(int array[], int size);
    void mergeSort(int arr[], int l, int r);
    void countingSort(vector<int>& arr);
    void quickSort(int arr[], int low, int high);
};


#endif //CPP_SORTING_H
