

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, search_key):
        current_node = self.root
        while current_node is not None:
            # Return the node if the key matches
            if current_node.key == search_key:
                return current_node
            # Search key is less than the current node
            elif search_key < current_node.key:
                current_node = current_node.left
            # search key is greater than the current node
            else:
                current_node = current_node.right
        # If the key is not found, return None
        return None

    def insert(self, node: Node):
        if self.root is None:
            self.root = node
        else:
            current_node = self.root
            while current_node is not None:
                if node.key < current_node.key:
                    if current_node.left is None:
                        current_node.left = node
                        current_node = None
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = node
                        current_node = None
                    else:
                        current_node = current_node.right

    def remove(self, key):
        parent = None
        current_node = self.root

        while current_node is not None:
            if current_node.key == key:
                # Case 1
                if current_node.left is None and current_node.right is None:
                    if parent is None:
                        # Node is root node
                        self.root = None
                    elif parent.left is current_node:
                        parent.left = None
                    else:
                        parent.right = None
                    return
                # Case 2
                elif current_node.left is not None and current_node.right is None:
                    if parent is None:
                        self.root = current_node.left
                    elif parent.left is current_node:
                        parent.left = current_node.left
                    else:
                        parent.right = current_node.left
                    return
                # Case 2
                elif current_node.left is None and current_node.right is not None:
                    if parent is None:
                        self.root = current_node.right
                    elif parent.left is current_node:
                        parent.left = current_node.right
                    else:
                        parent.right = current_node.right
                    return
                else:
                    successor_parent = current_node
                    successor = current_node.right
                    while successor.left is not None:
                        successor_parent = successor
                        successor = successor.left
                    current_node.key = successor.key
                    if successor_parent.left is successor:
                        successor_parent.left = successor.right
                    else:
                        successor_parent.right = successor.right
                    return
            elif current_node.key < key:
                parent = current_node
                current_node = current_node.right
            else:
                parent = current_node
                current_node = current_node.left
        return