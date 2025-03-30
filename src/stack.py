"""
Implementation of the Stack abstract data type (ADT).
"""
from typing import Any

class Stack:
    """
    Implementation of the stack abstract data type

    Methods
    -------
    __init__(max_length=-1)
        Initialize a stack, optionally with a maximum length to create a bounded stack.
    pop()
        Remove and return the item at the top of the stack.
    push()
        Push an item onto the top of the stack, provided it doesn't exceed the given bound.
    peek()
        Returns the value of the item on top of the stack, but does not remove it.
    get_length()
        Return the number of items in the stack.
    is_empty()
        Check if the stack is empty.
    """
    def __init__(self, max_length: int = -1) -> None:
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
        self.stack_list = []
        self.max_length = max_length

    def pop(self) -> Any:
        """
        Remove and return the item at the top of the stack.

        Returns
        -------
        Any
            The item at the top of the stack.

        Raises
        ------
        IndexError
            If the stack is empty
        """
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        return self.stack_list.pop()

    def push(self, item: Any) -> None:
        """
        Push an item onto the top of the stack, provided it doesn't exceed the given bound.

        Parameters
        ----------
        item : Any
            The item to be added to the stack.

        Returns
        -------
        None

        Raises
        ------
        OverflowError
            If the stack is full
        """
        if len(self.stack_list) == self.max_length:
            raise OverflowError("Stack is full")
        self.stack_list.append(item)

    def peek(self) -> Any:
        """
        Returns the value of the item on top of the stack, but does not remove it.

        Returns
        -------
        Any

        Raises
        ------
        IndexError
            If the stack is empty
        """
        if self.is_empty():
            raise IndexError("Cannot peek from an empty stack")
        return self.stack_list[-1]

    def get_length(self) -> int:
        """
        Return the number of items in the stack.

        Returns
        -------
        int
        """
        return len(self)

    def __len__(self) -> int:
        """
        Override __len__ method to allow users to call `len(stack)`.

        Returns
        -------
        int
        """
        return len(self.stack_list)

    def is_empty(self) -> bool:
        """
        Check if the stack is empty.

        Returns
        -------
        bool
        """
        return not self.stack_list
