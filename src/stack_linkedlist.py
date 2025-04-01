"""
Implementation of the Stack abstract data type (ADT) with a linked list.
"""
from typing import Any

from singlylinkedlist import LinkedList, Node


class Stack:
    """
    Implementation of the Stack abstract data type.

    Methods
    -------

    """
    def __init__(self, max_length: int = -1):
        """
        Initialize a stack, optionally with a maximum length to create a bounded stack.

        If the max_length parameter is omitted or negative, the stack is unbounded. If the max_length
        is non-negative, the stack is bounded.

        Parameters
        ----------
        max_length : int = -1
            The optional maximum length of the stack

        Returns
        -------
        None

        Raises
        ------
        ValueError
            If the provided max_length is less than -1
        """
        if max_length < -1:
            raise ValueError("max_length must be -1 (for unbounded) or a non-negative integer")
        self._max_length = max_length
        self._list = LinkedList()
        self._size = 0

    def is_empty(self) -> bool:
        """
        Check if the stack is empty.

        Returns
        -------
        bool
            True if the stack is empty, False otherwise
        """
        return self._list.head is None

    def push(self, new_item: Any) -> None:
        """
        Add a new item to the front of the stack.

        Parameters
        ----------
        new_item : Any
            The new item to be added to the stack

        Returns
        -------
        None

        Raises
        ------
        OverflowError
            If the stack is full
        """
        if self._max_length != -1 and len(self) >= self._max_length:
            raise OverflowError("Stack has reached its maximum capacity")
        if not isinstance(new_item, Node):
            self._list.prepend(Node(new_item))
            self._size += 1
        else:
            self._list.prepend(new_item)
            self._size += 1

    def pop(self) -> Any:
        """
        Remove the node from the front of the stack and return its data.

        Returns
        -------
        Node

        Raises
        ------
        ValueError
            If the stack is empty
        """
        if self.is_empty():
            raise ValueError("Stack is empty")
        popped_item = self._list.head.data
        self._list.remove_after()
        self._size -= 1
        return popped_item

    def peek(self) -> Any:
        """
        Return the value of the node at the front of the stack.

        Returns
        -------
        Any
            The value of the node at the front of the stack

        Raises
        ------
        ValueError
            If the stack is empty
        """
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self._list.head.data

    def get_length(self) -> int:
        """
        Return the number of nodes in a singly linked list.

        Returns
        -------
        int
            The total number of nodes in the list.
        """
        return len(self)

    def __len__(self) -> int:
        """
        Return the number of nodes in the stack.

        Returns
        -------
        int
            The total number of nodes in the stack.
        """
        return self._size


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert len(stack) == 3
    stack.pop()
    assert len(stack) == 2