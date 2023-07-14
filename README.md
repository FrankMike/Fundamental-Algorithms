# Fundamental Algorithms

## Searching:
- Linear Search
- Binary Search
- Breadth First Search (BFS)
- Depth First Search (DFS)

## Sorting:
- Insertion Sort Algorithm
- Heap Sort Algorithm
- Selection Sort Algorithm
- Merge Sort Algorithm
- Counting Sort Algorithm
- Quick Sort Algorithm

## Graph:
- Kruskal's Algorithm (MST Minimum Spanning Tree)
- Dijkstra's Algorithm
- Bellman Ford Algorithm
- Floyd Warshall Algorithm
- Topological Sort Algorithm
- Flood Fill Algorithm
- Lee Algorithm
- Kahn's Topological Sort Algorithm

## Tree Traversals:
- Inorder
- Preorder
- Postorder

## Arrays:
- Kadane's Algorithm
- Floyd's Cycle Detection Algorithm
- KMP Algorithm
- Quick select Algorithm
- Boyer-Moore Majority Vote Algorithm

## Basics:
- Huffman Coding Compression Algorithm
- Union Find Algorithm
- Euclid's Algorithm



# Algorithm analysis

## Searching
### *Linear search:*

A ***linear*** search or ***sequential*** search seaquentially checks each element of a list until a match is found or the whole list has been searched.

Pseudocode follows:

```
procedure linear_search (list, value)

   for each item in the list
      if match item == value
         return the item's location
      end if
   end for

end procedure
```

Linear search is simple to implement, it can be used whether the array/list is sorted or not and can be used on arrays/lists of any data type.
It's well suited for small datasets but has a time complexity of O(n), which makes it slow for large datasets.

### *Binary search:*
Also known as ***half-interval search***, ***logarithmic search***, or ***binary chop***, is a search algorithm that finds the position of a target value within a **sorted array**.

**Binary search** compares the target value to the middle element of the array. If they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half, again taking the middle element to compare to the target value, and repeating this until the target value is found. If the search ends with the remaining half being empty, the target is not in the array.

Binary Search can be implemented as iterative or recursive method as shown on the pseudocode.

Iteration method:
```
# Iterative method

binarySearch(arr, x, low, high)
        repeat till low = high
               mid = (low + high)/2
                   if (x == arr[mid])
                   return mid
   
                   else if (x > arr[mid]) // x is on the right side
                       low = mid + 1
   
                   else                  // x is on the left side
                       high = mid - 1
```

Recursive method:
```
# Recursive method

binarySearch(arr, x, low, high)
           if low > high
               return False 
   
           else
               mid = (low + high) / 2 
                   if x == arr[mid]
                   return mid
       
               else if x > arr[mid]        // x is on the right side
                   return binarySearch(arr, x, mid + 1, high)
               
               else                        // x is on the left side
                   return binarySearch(arr, x, low, mid - 1) 
```

Faster than linear search, especially for large arrays.
The loogaithmic time in the worst case scenario is O(log n), however the array must be sorted. This adds at least an additional O(n log n) time complexity for the sorting step.

### *Breadth First Search (BFS):*

***Breadth-First Search (BFS)*** is an algorithm for searching a ***tree*** data structure for a node that satisfies a given property.

It starts at the tree root and explores all nodes at the present depth prior to moving on to the nodes at the next depth level.

For a graph Breadth-First Search, to avoid processing a node in a graph cycle more than once, the vertices are divided into two categories:
- Visited
- Not Visited

It is assumed that all vertices are reachable from the starting vertex.
Extra memory, a queue in particular, is needed to keep track of the child nodes that were encountered but not yet explored.

