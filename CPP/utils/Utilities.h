//
// Created by Francesco Micheli on 27/01/23.
//

#ifndef CPP_UTILITIES_H
#define CPP_UTILITIES_H

#include <iostream>
#include <list>
#include <vector>

using namespace std;

class Utilities {
public:
    static void printArray(int arr[], int size);
    static void printVector(vector<int>& arr);
    static void swap(int *a, int *b);
};


#endif //CPP_UTILITIES_H
