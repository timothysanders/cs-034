# Chapter 11: Heaps and Treaps

### 11.1: Heaps
#### Heap concept
- Some applications will need access to and removal of the maximum item in a set of items. In these instances, maintaining fully sorted orders requires more work than necessary, and a **max-heap** may be an appropriate data structure.
- A **max-heap** is a complete binary tree that maintains the property that a node's key is greater than or equal to the node's children's keys. This means that the node key is equal to or greater than all of its descendant's keys. This means that the max-heap's root is always the maximum key in the entire tree.
- ![Sample max-heap](images/figure-11.1.1.png)
#### Max-heap insert and remove operations
- An **insert** into a max-heap starts by inserting the node into the tree's last level, then swapping the node with its parent until no max-heap property violations occur
- Inserts fill a level left-to-right before adding another level, to keep the tree at the minimum height possible
- The upward swapping of nodes in a max-heap is called **percolating**
- A **remove** from a max-heap is always a removal of the root, and is done by replacing the root with the last level's last node, and then swapping that node with its greatest child until no max-heap property violations occur
#### Min-heap
- A **min-heap** is similar to a max-heap, but a node's key is less than or equal to all of its children's keys

### 11.2 Heaps using arrays
#### Heap storage
- Heaps are typically stored with arrays, with the heap's array form produced by traversing the tree levels from left to right and top to bottom. The root node is always at index 0, the root's left child at index 1, right child at index 2, etc.
#### Parent and child indices
- Because heaps are not implemented with node structures and parent/child pointers, traversing from a node to parent/child nodes requires referring to nodes by index
- Parent and child indices for a heap

| Node index | Parent index            | Child indices  |
|------------|-------------------------|----------------|
| 0          | N/A                     | 1, 2           |
| 1          | 0                       | 3, 4           |
| 2          | 0                       | 5, 6           |
| 3          | 1                       | 7, 8           |
| 4          | 1                       | 9, 10          |
| 5          | 2                       | 11, 12         |
| ...        | ...                     | ...            |
| i          | $\lfloor(i-1)/2\rfloor$ | $2*i+1, 2*i+2$ |
#### Percolate algorithm
- Below is the pseudocode for array-based percolate-up and percolate-down functions for a max heap
##### Max-heap percolate up
```
MaxHeapPercolateUp(nodeIndex, heapArray) {
   while (nodeIndex > 0) {
      parentIndex = (nodeIndex - 1) / 2
      if (heapArray[nodeIndex] <= heapArray[parentIndex])
         return
      else {
         swap heapArray[nodeIndex] and heapArray[parentIndex]
         nodeIndex = parentIndex
      }
   }
}
```
##### Max-heap percolate down
```
MaxHeapPercolateDown(nodeIndex, heapArray, arraySize) {
   childIndex = 2 * nodeIndex + 1
   value = heapArray[nodeIndex]

   while (childIndex < arraySize) {
      // Find the max among the node and all the node's children
      maxValue = value
      maxIndex = -1
      for (i = 0; i < 2 && i + childIndex < arraySize; i++) {
         if (heapArray[i + childIndex] > maxValue) {
            maxValue = heapArray[i + childIndex]
            maxIndex = i + childIndex
         }
      }

      if (maxValue == value) {
         return
      }
      else {
         swap heapArray[nodeIndex] and heapArray[maxIndex]
         nodeIndex = maxIndex
         childIndex = 2 * nodeIndex + 1
      }
   }
}
```

### 11.3: Python - Heaps
#### Heaps and the MaxHeap class
- Each level of a max heap grows left to right, and new levels are added only after the current level is completely full. This means an array implementation is efficient, the root is always at index 0, and indexes of parent/child nodes can be easily calculated
  - `parent_index`: `(node_index - 1) // 2`
  - `left_child_index`: `2 * node_index + 1`
  - `right_child_index`: `2 * node_index + 2`
- No actual node class is used, but the elements of the list are still called nodes

### 11.4: Heap sort
#### Heapify operation
- **Heapsort** is a sorting algorithm that takes advantage of a max-heap's properties by repeatedly removing the max and building a sorted array in reverse order. However, the unsorted array must be first converted into a heap, using the **heapify** operation
- Heapify operation starts on the internal node with the largest index and continues down to, and including, the root node at index 0. For a binary tree with N nodes, the largest internal node index is $\lfloor N/2 \rfloor - 1$

