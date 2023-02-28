#![allow(non_snake_case)]

mod utils;
use utils::searching;
use utils::tools;

use crate::utils::sorting;


fn main() {
    println!("\n\nFundamentals Algorithms in Rust");
    
    /* Searching Algorithms */
    println!("\n\n## Searching Algorithms ##\n");

    // Linear Search String
    let arr: [i32; 10] = [1, 3, 4, 6, 7, 8, 10, 12, 15, 20];
    let key: i32 = 6;
    println!("# Linear Search #");
    print!("Array given: ");
    tools::print_int_array(&arr);
    let index = searching::linear_search(&arr, &key);
    match index {
        Some(x) => println!("\nThe element {} is at index {}", key, x),
        None => println!("\nThe element {} is not present", key),
    }

    // Binary Search
    println!("\n# Binary Search #");
    let arr: [i32; 8] = [1, 2, 3, 4, 5, 8, 15, 90];
    let key: i32 = 5;
    print!("Array given: ");
    tools::print_int_array(&arr);
    let index = searching::binary_search(&arr, key);
    match index {
        Some(x) => println!("\nThe element {} is at index {}", key, x),
        None => println!("\nThe element {} is not present", key),
    }

    // Graph
    let mut graph = searching::Graph::new(4);
    graph.add_edge(0, 1);
    graph.add_edge(0, 2);
    graph.add_edge(1, 2);
    graph.add_edge(2, 0);
    graph.add_edge(2, 3);
    graph.add_edge(3, 3);

    // BFS Breadth First Search
    print!("\n\nBFS Traversal: ");
    searching::bfs(&graph, 2);

    // DFS Depth First Search
    let mut visited = vec![false; graph.vertices.len()];
    print!("\nDFS Traversal: ");
    searching::dfs(&graph, 2, &mut visited);

    // Sorting Algorithms
    println!("\n\n## Sorting algorithms ##");

    //Insertion Sort
    println!("\n# Insertion Sort #");
    let mut arr = [5, 8, 3, 4, 1, 2];
    print!("\nUnsorted Array: ");
    tools::print_int_array(&arr);
    sorting::insertion_sort(&mut arr);
    print!("\nSorted Array: ");
    tools::print_int_array(&arr);

    // Heap Sort
    println!("\n\n# Heap Short #\n");
    let mut arr = [3, 5, 2, 6, 8, 1, 0, 4, 7, 9];
    print!("Given array: ");
    tools::print_int_array(&arr);
    sorting::heap_sort(&mut arr);
    print!("\nSorted array: ");
    tools::print_int_array(&arr);

    // Selection Sort
    println!("\n\n# Selection Short #\n");
    let mut arr = [3, 5, 2, 6, 8, 1, 0, 4, 7, 9];
    print!("Given array: ");
    tools::print_int_array(&arr);
    sorting::selection_sort(&mut arr);
    print!("\nSorted array: ");
    tools::print_int_array(&arr);

    // Merge Sort
    println!("\n\n# Merge Short #\n");
    let arr = [3, 5, 2, 6, 8, 1, 0, 4, 7, 9].to_vec();
    print!("Given array: ");
    tools::print_int_array(&arr);
    let sorted_arr = sorting::merge_sort(&arr);
    print!("\nSorted array: ");
    tools::print_int_array(&sorted_arr);

    // Quick Sort
    println!("\n\n# Quick Short #\n");
    let mut arr = [3, 5, 2, 6, 8, 1, 0, 4, 7, 9];
    print!("Given array: ");
    tools::print_int_array(&arr);
    sorting::quick_sort(&mut arr);
    print!("\nSorted array: ");
    tools::print_int_array(&arr);

    // Counting Sort
    println!("\n\n# Counting Short #\n");
    let mut arr = [3, 5, 2, 6, 8, 1, 0, 4, 7, 9];
    print!("Given array: ");
    tools::print_int_array(&arr);
    sorting::counting_sort(&mut arr);
    print!("\nSorted array: ");
    tools::print_int_array(&arr);

}
