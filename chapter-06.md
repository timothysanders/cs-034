# Chapter 6: Lists

### 6.1: List abstract data type (ADT)
#### List abstract data type
- A **list** is a common ADT for holding ordered data and typically has operations like append, remove, search if an item exists, and print. Lists commonly hold items like integers, strings, or entire objects.
#### Common list ADT operations

| Operation               | Description                              | Example starting with list: 99, 77                                  |
|-------------------------|------------------------------------------|---------------------------------------------------------------------|
| Append(list, x)         | Inserts x at end of list                 | Append(list, 44), list: 99, 77, 44                                  |
| Prepend(list, x)        | Inserts x at start of list               | Prepend(list, 44), list: 44, 99, 77                                 |
| InsertAfter(list, w, x) | Inserts x after w                        | InsertAfter(list, 99, 44), list: 99, 44, 77                         |
| Remove(list, x)         | Removes x                                | Remove(list, 77), list: 99                                          |
| Search(list, x)         | Returns item if found, else returns null | Search(list, 99), returns item 99<br>Search(list, 22), returns null |
| Print(list)             | Prints list's items in order             | Print(list) outputs: 99, 77                                         |
| PrintReverse(list)      | Prints list's items in reverse order     | PrintReverse(list) outputs: 77, 99                                  |
| Sort(list)              | Sorts the lists items in ascending order | list becomes: 77, 99                                                |
| IsEmpty(list)           | Returns true if list has no items        | For list 99, 77, IsEmpty(list) returns false                        |
| GetLength(list)         | Returns the number of items in the list  | GetLength(list) returns 2                                           |

### 6.1: Singly-linked lists
#### Singly-linked list data structure
- A **singly-linked list** is a data structure for implementing a list ADT, each node has data and a point to the next node. The list structure itself usually has pointers to the lists first node and last node. The first node is called the **head** and the last node is the **tail**.  These singly-linked lists are a type of **positional list**, which are lists where elements contain pointers to the next and/or previous elements in the list
##### null
- **null** is a special value indicating a pointer points to nothing. The name that is used to represent a pointer/reference that points to nothing may change between programming languages
#### Appending a node to a singly-linked list
- The **append** operation for a singly-linked list inserts a new node after the list's tail node
  - *Append to empty list*: If the list's head pointer is null/empty, the algorithm points the list's head and tail pointers to the new node
  - *Append to non-empty list*: If the list's head pointer is not null/not empty, the algorithm points the tail node's next point and the list's tail pointer to the new node
#### Prepending a node to a singly-linked list
- The **prepend** operation for a singly-linked list inserts a new node before the list's head node. The prepend algorithm is different if the list is empty vs non-empty
  - *Prepend to empty list*: If the list's head point is null/empty, the algorithm points the list's head and tail pointers to the new node
  - *Prepend to non-empty list*: If the list's head point is not null/not empty, the algorithm points the new node's next point to the head node, and then points the list's head pointer to the new node
##### Challenge Activity
- What is numList after the following operations?
  - numList = new List
  - ListAppend(numList, node 34)
  - ListAppend(numList, node 13)
  - ListAppend(numList, node 66)
  - ListAppend(numList, node 15)
  - Answer: 34, 13, 66, 15
- What is numList after the following operations?
  - numList = new List
  - ListPrepend(numList, node 74)
  - ListPrepend(numList, node 19)
  - ListPrepend(numList, node 87)
  - Answer: 87, 19, 74
- What is numList after the following operations?
  - numList = new List
  - ListPrepend(numList, node 76)
  - ListAppend(numList, node 99)
  - ListAppend(numList, node 74)
  - Answer: 76, 99, 74
- After ListAppend(numList, node 62), determine the following values. Enter null if the pointer is null.
- After ListPrepend(numList, node 90), determine the following values. Enter null if the pointer is null.
  - numList's head pointer points to node: 90
  - numList's tail pointer points to node: 75
  - node 90's next pointer points to node: 94
  - node 75's next pointer points to node: null

