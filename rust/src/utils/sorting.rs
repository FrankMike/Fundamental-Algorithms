// Sorting Algorithms
use super::tools;

// Insertion Sort
pub fn insertion_sort(arr: &mut [i32]) {
    for i in 1..arr.len() {
        let key = arr[i];
        let mut j = i;
        while j > 0 && arr[j - 1] > key {
            arr[j] = arr[j - 1];
            j -= 1;
        }
        arr[j] = key;
    }
}

// Heap Sort
fn heapify(arr: &mut [i32], n: usize, i: usize) {
    let mut largest = i;
    let left = 2 * i + 1;
    let right = 2 * i + 2;
    if left < n && arr[left] > arr[largest] {
        largest = left;
    }
    if right < n && arr[right] > arr[largest] {
        largest = right;
    }
    if largest != i {
        arr.swap(i, largest);
        heapify(arr, n, largest);
    }
}

pub fn heap_sort(arr: &mut [i32]) {
    // Heapify the array
    let n = arr.len();
    for i in (0..n / 2).rev() {
        heapify(arr, n, i);
    }
    // Sort the array
    for i in (1..n).rev() {
        arr.swap(0, i);
        heapify(arr, i, 0);
    }
}

// Selection sort
pub fn selection_sort(arr: &mut [i32]) {
    for i in 0..arr.len() {
        let mut min_index = i;

        for j in i + 1..arr.len() {
            if arr[j] < arr[min_index] {
                min_index = j;
            }
        }

        if i != min_index {
            arr.swap(i, min_index);
        }
    }
}

// Merge Sort
fn merge(left: &Vec<i32>, right: &Vec<i32>) -> Vec<i32> {
    let mut i = 0;
    let mut j = 0;
    let mut merged: Vec<i32> = Vec::new();
    while i < left.len() && j < right.len() {
        if left[i] < right[j] {
            merged.push(left[i]);
            i += 1;
        } else {
            merged.push(right[j]) ;
            j += 1;
        }
    }
    if i < left.len() {
        while i < left.len() {
            merged.push(left[i]);
            i += 1;
        }
    }
    if j < right.len() {
        while j < right.len() {
            merged.push(right[j]);
            j += 1;
        }
    }
    merged
}

pub fn merge_sort(arr: &Vec<i32>) -> Vec<i32> {
    if arr.len() < 2 {
        arr.to_vec()
    } else {
        let size = arr.len() / 2;
        let left = merge_sort(&arr[0..size].to_vec());
        let right = merge_sort(&arr[size..].to_vec());
        let merged = merge(&left, &right);
        merged
    }
}


// Quick sort
fn partition(slice: &mut [i32]) -> usize {
    let len = slice.len();
    let pivot = slice[len-1];
    let mut i = 0;
    let mut j = 0;
    while j < len - 1 {
        if slice[j] <= pivot {
            slice.swap(i, j);
            i += 1;
        }
        j += 1;
    }
    slice.swap(i, len-1);
    i
}


pub fn quick_sort(slice: &mut [i32]) {
    if !slice.is_empty() {
        let partition_index = partition(slice);
        let len = slice.len();
        quick_sort(&mut &mut slice[0..partition_index]);
        quick_sort(&mut slice[partition_index+1..len]);
    }
}

// Counting Sort
pub fn counting_sort(arr: &mut [i32]) {
    let mut count: [i32; 10] = [0; 10];
    let min = tools::get_min(arr);
    let max = tools::get_max(arr);
    for num in arr.iter() {
        count[(num - min) as usize] += 1;
    }
    let mut z:usize = 0;
    for i in min..=max {
        while count[(i-min) as usize] > 0 {
            arr[z] = i;
            z += 1;
            count[(i-min) as usize] -= 1;
        }
    }
}
