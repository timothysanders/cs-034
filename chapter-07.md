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
- A queue can be implemented with an array and needs two variables in addition to the array, `length` and `front_index`. The queue's content starts at `array[front_index]` and continues forward for `length` items, if the array's end is reached before encountering all items, remaining items are stored starting at index 0.
#### Bounded vs unbounded queue
- A **bounded queue** is a queue with a length that does exceed a specified maximum value and requires an additional variable, `max_length`. The maximum length is commonly assigned at construction time and does not change for the queue's lifetime. A bounded queue with a length equal to the maximum length is said to be **full**. **Unbounded queues** are queues with a length that can grow indefinitely.
#### Flexible implementation and resize operation
- An array-based queue can support both bounded and unbounded queue operations by using `max_length`. If `max_length` is negative, the queue is unbounded, or if `max_length` is nonnegative, the queue is bounded.
- The Python implementation can use a list to store queue items. `len(queue_list)` is the queue allocation size and the list is used much like a fixed size array. If `max_length` is non-negative, the new list's length is the minimum of `max_length` and double the current list's length, with existing list entries copied so that the front index is reset to 0.
#### Enqueue and dequeue operations
- An enqueue operation
  1. Compares `self.length` and `self.max_length`, if they are equal, the queue is full so no change occurs and False is returned
  2. Compares `self.length` and `len(self.queue_list)`. If equal, a resize operation occurs.
  3. Computes the enqueued item's index as `(self.front_index + self.length) % len(self.queue_list)` and assigns the queue_list at that index
  4. Increments the length attribute and returns True
- A dequeue operation
  1. Makes a copy of the list item at `front_index`
  2. Decrements `length`
  3. Increments `front_index`, resetting to 0 if the incremented value equals the allocation size
  4. Returns the list item from step 1
- Worst-case time complexities are the same for whether the queue is bounded or unbounded: O(n) for enqueue and O(1) for dequeue

### 7.7: Python: Stacks and Queues using linked lists
#### Implementing a stack in Python
- Stacks can be implemented with a single linked list data member and the Stack class itself has two methods, `push()` and `pop()`
  - `push()` adds a node to the top of the stack by calling LinkedList's `prepend()` method
  - `pop()` removes the head of the stack's list with the `LinkedList.remove_after()` method and returns the node's data
#### Implementing a queue in Python
- Queues can also be implemented with a single LinkedList data member and the Queue class has methods `enqueue()` and `dequeue()`
  - `enqueue()` adds a node at the end of the queue, calling `LinkedList.append()`
  - `dequeue()` removes the queue's head node and returns the node's data

### 7.8: Deque abstract data type (ADT)
#### Deque abstract data type
- A **deque** (pronounced "deck") is a double-ended queue, which is an ADT where items can be inserted and removed from both the front and the back
- The `push_front()` method inserts an item at the front of the deque and the `push_back()` adds an item at the back of the deque.
- The `pop_front()` method removes and returns the item at the front of the deque and the `pop_back()` method removes and returns the item at the back of the deque
#### Common deque ADT operations
- A deque typically supports peeking at the front and back, along with determining the length. The peek operations do not remove any items

| Operation           | Description                                                | Example starting with deque: 59, 63, 19 (front is 59)   |
|---------------------|------------------------------------------------------------|---------------------------------------------------------|
| PushFront(deque, x) | Inserts x at the front of the deque                        | PushFront(deque, 41). Deque: 41, 59, 63, 19             |
| PushBack(deque, x)  | Inserts x at the back of the deque                         | PushBack(deque, 41). Deque: 59, 63, 19, 41              |
| PopFront(deque)     | Returns and removes item at front of deque                 | PopFront(deque) returns 59. Deque: 63, 19               |
| PopBack(deque)      | Returns and removes item at back of deque                  | PopBack(deque) returns 19. Deque: 59, 63                |
| PeekFront(deque)    | Returns but does not remove the item at the front of deque | PeekFront(deque) returns 59. Deque is still: 59, 63, 19 |
| PeekBack(deque)     | Returns but does not remove the item at the back of deque  | PeekBack(deque) returns 19. Deque is still: 59, 63, 19  |
| IsEmpty(deque)      | Returns true if the deque is empty                         | IsEmpty(deque) returns false.                           |
| GetLength(deque)    | Returns the number of items in the deque                   | GetLength(deque) returns 3.                             |
