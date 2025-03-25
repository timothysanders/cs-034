"""
Implements a DoublyLinkedList and Node class to demonstrate doubly-linked lists.
"""

class Node:
    """

    """
    def __init__(self, initial_data: int):
        self.data = initial_data
        self.next = None
        self.previous = None

class LinkedList:
    """

    """
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_node: Node) -> None:
        """
        Add the given node to the end of the list.

        Parameters
        ----------
        new_node : Node

        Returns
        -------
        None
        """
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, new_node: Node) -> None:
        """
        Add the given node at the beginning of the list.

        Parameters
        ----------
        new_node : Node

        Returns
        -------
        None
        """
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


if __name__ == "__main__":
    node_a = Node(34)

    linked_list = LinkedList()
    assert linked_list.head is None
    assert linked_list.tail is None

    linked_list.append(node_a)

    assert linked_list.head.data == 34
    assert linked_list.tail.data == 34

    node_b = Node(15)