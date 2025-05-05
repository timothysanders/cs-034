# Chapter 11: Heaps and Treaps

### 11.1: Heaps
#### Heap concept
- Some applications will need access to and removal of the maximum item in a set of items. In these instances, maintaining fully sorted orders requires more work than necessary, and a **max-heap** may be an appropriate data structure.
- A **max-heap** is a complete binary tree that maintains the property that a node's key is greater than or equal to the node's children's keys. This means that the node key is equal to or greater than all of its descendant's keys. This means that the max-heap's root is always the maximum key in the entire tree.
- ![Sample max-heap](images/figure-11.1.1.png)
#### Max-heap insert and remove operations
- An **insert** into a max-heap starts by inserting the node into the tree's last level, then swapping the node with its parent until no max-heap property violations occur
- Inserts fill a level left-to-right before adding another level, to keep the tree at the minimum height possible
- The upward swapping of nodes in a max-heap is called **percolating**
- A **remove** from a max-heap is always a removal of the root, and is done by replacing the root with the last level's last node, and then swapping that node with its greatest child until no max-heap property violations occur