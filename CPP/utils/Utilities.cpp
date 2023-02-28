//
// Created by Francesco Micheli on 27/01/23.
//

#include "Utilities.h"

// Print Array function
void Utilities::printArray(int *arr, int size) {
    for (int i = 0; i < size; ++i) {
        cout << arr[i] <<" ";
    }
}

// Print Vector function
void Utilities::printVector(vector<int>& arr) {
    for (int i : arr)
        cout << i << " ";
    cout << endl;
}

// Swap two elements function
void Utilities::swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}