Pseudocode for BFS implementation on a Graph:
```
Breadth_First_Serach( Graph, X ) // Here, Graph is the graph that we already have and X is the source node

Let Q be the queue
Q.enqueue( X ) // Inserting source node X into the queue
Mark X node as visited.

While ( Q is not empty )
Y = Q.dequeue( ) // Removing the front node from the queue

Process all the neighbors of Y, For all the neighbors Z of Y
If Z is not visited, Q. enqueue( Z ) // Stores Z in Q
Mark Z as visited
```

The time complexity is O(V+E) where V is the number of Nodes of Vertices and E is the number of Edges.
The auxiliary space complexity is O(V) in the worst case scenario.


### *Depth First Search (DFS):*

Algorithm used for traversing or searching ***tree*** or ***graph*** data structures. DFS starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.
Extra memory, usually a stack, is needed to keep track of the nodes discovered so far along a specific branch wich helps in backtracking of the graph.
To avoid processing a node more than once, a boolean is used to store the visited nodes.
A graph can have more than one DFS traversal.


```
DFS(G, u)
    u.visited = true
    for each v ∈ G.Adj[u]
        if v.visited == false
            DFS(G,v)
     
init() {
    For each u ∈ G
        u.visited = false
     For each u ∈ G
       DFS(G, u)
}
```
Where u is the root.

The time complexity is O(V+E) where V is the number of Nodes of Vertices and E is the number of Edges.
The auxiliary space complexity is O(V) in the worst case scenario.


