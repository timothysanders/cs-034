"""
Implements a DoublyLinkedList and Node class to demonstrate doubly-linked lists.
"""

class Node:
    """
    The Node class implements a list node with three attributes, `data`, `next`, and `previous`.
    """
    def __init__(self, initial_data: int):
        self.data = initial_data
        self.next = None
        self.previous = None

class LinkedList:
    """
    The LinkedList class implements a doubly-linked list data structure with two attributes, `head` and `tail`.

    Methods
    -------
    append(new_node: Node)
        - Add the given node to the end of the list.
    prepend(new_node: Node)
        - Add the given node at the beginning of the list.
    insert_after(current_node: Node, new_node: Node)
        - Insert a new node after the given current node.
    remove(current_node: Node)
        - Remove the given node from the LinkedList instance.
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
            new_node.previous = self.tail
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
            self.head.previous = new_node
            self.head = new_node

    def insert_after(self, current_node: Node, new_node: Node) -> None:
        """
        Insert a new node after the given current node.

        Parameters
        ----------
        current_node : Node
        new_node : Node

        Returns
        -------
        None
        """
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif current_node is self.tail:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        else:
            successor_node = current_node.next
            new_node.next = successor_node
            new_node.previous = current_node
            current_node.next = new_node
            successor_node.previous = new_node

    def remove(self, current_node: Node) -> None:
        """
        Remove the given node from the LinkedList instance.

        Parameters
        ----------
        current_node : Node

        Returns
        -------
        None
        """
        successor_node = current_node.next
        predecessor_node = current_node.previous

        if successor_node is not None:
            successor_node.previous = predecessor_node

        if predecessor_node is not None:
            predecessor_node.next = successor_node

        if current_node is self.head:
            self.head = successor_node

        if current_node is self.tail:
            self.tail = predecessor_node

    def insertion_sort(self):
        """
        Sort the LinkedList instance using the insertion sort algorithm.

        Returns
        -------
        None
        """
        current_node = self.head.next
        while current_node is not None:
            next_node = current_node.next
            search_node = current_node.previous
            while ((search_node is not None) and
                   (search_node.data > current_node.data)):
                search_node = search_node.previous

            self.remove(current_node)

            if search_node is None:
                current_node.previous = None
                self.prepend(current_node)
            else:
                self.insert_after(search_node, current_node)

            current_node = next_node


if __name__ == "__main__":
    node_a = Node(34)

    linked_list = LinkedList()
    assert linked_list.head is None
    assert linked_list.tail is None

    linked_list.append(node_a)

    assert linked_list.head.data == 34
    assert linked_list.tail.data == 34

    num_list = LinkedList()
    node_a = Node(1)
    node_b = Node(2)
    node_c = Node(3)
    node_d = Node(4)
    node_e = Node(5)

    num_list.append(node_a)
    num_list.append(node_b)
    num_list.append(node_c)
    num_list.prepend(node_d)
    num_list.insert_after(node_a, node_e)
    num_list.remove(node_c)
    assert num_list.head.data == 4
    assert num_list.tail.data == 2
    num_list.insertion_sort()
    assert num_list.head.data == 1
    assert num_list.head.next.data == 2
    assert num_list.tail.data == 5
    assert num_list.tail.previous.data == 4