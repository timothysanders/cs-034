class MaxHeap:
    def __init__(self):
        self.heap_array = []

    def percolate_up(self, node_index):
        while node_index > 0:
            parent_index = (node_index - 1) // 2
            # check for violations of max heap property
            if self.heap_array[node_index] <= self.heap_array[parent_index]:
                return
            else:
                # swap heap_array[node_index] and heap_array[parent_index]
                temp = self.heap_array[node_index]
                self.heap_array[node_index] = self.heap_array[parent_index]
                self.heap_array[parent_index] = temp
                node_index = parent_index

    def percolate_down(self, node_index):
        child_index = 2 * node_index + 1
        value = self.heap_array[node_index]
        while child_index < len(self.heap_array):
            # Find the max among the node and the node's children
            max_value = value
            max_index = -1
            i = 0
            while i < 2 and i + child_index < len(self.heap_array):
                if self.heap_array[i + child_index] > max_value:
                    max_value = self.heap_array[i + child_index]
                    max_index = i + child_index
                i = i + 1

            # check for a violation of the max heap property
            if max_value == value:
                return
            else:
                # swap heap_array[node_index] and heap_array[max_index]
                temp = self.heap_array[node_index]
                self.heap_array[node_index] = self.heap_array[max_index]
                self.heap_array[max_index] = temp

                # Continue loop from the larger child node
                node_index = max_index
                child_index = 2 * node_index + 1

    def insert(self, value):
        self.heap_array.append(value)
        # Percolate up from the last index to restore the heap property
        self.percolate_up(len(self.heap_array) - 1)

    def remove(self):
        # Retrieve the root value
        max_value = self.heap_array[0]
        # Move the last item in the array into index 0
        replace_value = self.heap_array.pop()
        if len(self.heap_array) > 0:
            self.heap_array[0] = replace_value

            # percolate down to restore max heap property
            self.percolate_down(0)
        return max_value