## Sorting
### *Insertion Sort:*
***Insertion Sort*** is a sorting algorithm that builds the final sorted array/list one item at a time by comparisons. It's much less efficient on large lists
The time complexity is quadratic O(n^2).
Insertion sort iterates, consuming one input element each repetition, and grows a sorted output list. At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there. It repeats until no input elements remain.

 ```
 procedure insertionSort(A: list of sortable items)
   n = length(A)
   for i = 1 to n - 1 do
       j = i
       while j > 0 and A[j-1] > A[j] do
           swap(A[j], A[j-1])
           j = j - 1
       end while
   end for
end procedure
 ```
 [Insertion Sort](https://www.programiz.com/dsa/insertion-sort)

 ### *Heap Sort:*

Heap sort is a comparison-based sorting technique based on Binary Heap data structure. It is similar to the selection sort where we first find the minimum element and place the minimum element at the beginning. Repeat the same process for the remaining elements.
Pseudocode for Heap Sort:
```
procedure heapsort(a, count) is
    input: an unordered array a of length count
 
    (Build the heap in array a so that largest value is at the root)
    heapify(a, count)

    (The following loop maintains the invariants that a[0:end] is a heap and every element
     beyond end is greater than everything before it (so a[end:count] is in sorted order))
    end ← count - 1
    while end > 0 do
        (a[0] is the root and largest value. The swap moves it in front of the sorted elements.)
        swap(a[end], a[0])
        (the heap size is reduced by one)
        end ← end - 1
        (the swap ruined the heap property, so restore it)
        siftDown(a, 0, end)
```
The sorting routine uses two subroutines, heapify and siftDown. The former is the common in-place heap construction routine, while the latter is a common subroutine for implementing heapify.
Procedure for Heapify function.
```
(Put elements of 'a' in heap order, in-place)
procedure heapify(a, count) is
    (start is assigned the index in 'a' of the last parent node)
    (the last element in a 0-based array is at index count-1; find the parent of that element)
    start ← iParent(count-1)
    
    while start ≥ 0 do
        (sift down the node at index 'start' to the proper place such that all nodes below
         the start index are in heap order)
        siftDown(a, start, count - 1)
        (go to the next parent node)
        start ← start - 1
    (after sifting down the root all nodes/elements are in heap order)

(Repair the heap whose root element is at index 'start', assuming the heaps rooted at its children are valid)
procedure siftDown(a, start, end) is
    root ← start

    while iLeftChild(root) ≤ end do    (While the root has at least one child)
        child ← iLeftChild(root)   (Left child of root)
        swap ← root                (Keeps track of child to swap with)

        if a[swap] < a[child] then
            swap ← child
        (If there is a right child and that child is greater)
        if child+1 ≤ end and a[swap] < a[child+1] then
            swap ← child + 1
        if swap = root then
            (The root holds the largest element. Since we assume the heaps rooted at the
             children are valid, this means that we are done.)
            return
        else
            Swap(a[root], a[swap])
            root ← swap          (repeat to continue sifting down the child now)
```
The time complexity of Heap Sort is O(n log n).

[Heap Sort](https://www.programiz.com/dsa/heap-sort)

### *Selection Sort:*

Selection sort is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list. The algorithm repeatedly selects the smallest (or largest) element from the unsorted portion of the list and swaps it with the first element of the unsorted portion. This process is repeated for the remaining unsorted portion of the list until the entire list is sorted. One variation of selection sort is called “Bidirectional selection sort” that goes through the list of elements by alternating between the smallest and largest element, this way the algorithm can be faster in some cases.

The algorithm maintains two subarrays in a given array.
- The subarray which already sorted. 
- The remaining subarray was unsorted.

The time complexity is O(n^2) in the worst case scenario for the comparisons and O(n) for swaps.

```
procedure selection sort 
   list  : array of items
   n     : size of list

   for i = 1 to n - 1
   /* set current element as minimum*/
      min = i    
  
      /* check the element to be minimum */

      for j = i+1 to n 
         if list[j] < list[min] then
            min = j;
         end if
      end for

      /* swap the minimum element with the current element*/
      if indexMin != i  then
         swap list[min] and list[i]
      end if
   end for
	
end procedure
```

[Selection Sort](https://www.programiz.com/dsa/selection-sort)

### *Merge Sort:*

Merge sort is a sorting algorithm that works by dividing an array into smaller subarrays, sorting each subarray, and then merging the sorted subarrays back together to form the final sorted array.

In simple terms, we can say that the process of merge sort is to divide the array into two halves, sort each half, and then merge the sorted halves back together. This process is repeated until the entire array is sorted.
The algorithm explained:
```
step 1: start

step 2: declare array and left, right, mid variable

step 3: perform merge function.
    if left > right
        return
    mid= (left+right)/2
    mergesort(array, left, mid)
    mergesort(array, mid+1, right)
    merge(array, left, mid, right)

step 4: Stop
```

Top Down pseudocode:
```
function merge_sort(list m) is
    // Base case. A list of zero or one elements is sorted, by definition.
    if length of m ≤ 1 then
        return m

    // Recursive case. First, divide the list into equal-sized sublists
    // consisting of the first half and second half of the list.
    // This assumes lists start at index 0.
    var left := empty list
    var right := empty list
    for each x with index i in m do
        if i < (length of m)/2 then
            add x to left
        else
            add x to right

    // Recursively sort both sublists.
    left := merge_sort(left)
    right := merge_sort(right)

    // Then merge the now-sorted sublists.
    return merge(left, right)
```

Bottom up implementation pseudocode:
```
function merge_sort(node head) is
    // return if empty list
    if head = nil then
        return nil
    var node array[32]; initially all nil
    var node result
    var node next
    var int  i
    result := head
    // merge nodes into array
    while result ≠ nil do
        next := result.next;
        result.next := nil
        for (i = 0; (i < 32) && (array[i] ≠ nil); i += 1) do
            result := merge(array[i], result)
            array[i] := nil
        // do not go past end of array
        if i = 32 then
            i -= 1
        array[i] := result
        result := next
    // merge array into single list
    result := nil
    for (i = 0; i < 32; i += 1) do
        result := merge(array[i], result)
    return result
```

Time complexity of Merge Sort is O(n log n) in the worst case scenario.

[Merge Sort](https://www.programiz.com/dsa/merge-sort)


### *Counting Sort:*

Counting sort is an algorithm for sorting a collection of objects according to keys that are small positive integers; that is, it is an integer sorting algorithm.
Counting sort is a sorting technique based on keys between a specific range. It works by counting the number of objects having distinct key values (a kind of hashing). Then do some arithmetic operations to calculate the position of each object in the output sequence. 

```
function CountingSort(input, k)
    
    count ← array of k + 1 zeros
    output ← array of same length as input
    
    for i = 0 to length(input) - 1 do
        j = key(input[i])
        count[j] = count[j] + 1

    for i = 1 to k do
        count[i] = count[i] + count[i - 1]

    for i = length(input) - 1 down to 0 do
        j = key(input[i])
        count[j] = count[j] - 1
        output[count[j]] = input[i]

    return output
```

Time complexity of Counting sort is O(n+k) where k is the range of the non-negative key values.

[Counting Sort](https://www.programiz.com/dsa/counting-sort)

### *Quick Sort:*

QuickSort is a Divide and Conquer algorithm. It picks an element as a pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways. 
- Always pick the first element as a pivot.
- Always pick the last element as a pivot (implemented below)
- Pick a random element as a pivot.
- Pick median as the pivot.
The key process in quickSort is a partition(). The target of partitions is, given an array and an element x of an array as the pivot, put x at its correct position in a sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time.

Pseudocode for recursive Quick Sort function:

```
/* low  –> Starting index,  high  –> Ending index */

quickSort(arr[], low, high) {

    if (low < high) {

        /* pi is partitioning index, arr[pi] is now at right place */

        pi = partition(arr, low, high);

        quickSort(arr, low, pi – 1);  // Before pi

        quickSort(arr, pi + 1, high); // After pi

    }

}
```

Pseudocode for the partition function:
```
/* This function takes last element as pivot, places the pivot element at its correct position in sorted array, and places all smaller (smaller than pivot) to left of pivot and all greater elements to right of pivot */

partition (arr[], low, high)
{
    // pivot (Element to be placed at right position)
    pivot = arr[high];  

    i = (low – 1)  // Index of smaller element and indicates the 
    // right position of pivot found so far

    for (j = low; j <= high- 1; j++){

        // If current element is smaller than the pivot
        if (arr[j] < pivot){
            i++;    // increment index of smaller element
            swap arr[i] and arr[j]
        }
    }
    swap arr[i + 1] and arr[high])
    return (i + 1)
}
```

[Quick Sort](https://www.programiz.com/dsa/quick-sort)

## Graph
### *Kruskal's Algorithm:*

Kruskal's algorithm is a minimum spanning tree algorithm that takes a graph as input and finds the subset of the edges of that graph which
- form a tree that includes every vertex
- has the minimum sum of weights among all the trees that can be formed from the graph

It falls under a class of algorithms called greedy algorithms that find the local optimum in the hopes of finding a global optimum.

We start from the edges with the lowest weight and keep adding edges until we reach our goal.

The steps for implementing Kruskal's algorithm are as follows:

- Sort all the edges from low weight to high
- Take the edge with the lowest weight and add it to the spanning tree. If adding the edge created a cycle, then reject this edge.
- Keep adding edges until we reach all vertices.

Pseudocode:
```
KRUSKAL(G):
A = ∅
For each vertex v ∈ G.V:
    MAKE-SET(v)
For each edge (u, v) ∈ G.E ordered by increasing order by weight(u, v):
    if FIND-SET(u) ≠ FIND-SET(v):       
    A = A ∪ {(u, v)}
    UNION(u, v)
return A
```

The time complexity Of Kruskal's Algorithm is: O(E log E).

[Kruskal's Algorithm](https://www.programiz.com/dsa/kruskal-algorithm)


### *Dijkstra's Algorithm:*

Dijkstra's algorithm allows us to find the shortest path between any two vertices of a graph.

It differs from the minimum spanning tree because the shortest distance between two vertices might not include all the vertices of the graph

Dijkstra's Algorithm works on the basis that any subpath B -> D of the shortest path A -> D between vertices A and D is also the shortest path between vertices B and D.

Djikstra used this property in the opposite direction i.e we overestimate the distance of each vertex from the starting vertex. Then we visit each node and its neighbors to find the shortest subpath to those neighbors.

The algorithm uses a greedy approach in the sense that we find the next best solution hoping that the end result is the best solution for the whole problem.

Pseudocode:
```
function dijkstra(G, S)
    for each vertex V in G
        distance[V] <- infinite
        previous[V] <- NULL
        If V != S, add V to Priority Queue Q
    distance[S] <- 0
	
    while Q IS NOT EMPTY
        U <- Extract MIN from Q
        for each unvisited neighbour V of U
            tempDistance <- distance[U] + edge_weight(U, V)
            if tempDistance < distance[V]
                distance[V] <- tempDistance
                previous[V] <- U
    return distance[], previous[]
```

Time Complexity: O(E Log V)

where, E is the number of edges and V is the number of vertices.

Space Complexity: O(V)

[Dijkstra's Algorithm](https://www.programiz.com/dsa/dijkstra-algorithm)


### *Bellman Ford's Algorithm:*

Bellman Ford algorithm helps us find the shortest path from a vertex to all other vertices of a weighted graph.

It is similar to Dijkstra's algorithm but it can work with graphs in which edges can have negative weights.

Pseudocode:
```
function bellmanFord(G, S)
  for each vertex V in G
    distance[V] <- infinite
      previous[V] <- NULL
  distance[S] <- 0

  for each vertex V in G				
    for each edge (U,V) in G
      tempDistance <- distance[U] + edge_weight(U, V)
      if tempDistance < distance[V]
        distance[V] <- tempDistance
        previous[V] <- U

  for each edge (U,V) in G
    If distance[U] + edge_weight(U, V) < distance[V}
      Error: Negative Cycle Exists

  return distance[], previous[]
```

The time complexity on worst case scenario O(VE).

[Bellman Ford's Algorithm](https://www.programiz.com/dsa/bellman-ford-algorithm)


### *Floyd-Warshall Algorithm:*

Floyd-Warshall Algorithm is an algorithm for finding the shortest path between all the pairs of vertices in a weighted graph. This algorithm works for both the directed and undirected weighted graphs. But, it does not work for the graphs with negative cycles (where the sum of the edges in a cycle is negative)

This algorithm follows the dynamic programming approach to find the shortest paths.

Pseudocode:
```
n = no of vertices
A = matrix of dimension n*n
for k = 1 to n
    for i = 1 to n
        for j = 1 to n
            Ak[i, j] = min (Ak-1[i, j], Ak-1[i, k] + Ak-1[k, j])
return A
```

[Floyd-Warshall Algorithm](https://www.programiz.com/dsa/floyd-warshall-algorithm)


### *Topological Sorting for Directed Acyclic Graph (DAG):*

Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u v, vertex u comes before v in the ordering.

Topological Sorting for a graph is not possible if the graph is not a DAG.

Any DAG has at least one topological ordering, and algorithms are known for constructing a topological ordering of any DAG in linear time. Topological sorting has many applications especially in ranking problems such as feedback arc set. Topological sorting is possible even when the DAG has disconnected components.

We can modify DFS to find the Topological Sorting of a graph. 
In DFS, 
- We start from a vertex, we first print it, and then 
- Recursively call DFS for its adjacent vertices. 
In topological sorting,

- We use a temporary stack. 
- We don’t print the vertex immediately, 
- we first recursively call topological sorting for all its adjacent vertices, then push it to a stack. 
- Finally, print the contents of the stack.

Time Complexity: O(V + E) The above algorithm is simply DFS with a working stack and a result stack. Unlike the recursive solution, recursion depth is not an issue here.
Auxiliary space: O(V), The extra space is needed for the 2 stacks used

[Topological Sorting for Directed Acyclic Graph (DAG)](https://www.geeksforgeeks.org/topological-sorting/)


### *Flood Fill Algorithm:*

Flood fill, also called seed fill, is a flooding algorithm that determines and alters the area connected to a given node in a multi-dimensional array with some matching attribute.

BFS Approach: The idea is to use BFS traversal to replace the color with the new color. 

Create an empty queue lets say Q.
Push the starting location of the pixel as given in the input and apply replacement color to it.
Iterate until Q is not empty and pop the front node (pixel position).
Check the pixels adjacent to the current pixel and push into the queue if valid (had not been colored with replacement color and have the same color as the old color).


[Flood Fill Algorithm](https://www.geeksforgeeks.org/flood-fill-algorithm/)


### *Lee Algorithm:*

The algorithm, also known as Shortest path in a Binary Maze, is a breadth-first based algorithm that uses queues to store the steps. It usually uses the following steps:

Choose a starting point and add it to the queue.
Add the valid neighboring cells to the queue.
Remove the position you are on from the queue and continue to the next element.
Repeat steps 2 and 3 until the queue is empty.

Given an MxN matrix where each element can either be 0 or 1. We need to find the shortest path between a given source cell to a destination cell. The path can only be created out of a cell if its value is 1.

Lee algorithm uses BFS.  

We start from the source cell and call the BFS procedure.
We maintain a queue to store the coordinates of the matrix and initialize it with the source cell.
We also maintain a Boolean array visited of the same size as our input matrix and initialize all its elements to false.
We LOOP till queue is not empty
Dequeue front cell from the queue
Return if the destination coordinates have been reached.
For each of its four adjacent cells, if the value is 1 and they are not visited yet, we enqueue it in the queue and also mark them as visited

[Lee Algorithm](https://www.geeksforgeeks.org/shortest-path-in-a-binary-maze/)

### *Kahn's Topological Sorting Algorithm:*

Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge uv, vertex u comes before v in the ordering. Topological Sorting for a graph is not possible if the graph is not a DAG.

Time Complexity: O(V+E). 
The outer for loop will be executed V number of times and the inner for loop will be executed E number of times.
Auxiliary Space: O(V). 
The queue needs to store all the vertices of the graph. So the space required is O(V)

[Kahn's Topological Sorting Algorithm](https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/)


## *Tree Traversals*

Traversing a tree means visiting every node in the tree. You might, for instance, want to add all the values in the tree or find the largest one. For all these operations, you will need to visit each node of the tree.

Linear data structures like arrays, stacks, queues, and linked list have only one way to read the data. But a hierarchical data structure like a tree can be traversed in different ways.

[Tree Traversals](https://www.programiz.com/dsa/tree-traversal)

### *Pre Order:*

Visit root node
Visit all the nodes in the left subtree
Visit all the nodes in the right subtree

### *In Order:*

First, visit all the nodes in the left subtree
Then the root node
Visit all the nodes in the right subtree

### *Post Order:*

Visit all the nodes in the left subtree
Visit all the nodes in the right subtree
Visit the root node


## Arrays

### *Kadane's Algorithm:*

Dynamic Programming is a method for solving a complex problem by breaking it down into a collection of simpler subproblems, solving each of those subproblems just once, and storing their solutions using a memory-based data structure (array, map, etc.). So the next time the same sub-problem occurs, instead of recomputing its solution, one simply looks up the previously computed solution, thereby saving computation time.

The idea of Kadane’s algorithm is to maintain a variable max_ending_here that stores the maximum sum contiguous subarray ending at current index and a variable max_so_far stores the maximum sum of contiguous subarray found so far, Everytime there is a positive-sum value in max_ending_here compare it with max_so_far and update max_so_far if it is greater than max_so_far.

Pseudocode:

```
Initialize:
    max_so_far = INT_MIN
    max_ending_here = 0

Loop for each element of the array

  (a) max_ending_here = max_ending_here + a[i]
  (b) if(max_so_far < max_ending_here)
            max_so_far = max_ending_here
  (c) if(max_ending_here < 0)
            max_ending_here = 0
return max_so_far
```

[Kadane's Algorithm](https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/)


### *Floyd's Cycle Detection Algorithm:*

Floyd’s cycle finding algorithm or Hare-Tortoise algorithm is a pointer algorithm that uses only two pointers, moving through the sequence at different speeds. This algorithm is used to find a loop in a linked list. It uses two pointers one moving twice as fast as the other one. The faster one is called the faster pointer and the other one is called the slow pointer.

While traversing the linked list one of these things will occur-

The Fast pointer may reach the end (NULL) this shows that there is no loop in the linked list.
The Fast pointer again catches the slow pointer at some time therefore a loop exists in the linked list.

- Initialize two-pointers and start traversing the linked list.
- Move the slow pointer by one position.
- Move the fast pointer by two positions.
- If both pointers meet at some point then a loop exists and if the fast pointer meets the end position then no loop exists.

Time complexity: O(n), as the loop is traversed once.
Auxiliary Space: O(1), only two pointers are used therefore constant space complexity.


[Floyd's Cycle Detection Algorithm](https://www.geeksforgeeks.org/floyds-cycle-finding-algorithm/)


### *KMP Algorithm:*

Pattern searching is an important problem in computer science. When we do search for a string in a notepad/word file or browser or database, pattern-searching algorithms are used to show the search results. We have discussed the Naive pattern-searching algorithm in the previous post. 
The worst-case complexity of the Naive algorithm is O(m(n-m+1)). The time complexity of the KMP algorithm is O(n) in the worst case. KMP (Knuth Morris Pratt) Pattern Searching.

The KMP matching algorithm uses degenerating property (pattern having the same sub-patterns appearing more than once in the pattern) of the pattern and improves the worst-case complexity to O(n). 

The basic idea behind KMP’s algorithm is: whenever we detect a mismatch (after some matches), we already know some of the characters in the text of the next window. We take advantage of this information to avoid matching the characters that we know will anyway match. 

[KMP Algorithm for Pattern Searching](https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/)


### *Quick select Algorithm:*

Quickselect is a selection algorithm to find the k-th smallest element in an unordered list. It is related to the quick sort sorting algorithm.

The algorithm is similar to QuickSort. The difference is, instead of recurring for both sides (after finding pivot), it recurs only for the part that contains the k-th smallest element. The logic is simple, if index of the partitioned element is more than k, then we recur for the left part. If index is the same as k, we have found the k-th smallest element and we return. If index is less than k, then we recur for the right part. This reduces the expected complexity from O(n log n) to O(n), with a worst-case of O(n^2).

Pseudocode:

```
function quickSelect(list, left, right, k)

   if left = right
      return list[left]

   Select a pivotIndex between left and right

   pivotIndex := partition(list, left, right, 
                                  pivotIndex)
   if k = pivotIndex
      return list[k]
   else if k < pivotIndex
      right := pivotIndex - 1
   else
      left := pivotIndex + 1 
```

[Quick Select Algorithm](https://www.geeksforgeeks.org/quickselect-algorithm/)

### *Boyer-Moore Majority Vote Algorithm:*

The Boyer-Moore voting algorithm is one of the popular optimal algorithms which is used to find the majority element among the given elements that have more than N/ 2 occurrences. This works perfectly fine for finding the majority element which takes 2 traversals over the given elements, which works in O(N) time complexity and O(1) space complexity.

This algorithm works on the fact that if an element occurs more than N/2 times, it means that the remaining elements other than this would definitely be less than N/2. So let us check the proceeding of the algorithm.

First, choose a candidate from the given set of elements if it is the same as the candidate element, increase the votes. Otherwise, decrease the votes if votes become 0, select another new element as the new candidate.

[Boyer-Moore Majority Vote Algorithm](https://www.geeksforgeeks.org/boyer-moore-majority-voting-algorithm/)


## Basics

### *Huffman Coding Compression Algorithm:*

Huffman Coding is a technique of compressing data to reduce its size without losing any of the details. It was first developed by David Huffman.

Huffman Coding is generally useful to compress the data in which there are frequently occurring characters.
Each character occupies 8 bits. There are a total of 15 characters in the above string. Thus, a total of 8 * 15 = 120 bits are required to send this string.

Using the Huffman Coding technique, we can compress the string to a smaller size.

Huffman coding first creates a tree using the frequencies of the character and then generates code for each character.

Once the data is encoded, it has to be decoded. Decoding is done using the same tree.

Huffman Coding prevents any ambiguity in the decoding process using the concept of prefix code ie. a code associated with a character should not be present in the prefix of any other code. The tree created above helps in maintaining the property.

Pseudocode:

```
create a priority queue Q consisting of each unique character.
sort then in ascending order of their frequencies.
for all the unique characters:
    create a newNode
    extract minimum value from Q and assign it to leftChild of newNode
    extract minimum value from Q and assign it to rightChild of newNode
    calculate the sum of these two minimum values and assign it to the value of newNode
    insert this newNode into the tree
return rootNode
```

The time complexity for encoding each unique character based on its frequency is O(nlog n).

Extracting minimum frequency from the priority queue takes place 2*(n-1) times and its complexity is O(log n). Thus the overall complexity is O(nlog n).

[Huffman Coding Compression Algorithm](https://www.programiz.com/dsa/huffman-coding)


### *Union Find Algorithm:*

A union-find algorithm is an algorithm that performs two useful operations on such a data structure:

Find: Determine which subset a particular element is in. This can be used for determining if two elements are in the same subset.
Union: Join two subsets into a single subset. Here first we have to check if the two subsets belong to same set. If no, then we cannot perform union. 

Note that the implementation of union() and find() is naive and takes O(n) time in the worst case.
Auxiliary Space: O(1).

[Union Find Algorithm](https://www.geeksforgeeks.org/introduction-to-disjoint-set-data-structure-or-union-find-algorithm/)


### *Euclid's Algorithm:*

The Euclidean algorithm is a way to find the greatest common divisor of two positive integers. GCD of two numbers is the largest number that divides both of them. A simple way to find GCD is to factorize both numbers and multiply common prime factors.

The algorithm is based on the below facts. 

If we subtract a smaller number from a larger one (we reduce a larger number), GCD doesn’t change. So if we keep subtracting repeatedly the larger of two, we end up with GCD.
Now instead of subtraction, if we divide the smaller number, the algorithm stops when we find the remainder 0.

The extended Euclidean algorithm updates the results of gcd(a, b) using the results calculated by the recursive call gcd(b%a, a). Let values of x and y calculated by the recursive call be x1 and y1. x and y are updated using the below expressions.

Time Complexity: O(log N)
Auxiliary Space: O(log N)

[Euclidean Algorithm](https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/)

### *Fermat's little theorem:*

Fermat's little theorem states that p is a prime number, then for any integer a, the number a^p - a is an integer multiple of p.
a^p is equivalent to a(mod p).

```
// returns a^b mod(MOD) (a to the power b mod MOD)
func modular_exponentiation(a, b, MOD)
	ans = 1
	a = a mod(MOD)
	while b is more than 0
		if b is an odd number
			ans = (ans * a) mod(MOD)
		a = (a * a) mod(MOD)
		b = b / 2
	return ans
// it’s assumed that input m is a prime number
print(modular_exponentiation(a, m-2, m))
```

[Fermat's little theorem](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem)


# Thanks to

[Wikipedia](https://en.wikipedia.org)

[Geeks for Geeks](https://www.geeksforgeeks.org/)

[Programiz](https://www.programiz.com/)