# Chapter 7: Stacks and Queues

### 7.1: Stack abstract data type (ADT)
#### Stack abstract data type
- A **stack** is an ADT where items are added and removed only at the "top". The **push** operation inserts an item on the top and a **pop** operation removes and returns an item at the top of the stack. Stacks are referred to as a **last-in first-out** ADT and can be implemented with linked lists, arrays, or vectors.
#### Common stack ADT operations
| Operation        | Description                                      | Example starting with stack: 99, 77 (top is 99). |
|------------------|--------------------------------------------------|--------------------------------------------------|
| Push(stack, x)   | Inserts x on top of stack                        | Push(stack, 44). Stack: 44, 99, 77               |
| Pop(stack)       | Returns and removes item at top of stack         | Pop(stack) returns: 99. Stack: 77                |
| Peek(stack)      | Returns but does not remove item at top of stack | Peek(stack) returns 99. Stack still: 99, 77      |
| IsEmpty(stack)   | Returns true if stack has no items               | IsEmpty(stack) returns false.                    |
| GetLength(stack) | Returns the number of items in the stack         | GetLength(stack) returns 2.                      |

### 7.2: Stacks using linked lists
- Stacks are often implemented with linked lists, with the list's head node being the top. Push is performed by creating a new list node, assigning the node's data with the item, and prepending the node to the list. A pop is performed by assigning a local node to the head node's data, removing the head node from the list, and then returning the local variable

### 7.3: Python: Array-based stacks
#### Array-based stack storage
- A stack can also be implemented with an array, with two variables needed in addition to the array itself
  - `allocation_size`: integer for the array's allocated size
  - `length`: integer for the stack's length
- The bottom of the stack is at `array[0]` and the top item is at `array[length - 1]`. if the stack is empty, the `length` is 0
#### Unbounded stack
- An **unbounded** stack is a stack with no upper limit on length, and the unbounded stack's length can increase indefinitely
#### Bounded stack
- A **bounded** stack is a stack with a length that does not exceed a specific maximum value, which is usually the initial allocation size. For example, a bounded stack with an allocation size of 100 cannot exceed a length of 100 items. A bounded stack whose length equals its allocation size is said to be **full**.
#### Implementing a stack with a Python list
- Because Python lists do not have fixed sizes, the implementation of a reallocation method is not needed, which makes implementation simpler. The stack class has only one attribute, which is the stack list that stored the data. Stack methods `push()` and `pop()` utilize list `append()` and `pop()` methods.
- See [src/stack.py](src/stack.py) for full implementation
```python
class Stack:
    def __init__(self):
        self.stack_list = []

    def pop(self):
        return self.stack_list.pop()

    def push(self, item):
        self.stack_list.append(item)
```

### 7.4: Queue abstract data type (ADT)
#### Queue abstract data type
- A **queue** is an ADT where items are inserted at the end of the queue and removed from the front of the queue. The queue **enqueue** operation inserts an item at the end of the queue and the **dequeue** operation removes and returns the item at the front of the queue. A queue is referred to as a **first-in first-out** ADT and can be implemented with a linked list or an array.
- Conceptually, queues are similar to waiting in line at a grocery store, ride, etc. where you enter at the end and exit at the front
#### Common queue ADT operations
| Operation         | Description                                                | Example starting with queue: 43, 12, 77 (front is 43) |
|-------------------|------------------------------------------------------------|-------------------------------------------------------|
| Enqueue(queue, x) | Inserts x at end of the queue                              | Enqueue(queue, 56). Queue: 43, 12, 77, 56             |
| Dequeue(queue)    | Returns and removes item at front of queue                 | Dequeue(queue) returns: 43. Queue: 12, 77             |
| Peek(queue)       | Returns but does not remove item at the front of the queue | Peek(queue) returns 43. Queue: 43, 12, 77             |
| IsEmpty(queue)    | Returns true if queue has no items                         | IsEmpty(queue) returns false.                         |
| GetLength(queue)  | Returns the number of items in the queue                   | GetLength(queue)                                      |

### 7.5: Queues using linked lists
- Queues are often implemented with linked lists, the list's head node represents the front of the queue and the list's tail node represents the queue's end. Enqueueing is done by creating a new node, assigning the data to the node, then appending the node to the list. Dequeuing is done by assigning a local variable to the head node's data, removing the head node from the list, then returning the local variable

### 7.6: Python: Array-based queues
#### Array-based queue storage