### 6.3: Singly-linked lists: Insert
- Given a new node, the **insertAfter** operation inserts a new node after the provided existing list node. `curNode` is a pointer to an existing list node, but can be null if the list is empty. There are three insertion scenarios
  - *Insert as list's first node*: If the list's head pointer is null, the algorithm points the list's head and tail pointers to the new node
  - *Insert after list's tail node*: If the list's head pointer is not null (list not empty) and curNode points to the list's tail node, the algorithm points the tail node's next pointer and the list's tail pointer to the new node
  - *Insert in middle of list*: If the list's head pointer is not null (list not empty) and curNode does not point to the list's tail node, the algorithm points the new node's next pointer to curNode's next node, and then points curNode's next pointer to the new node
##### Challenge Activity
- What is numList after the following operations?
  - numList: 53, 55
  - ListInsertAfter(numList, node 53, node 47)
  - ListInsertAfter(numList, node 47, node 38)
  - ListInsertAfter(numList, node 55, node 31)
  - ListInsertAfter(numList, node 55, node 43)
  - Answer: 53, 47, 38, 55, 43, 31
- What is numList after the following operations?
  - numList = new List
  - ListInsertAfter(numList, list head, node 76)
  - ListInsertAfter(numList, list tail, node 85)
  - ListInsertAfter(numList, list tail, node 92)
  - Answer: 76, 85, 92
- What is numList after the following operations?
  - numList = new List
  - ListInsertAfter(numList, list head, node 66)
  - ListInsertAfter(numList, list tail, node 25)
  - ListInsertAfter(numList, list tail, node 83)
  - ListInsertAfter(numList, node 66, node 93)
  - Answer: 66, 93, 25, 83

### 6.4: Singly-linked lists: Remove
- Given an existing node, **removeAfter** operation removes the node after the specified list node. The existing node must be specified because each node in a singly linked list only maintains a pointer to the next node. The existing node is specified with curNode, if curNode is null, removeAfter removes the list's first node. Otherwise, the algorithm removes the node after curNode
  - *Remove list's head node (special case)*: If curNode is null, the algorithm points sucNode to the head node's next node and points the list's head pointer to sucNode. If sucNode is null, the only list node was removed, so the list's tail pointer is pointed to null (indicating the list is now empty)
  - *Remove node after curNode*: If curNode's next pointer is not null (a node after curNode exists), the algorithm points sucNode to the node after curNode's next node. Then curNode's next pointer is pointed to sucNode. If sucNode is null, the list's tail node was removed, so the algorithm points the list's tail pointer to curNode (the new tail node)
##### Challenge Activity
- Given list: [4, 8, 5, 6, 9, 7] What list results from the following operations?
  - ListRemoveAfter(list, null)
  - ListRemoveAfter(list, node 8)
  - ListRemoveAfter(list, node 9)
  - Answer: 8, 6, 9
- Given list: [9, 4, 7, 1] Select the value of the list's head pointer after each operation.

### 6.5: Linked list search
- Given a key, a **search** algorithm returns the first node that matches that key, or returns null if a matching node was not found. Simple linked list search algorithms check the current node (initially the head node), returning that node if a match is found, or pointing the current node to the next node and repeating