| Number of nodes in binary heap | Largest internal node index |
|--------------------------------|-----------------------------|
| 1                              | -1 (no internal nodes)      |
| 2                              | 0                           |
| 3                              | 0                           |
| 4                              | 1                           |
| 5                              | 1                           |
| 6                              | 2                           |
| 7                              | 2                           |
| ...                            | ...                         |
| N                              | $\lfloor N/2 \rfloor - 1$   |
#### Heapsort overview
- Heapsort begins by heapifying the array into a max-heap and using an end index value of the size of the array minus 1. Heapsort repeatedly removes the max value, stores that value at the end index, and decrements the end index, repeating until the end index is 0
#### Heapsort algorithm
- Heapsort uses 2 loops to sort an array, the first heapifies the array using MaxHeapPercolateDown and the second loop removes the maximum value, stores it at the end index and decrements the end index (until it is 0)
```
Heapsort(numbers, numbersSize) {
   // Heapify numbers array
   for (i = numbersSize / 2 - 1; i >= 0; i--) {
      MaxHeapPercolateDown(i, numbers, numbersSize)
   }

   for (i = numbersSize - 1; i > 0; i--) {
      Swap numbers[0] and numbers[i]
      MaxHeapPercolateDown(0, numbers, i)
   }
}
```

### 11.6: Priority queue abstract data type (ADT)
#### Priority queue abstract data type
- A **priority queue** is a queue where each item has a priority and items with higher priorities are closer to the front than items with lower priorities. The **enqueue** operation inserts an item so that it is closer to the front than all items of a lower priority and closer to the end than all items of equal or higher priority. The **dequeue** operation removes and returns an item at the front of the queue (with the highest priority).
#### Common priority queue operations
- In addition to enqueue and dequeue, priority queues usually support peek/length querying. **Peek** returns the highest priority item, without removing it from the front of the queue.

| Operation          | Description                                                 | Example starting with priority queue: 42, 61, 98 (front is 42) |
|--------------------|-------------------------------------------------------------|----------------------------------------------------------------|
| Enqueue(PQueue, x) | Inserts x after all equal or higher priority items          | Enqueue(PQueue, 87). PQueue: 42, 61, 87, 98                    |
| Dequeue(PQueue)    | Returns and removes the item at the front of PQueue         | Dequeue(PQueue) returns 42. PQueue: 61, 98                     |
| Peek(PQueue)       | Returns but does not remove the item at the front of PQueue | Peek(PQueue) returns 42. PQueue: 42, 61, 98                    |
| IsEmpty(PQueue)    | Returns true if PQueue has no items                         | IsEmpty(PQueue) returns false.                                 |
| GetLength(PQueue)  | Returns the number of items in PQueue                       | GetLength(PQueue) returns 3.                                   |
#### Enqueueing items with priority
- A priority queue can be implemented such that each item's priority can be determined from the item itself, and a priority queue can be implemented with an **EnqueueWithPriority** operation
#### Implementing priority queues with heaps
- A priority queue is often implemented with a heap, which keeps the highest priority item as the root node and allows access in O(1) time. Adding or removing items from the queue operates in a worst-case O(log N) time

| Priority queue operation | Heap functionality used to implement operation                           | Worst-case runtime complexity |
|--------------------------|--------------------------------------------------------------------------|-------------------------------|
| Enqueue                  | Insert                                                                   | O($\log N$)                   |
| Dequeue                  | Remove                                                                   | O($\log N$)                   |
| Peek                     | Return value in root node                                                | O(1)                          |
| IsEmpty                  | Return true if no nodes in heap, false otherwise                         | O(1)                          |
| GetLength                | Return number of nodes (expected to be stored in the heap's member data) | O(1)                          |

### 11.7: Treaps
#### Treap basics
- A BST built from inserts of N nodes having random-ordered keys stays well-balanced and has near-minimum height, which means searches, inserts, and deletions are O(log N). However, insertion order may not always be random, so we need a data structure that randomizes BST inserts. A **treap** (combines "tree" and "heap") uses a main key that maintains the BST ordering property, and a secondary key generated randomly (often called "priority") during insertions that maintains a heap property. This combination usually keeps the tree balanced
- Basic treap operations
  - **search**: same as BST search using the main key
  - **insert**: initially inserts a node as in a BST using the main key, then assigns a random priority to the node, and percolates the node up until the heap property is not violated. In a treap, a node is moved up via a rotation at the parent, which maintains the BST property
  - **delete**: done by setting the node's priority such that the node should be a leaf, percolating the node down using rotations until the node is a left, and then removing the node
#### Treap delete
- Treap deletes can be done by first doing a BST delete (copying successor node to the node-to-delete, then deleting original successor), followed by percolating the node down until the heap properties are not violated
- A simpler approach is to set the node-to-delete's priority to negative infinity (for a max-heap), percolate the node down until it is a leaf, then removing the node