"""
Implements a singly-LinkedList and Node class to demonstrate singly-linked lists.
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
    The LinkedList class implements a singly-linked list data structure with two attributes, `head` and `tail`.

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

    def insertion_sort(self) -> None:
        """
        Sort the LinkedList instance using the insertion sort algorithm.

        Returns
        -------
        None
        """
        before_current = self.head
        current_node = self.head.next
        while current_node is not None:
            next_node = current_node.next
            position = self.find_insertion_position(current_node.data)
            if position == before_current:
                before_current = current_node
            else:
                self.remove_after(before_current)
                if position is None:
                    self.prepend(current_node)
                else:
                    self.insert_after(position, current_node)
            current_node = next_node

    def find_insertion_position(self, data_value: int) -> Node:
        """
        Return the node prior to the given `data_value`.

        Parameters
        ----------
        data_value : int

        Returns
        -------
        Node
        """
        position_a = None
        position_b = self.head
        while (position_b is not None) and (data_value > position_b.data):
            position_a = position_b
            position_b = position_b.next
        return position_a



if __name__ == "__main__":
    node_a = Node(95)
    node_b = Node(42)
    node_c = Node(35)
    node_d = Node(10)

    list_test = LinkedList()
    list_test.append(node_a)
    assert list_test.head.data == 95
    assert list_test.tail.data == 95
    list_test.append(node_b)
    assert list_test.head.data == 95
    assert list_test.tail.data == 42
    assert list_test.head.next.data == 42
    list_test.prepend(node_c)
    assert list_test.head.data == 35
    assert list_test.head.next.data == 95
    list_test.insert_after(node_c, node_d)
    assert list_test.head.next.data == 10
    assert list_test.head.next.next.data == 95
    list_test.remove_after(node_a)

    num_list = LinkedList()
    node_a = Node(72)
    node_b = Node(91)
    node_c = Node(53)
    node_d = Node(12)

    num_list.append(node_a)
    num_list.append(node_b)
    num_list.append(node_c)
    num_list.append(node_d)
    num_list.insertion_sort()
    assert num_list.head.data == 12
    assert num_list.tail.data == 91
    assert num_list.head.next.data == 53