### 6.6: Python - Singly-linked lists
- For the implementation of the singly-linked list in Python, see [src/linkedlist.py](src/linkedlist.py)
#### Constructing the node and list class
- Classes are used for the linked list and the nodes that comprise the list. Each class includes references to nodes (next node for node class and head and tail nodes for the LinkedList class)
- The Node class implements a list node with two data members, a data value and the next node in the list. If the node has no next value, the next data member is assigned None (Python's term signifying the absence of a value)
- The LinkedList class implements the list data structure and contains two data members, head and tail, which are assigned nodes once the list is populated. Initially the list has no nodes, so both data members are initially assigned None
#### Appending a node to a singly-linked list
- The `append()` method is a part of the LinkedList class which adds a node to the end of a linked list, making the node the new tail. The `append()` method has two parameters, the second of which is the new node to be appended to the list. Note that `append()` and all class methods contain a `self` parameter, which refers to the class object itself
#### Additional singly-linked list methods
- The `prepend()` method adds a node to the beginning of the linked list, making it the new head node of the list. `prepend()`'s second parameter is the new node to be prepended to the list.
- The `insert_after()` method adds a node after an existing node by assigning the new node's next data member to the existing node's next data member, then assigning the existing node's next data member to the new node. The method takes parameters of the existing node (current node) and the new node to be inserted (in addition to self). 
- The `remove_after()` method removes a node after the specified node by assigning the node's next value to the specified node's next data member. The method's parameter is the node before the node to be removed

### 6.7: Doubly-linked lists
- A **doubly-linked list** is another data structure for implementing a list ADT, where each node has a data, a pointer to the next node, and a pointer to the previous node. The list structure itself typically points to the first and last node, which are called the head and tail nodes
- This structure is very similar to a singly-linked list, but it has the additional pointer to the previous node. Doubly-linked lists are a type of **positional list**, where elements contain pointers to the next and/or previous elements in the list
#### Appending a node to a doubly-linked list
- Given a new node, the **append** operation for a doubly-linked list inserts a new node after the list's tail node, and the algorithm differs if the list is empty or not empty
  - *Append to empty list*: If the list's head pointer is null/empty, the algorithm points to the list's head and tail pointers to the new node
  - *Append to non-empty list*: If the list's head pointer is not null/not empty, the algorithm points the tail node's next pointer to the new node, points the new node's previous pointer to the list's tail node, and points the list's tail pointer to the new node.
#### Prepending a node to a doubly-linked list
- Given a new node, the **prepend** operation of a doubly-linked list inserts the new node before the list's head node and points the head node pointer to the new node
  - *Prepend to empty list*: If the list's head pointer is null/empty, the algorithm points the list's head and tail pointers to the new node
  - *Prepend to non-empty list*: If the list's head pointer is not null/not empty, the algorithm points the new node's next pointer to the list's head node, points the list head node's previous pointer to the new node, and then points the list's head pointer to the new node

### 6.8: Doubly-linked lists: Insert
- Given a new node, the *insertAfter* operation for a doubly-linked list inserts the new node after the provided, existing list node. curNode is a pointer to an existing node. The insertAfter algorithm has three scenarios
  - *Insert as first node*: If the list's head pointer is null (list is empty), the algorithm points the list's head and tail pointers to the new node
  - *Insert after list's tail node*: If the list's head pointer is not null (list is not empty) and curNode points to the list's tail node, the new node is inserted after the tail node. The algorithm points the tail node's next pointer to the new node, points the new node's previous pointer to the list's tail node, and then points the list's tail pointer to the new node
  - *Insert in middle of list*: If the list's head pointer is not null (list is not empty) and curNode does not point to the list's tail node, the algorithm updates the current, new, and successor nodes' next and previous points to achieve the ordering `{curNode newNode sucNode}`, which requires four pointer updates: point the new node's next pointer to sucNode, point the new node's previous pointer to curNode, point curNode's next pointer to the new node, and point sucNode's previous pointer to the new node

### 6.9: Doubly-linked lists: Remove
- The **remove** operation for a doubly-linked list removes a provided existing list node, where `curNode` is a pointer to an existing list node. The algorithm first determines the node's successor (next node) and predecessor (previous node). The variable `sucNode` points to the node's successor, and the variable `predNode` points to the node's predecessor. There are four checks to update each pointer
  - *Successor exists*: If the successor node next pointer is not null (successor exists), the algorithm points the successor's previous pointer to the predecessor node
  - *Predecessor exists*: If the predecessor node pointer is not null (predecessor exists), the algorithm points the predecessor's next pointer to the successor node.
  - *Removing list's head node*: If `curNode` points to the list's head node, the algorithm points the list's head pointer to the successor node
  - *Removing list's tail node*: If `curNode` points to the list's tail node, the algorithm points the list's tail pointer to the predecessor node
- When removing a node in the middle of a list, both the successor and predecessor node exist, so the algorithm updates the predecessor and successor nodes' pointer to achieve the ordering `{predNode sucNode}`. When removing the only node in a list, `curNode` points to both the list's head and tail nodes, and `sucNode` and `predNode` are both null. The algorithm points the list's head and tail pointers to null, making the list empty

### 6.10 Python: Doubly-linked lists
- For implementation of the doubly-linked list in Python, see [src/doublylinkedlist.py](src/doublylinkedlist.py)
#### Adding a reference to the previous node
- The Node class defined previously can be extended from the singly-linked list version to include a variable reference called `prev` that refers to the previous node in the list. When a node is first constructed, `prev` is assigned None
#### Appending a node to a doubly-linked list
- The LinkeList's `append()` method for doubly-linked lists is very similar to the method for singly-linked nodes, but has an added line of code. Before the method assigns the list's tail with the `new_node`, the method assigns the new node's `previous` variable with the old tail fof the list
#### Additional doubly-linked list members
- The `prepend()` method inserts a new node at the head of the doubly-linked list, which makes it the new head node. The `previous` variable of the old head node must be set to point to the new head node
- The `insert_after()` method requires two node parameters, the new node to be inserted and the node that is already in the list that comes immediately before the new node. Three nodes may be impacted by the `insert_after()` method
  1. The new node (`new_node`), which needs both `next` and `previous` attributes to be assigned
  2. The existing node (`current_node`), which needs to have its `next` attribute assigned
  3. The node that follows `current_node` in the list (`successor_node`), which needs to have the `previous` attribute updated
  - Generally, new node's `previous` attribute is assigned with `current_node`, the new node's `next` attribute is assigned to `successort_node`, the current node's `next` attribute is assigned with `new_node`, and the successor node's `previous` is assigned with `new_node`
  - The method needs to handle two special cases, when the list is currently empty (new node becomes the only node in the list), or when the current node is the tail of the list
- The `remove()` method unlinks a given node (`current_node`) from the list, joining together the node before the removed node (`predecessor_node`) and the node after the removed node (`successor_node`). If either the head or the tail of the list is removed, the method updates the LinkedList instance's head and tail attributes.

### 6.11 Linked list traversal
#### Linked list traversal
- A **list traversal** algorithm visits all nodes in the list once and performs an operation on each node. A common traversal operation is printing all list nodes
- The algorithm starts by pointing a `current_node` pointer to the list's head node, then while `current_node` is not `None`, the algorithm prints the current node and the points `current_node` to the next node. After the list's tail node is visited, the `current_node` is pointed to the tail node's `next` attribute, which is `None`, so the traversal ends. This algorithm can be used on singly-linked lists or doubly-linked lists
#### Doubly-linked list reverse traversal
- A doubly-linked list also supports reverse traversal. A **reverse traversal** visits all nodes starting with the list's tail node and ends after visiting the list's head node

### 6.12: Sorting linked lists
#### Insertion sort for doubly-linked lists
- Insertion sort for doubly-linked lists is similar to the insertion sort algorithm used for arrays. Starting with the second element, each element in the linked list is visited. Each visited element is moved back as needed and inserted into the correct position in the list's sorted portion. The list must be a doubly-linked list, since reverse traversal is not possibly with a singly-linked list
- Insertion sort's typical runtime is $O(N^2)$, if a list has `N` elements, the outer loop executes `N - 1` times and the inner loop executes an average of `N/2` times. The best case scenario is where the list is already sorted and the runtime complexity is `O(N)`
#### Insertion sort for singly-linked lists
- Insertion sort can be performed on a singly-linked list by changing how each visited element is inserted into the sorted portion of the list. For a singly-linked list, the insertion sort algorithm can find the insertion position by traversing the list from the list head toward the current element
- The average and worst case runtime for insertion sort on singly-linked lists is `O(N^2)`, the best case is `O(N)` which occurs when the list is sorted in descending order
#### Sorting linked-lists vs arrays
- Sorting algorithms for arrays, such as quicksort and heapsort, require constant-time access to indexed locations to operate efficiently. Linked lists do not allow indexed access, which makes adaptation of these sorting algorithms to linked lists difficult.
##### Sorting algorithms easily adapted to efficiently sort linked lists
| Sorting algorithm | Adaptation to linked lists                                                                                                                                 |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Insertion sort    | Operates similarly on doubly-linked lists. Requires searching from the head of the list for an element's insertion position for singly-linked lists.       |
| Merge sort        | Finding the middle of the list requires searching linearly from the head of the list. The merge algorithm can also merge lists without additional storage. |
##### Sorting algorithms difficult to adapt to efficiently sort linked lists
| Sorting algorithm | Challenge                                                                                                                               |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Shell sort        | Jumping the gap between elements cannot be done on a linked list, as each element between two elements must be traversed.               |
| Quicksort         | Partitioning requires backward traversal through the right portion of the array. Singly-linked lists do not support backward traversal. |
| Heap sort         | Indexed access is required to find child nodes in constant time when percolating down.                                                  |

### 6.13 Python: Sorting linked lists
#### Python insertion sort algorithm for doubly-linked lists
- Insertion sort visits all list nodes and shifts the nodes backward to be placed in the correctly positions. The list is traversed backwards to find a node's new insertion point. To move a node backward to an earlier position in the list, the node is removed using `remove()` method and re-inserted using either the `prepend()` (if the node becomes the head) or `insert_after()` method
#### Python insertion sort variant for singly-linked lists
- Insertion sort can work with singly-linked lists as well by traversing the list forwards to identify a node's insertion point and then using `prepend()` or `insert_after()` to move the node backward to the insertion point
- This method calls the `find_insertion_position()` method to find where the current node should be located.

### 6.14: Linked list dummy nodes
#### Dummy nodes
- A linked list implementation may use a **dummy node** (or **header node**), which is a node with an unused data member/attribute that always resides at the head of the list and cannot be removed. This simplifies the algorithms for a linked list because the head and tail pointers are never null
- An empty list consists of the dummy node, which has the next pointer set to None, and the list's head and tail pointers both point to the dummy node
#### Singly-linked list implementation
- When a singly-linked list with a dummy node is created, the dummy node is allocated and the list's head/tail pointers are set to the dummy node
- List operations like append, prepend, insert after, and remove after are simpler to implement compared to a linked list without a dummy node, since a special case is removed from each implementation. `append()`, `prepend()`, and `insert_after()` do not need to check if the list's head is null, since the list's head always points to the dummy node. `remove_after()` does not need a special case for removing the first item, since the first item is after the dummy node
#### Doubly-linked list implementation
- A dummy node can also be used in a doubly-linked list implementation and the dummy node always has the `previous` pointer set to `None`. 
#### Dummy head and tail nodes
- A doubly-linked list implementation can use two dummy nodes, one at the head and one at the tail. Doing this removes additional special cases and further simplifies the implementation of most methods
- The if statement at the beginning of `insert_after()` may be removed in favor of having a precondition that `current_node` cannot point to the dummy tail node. Similarly, `remove()` can remove the if statement and have a precondition that `current_node` cannot point to either dummy node

### 6.15: Linked lists: Recursion
#### Forward traversal
- Forward traversal through a linked list can be implemented with a recursive function that takes a node as an argument. If the node is non-null, it is visited first, then a recursive call is made on the node's next pointer, to traverse the remainder of the list.
#### Searching
- A recursive linked list search is implemented similar to forward traversal, with each call examining one node. If the node is null, then null is returned. Otherwise, the node's data is compared to the search key. If a match occurs, the node is returned, otherwise the remainder of the list is searched recursively
#### Reverse traversal
- Forward traversal visits a node first, then recursively traverses the remainder of the list. If the order is swapped, such that the recursive call is made first, then the list is traversed in reverse order.

### 6.16: Array-based lists
#### Array-based lists
- An **array-based list** is a list ADT implemented using an array. An array-based list supports the common list ADT operations, such as append, prepend, insert after, remove, and search
- In many programming languages, arrays have fixed sizes. An array-based list implementation will dynamically allocate the array as needed as the number of elements changes. The array-based list implementation starts by allocating a fixed size array and uses a length variable to keep track of how many array elements are in use. The list starts with a default allocation size, greater than or equal to 1, with a default size of 1 to 10 being common.
- Given a new element, the **append** operation for an array-based list of length X inserts a new element at the end of the list, index X
#### Resize operation
- An array-based list must be resized if an item is added when the allocation size equals the list length. A new array is allocated with a length greater than the existing array. Allocating the new array with twice the current length is a common approach. The existing array elements are then copied to the new array, which becomes the list's storage array. This resize operation has a runtime complexity of `O(N)`
#### Prepend and insert after operations
- The **prepend** operation for an array-based list inserts a new item at the start of the list. If the allocation size equals the list length, then the array is resized and all existing array elements are moved up by 1 position and the new item is inserted at the list start, or index 0. Because all elements must be moved up by 1, the prepend operation has a runtime complexity of $O(N)$
- The **insert_after** operation for an array-based list inserts a new item after a specified index. First, if the allocation equals the list length, the array is resized. Next, all elements in the array residing after the specific index are moved up by one position, then the new item is inserted at index `specified index + 1`. This operation has a best case runtime complexity of $O(1)$ and a worst case runtime complexity of $O(N)$
- Array-based lists often support an **insert_at** operation, which inserts an item at a specific index, which can be accomplished by using `insert_after(x - 1)`
#### Search and removal operations
- Given a key, the **search** operation returns an index for the first element whose data matches that key, or -1 if not found
- Given the index of an item in an array-based index, the **remove-at** operation removes the item at that index. When removing an item at index X, each item after index X is moved down by 1 position
- Both the search and remove operations have a worst case runtime complexity of $O(N)$

### 6.17: Python - Array-based list
#### Python: Array-based list
- Python's built-in list type is implemented with an array-based data structure. The ArrayList class uses a list object as the internal array, with the entire list allocation and populated with None at the outset.
#### append() and resize() methods
- `append()` is implemented by inserting the new item at the index equal to the array's current length, if the array is already filled to its allocation size, then the array is doubled in size first
- `resize()` works by first creating a new array of the indicated size, then copying all items in the current array to the new array. This new array is reassigned to the existing array and the `allocation_size` attribute is updated
#### prepend and insert_after() methods
- The `prepend()` method shifts the entire contents of the array one index to the right, which is accomplished by copying the list item to the next index, then copying the second to last item to the index previously occupied by the last item, and so on until the first item is copied at index 1
- To shift the items, the loop must use the indices in reverse order, which is accomplished by using the `range()` function up to `self.length` and then the `reversed()` function to iterate backward through the indices
- The `insert_after()` method operates almost identically to `prepend()`. Items are shifted one space to the right, but only down to the index + 1. Items below that are not shifted, which creates an empty space for the new item to be inserted. The functions `range()` and `reversed()` are used to iterate through the indices in the proper order
#### search() and remove_at() methods
- The `search()` method takes a target item as a parameter, then tests each item in the list, from index zero to length - 1, for equality with the target. The method returns the index of the first matching item is found, or -1 if no match is found. This method does not change the list's length or internal array's allocation size
- The `remove_at()` method removes the item at the specified index by shifting the array items. The items from the parameter index plus 1 are shifted to the left by one index, up to the final item in the array. The `remove_at()` method decreases the list's length, but does not change the internal array's allocation size