/* Searching Algorithms */
use std::collections::LinkedList;

// Linear Search
pub fn linear_search(arr: &[i32], key: &i32) -> Option<usize> {
    for (i, data) in arr.iter().enumerate() {
        if key == data {
            return Some(i);
        }
    }
    None
}

// Binary Search
pub fn binary_search(arr: &[i32], find: i32) -> Option<usize> {
    let length = arr.len();
    let mut half_index = length / 2;
    let mut high_index = length - 1;
    let mut low_index = 0;
    let mut current = arr[half_index];
    while low_index <= high_index {
        match current.cmp(&find) {
            std::cmp::Ordering::Equal => return Some(half_index),
            std::cmp::Ordering::Less => low_index = half_index +1,
            std::cmp::Ordering::Greater => high_index = half_index -1,
        }
        half_index = (high_index + low_index) / 2;
        current = arr[half_index];
    }
    return None;
}


// Graph structure
pub struct Graph {
    pub vertices: Vec<Vec<u32>>,
}

impl Graph {
    pub fn new(size: usize) -> Self {
        Graph { vertices: vec![Vec::new(); size] }
    }

    pub fn add_edge(&mut self, u: usize, v: usize) {
        self.vertices[u].push(v as u32);
    }
}

// BFS implementation
pub fn bfs(graph: &Graph, start: usize) {
    let mut visited = vec![false; graph.vertices.len()];
    let mut queue = LinkedList::new();

    visited[start] = true;
    queue.push_back(start);

    while !queue.is_empty() {
        let u = queue.pop_front().unwrap();
        print!("{} ", u);

        for v in &graph.vertices[u] {
            if !visited[*v as usize] {
                visited[*v as usize] = true;
                queue.push_back(*v as usize);
            }
        }
    }
}

// DFS implementation
pub fn dfs(graph: &Graph, start: usize, visited: &mut Vec<bool>) {
    visited[start] = true;
    print!("{} ", start);

    for v in &graph.vertices[start] {
        if !visited[*v as usize] {
            dfs(graph, *v as usize, visited);
        }
    }
}

// BFS Breadth First Search


// DFS Depth First Search
