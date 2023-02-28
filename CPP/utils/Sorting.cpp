//
// Created by Francesco Micheli on 31/01/23.
//

#include "Sorting.h"


void Sorting::insertionSort(int *array, int size) {
    for(int step = 1; step < size; step++) {
        int key = array[step];
        int j = step-1;
        while (key < array[j] && j >= 0) {
            array[j+1] = array[j];
            --j;
        }
        array[j+1] = key;
    }
}

void Sorting::heapify(int *arr, int n, int i) {
    int largest = i;
    int left = 2*i+1;
    int right = 2*i+2;
    if (left<n && arr[left]>arr[largest])
        largest = left;
    if (right<n && arr[right] > arr[largest])
        largest = right;
    if (largest != i) {
        swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}

void Sorting::heapSort(int *arr, int n) {
    for (int i = n/2-1; i >= 0; i--)
        heapify(arr, n, i);
    for (int i = n-1; i >= 0; i--) {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}

void Sorting::selectionSort(int *array, int size) {
    for (int step = 0; step < size-1; ++step) {
        int min_idx = step;
        for (int i = step+1; i < size; ++i) {
            if (array[i]<array[min_idx])
                min_idx = i;
        }
        Utilities::swap(&array[min_idx], &array[step]);
    }
}

void Sorting::merge(int *arr, int const left, int const mid, int const right) {
    auto const subArrayOne = mid - left + 1;
    auto const subArrayTwo = right - mid;
    auto *leftArray = new int[subArrayOne], *rightArray = new int[subArrayTwo];
    for (auto i = 0; i < subArrayOne; i++)
        leftArray[i] = arr[left+i];
    for (auto j = 0; j < subArrayTwo; j++)
        rightArray[j] = arr[mid+1+j];
    auto indexOfSubArrayOne = 0, indexOfSubArrayTwo = 0, indexOfMergedArray = left;
    while (indexOfSubArrayOne < subArrayOne && indexOfSubArrayTwo < subArrayTwo) {
        if (leftArray[indexOfSubArrayOne] <= rightArray[indexOfSubArrayTwo]) {
            arr[indexOfMergedArray] = leftArray[indexOfSubArrayOne];
            indexOfSubArrayOne++;
        } else {
            arr[indexOfMergedArray] = rightArray[indexOfSubArrayTwo];
            indexOfSubArrayTwo++;
        }
        indexOfMergedArray++;
    }
    while (indexOfSubArrayOne < subArrayOne) {
        arr[indexOfMergedArray] = leftArray[indexOfSubArrayOne];
        indexOfSubArrayOne++;
        indexOfMergedArray++;
    }
    while (indexOfSubArrayTwo < subArrayTwo) {
        arr[indexOfMergedArray] = rightArray[indexOfSubArrayTwo];
        indexOfSubArrayTwo++;
        indexOfMergedArray++;
    }
    delete[] leftArray;
    delete[] rightArray;
}

void Sorting::mergeSort(int *arr, int l, int r) {
    if (l<r) {
        int m = l+(r-l)/2;
        mergeSort(arr,l,m);
        mergeSort(arr,m+1,r);
        merge(arr,l,m,r);
    }
}


void Sorting::countingSort(vector<int>& arr) {
    int max = *max_element(arr.begin(), arr.end());
    int min = *min_element(arr.begin(), arr.end());
    int range = max - min - 1;
    vector<int> count(range), output(arr.size());
    for (int i = 0; i < arr.size(); i++)
        count[arr[i] - min]++;
    for (int i = 1; i < count.size(); i++)
        count[i] += count[i-1];
    for (int i = arr.size()-1; i>=0; i--) {
        output[count[arr[i]-min]-1] = arr[i];
        count[arr[i]-min]--;
    }
    for (int i=0; i<arr.size(); i++)
        arr[i] = output[i];
}

int Sorting::partition(int *arr, int low, int high) {
    int pivot = arr[high];
    int i = (low-1);
    for (int j=low; j<=high-1; j++){
        if (arr[j]<pivot){
            i++;
            Utilities::swap(&arr[i], &arr[j]);
        }
    }
    Utilities::swap(&arr[i+1], &arr[high]);
    return (i+1);
}

void Sorting::quickSort(int *arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi-1);
        quickSort(arr, pi+1, high);
    }
}

