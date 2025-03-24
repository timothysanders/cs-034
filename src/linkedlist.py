"""
Implements a LinkedList and Node class to demonstrate singly-linked lists.
"""

class Node:
    """
    The Node class implements a list node with two attributes, `data` and `next`.

    Attributes
    ----------
    data : int
    next : Node
    """
    def __init__(self, initial_data: int):
        self.data = initial_data
        self.next = None

class LinkedList:
    """
    The LinkedList class implements a list data structure with two attributes, `head` and `tail`.

    Methods
    -------
    append(new_node: Node)
        - Add a node to the end of the linked list.
    prepend(new_node: Node)
        - Add a new node to the beginning of the linked list.
    insert_after(current_node: Node, new_node: Node):
        - Insert a new node after the specified current node.
    remove_after(current_node: Node)
        - Remove a node after the specified current node.

    Attributes
    ----------
    head : Node
    tail : Node
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_node: Node) -> None:
        """
        Add a node to the end of the linked list.

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
            self.tail = new_node

    def prepend(self, new_node: Node) -> None:
        """
        Add a new node to the beginning of the linked list.

        Parameters
        ----------
        new_node : Node

        Returns
        -------
        None
        """
        # If the list is empty, set the new node to the head and tail node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # If the list is not empty, insert the new node as the head node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, current_node: Node, new_node: Node) -> None:
        """
        Insert a new node after the specified current node.

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
            self.tail = new_node
        else:
            new_node.next = current_node.next
            current_node.next = new_node

    def remove_after(self, current_node: Node) -> None:
        """
        Remove a node after the specified current node.

        Parameters
        ----------
        current_node : Node

        Returns
        -------
        None
        """
        if current_node is None and self.head is not None:
            succeeding_node = self.head.next
            self.head = succeeding_node
            if succeeding_node is None:
                self.tail = None
        elif current_node.next is not None:
            succeeding_node = current_node.next.next
            current_node.next = succeeding_node
            if succeeding_node is None:
                self.tail = current_node



if __name__ == "__main__":
    node_a = Node(95)
    node_b = Node(42)
    node_c = Node(35)
    node_d = Node(10)

    list_test = LinkedList()
    list_test.append(node_a)
    list_test.append(node_b)
    list_test.prepend(node_c)
    list_test.insert_after(node_c, node_d)
    list_test.remove_after(node_a)