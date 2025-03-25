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
- 