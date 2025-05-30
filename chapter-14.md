# Chapter 14: Algorithms

### 14.1: Huffman Compression
#### Basic compression idea
- Given data represented as a certain quantity of bits, **compression** transforms the data to use fewer bits. Compressed data uses less storage and can be communicated faster than uncompressed data.
- The basic idea of compression is to encode frequently occurring items using fewer bits. For example, uncompressed ASCII characters use 8 bits each, but compression uses fewer than 8 bits for more frequently occurring characters.
#### Building a character frequency table
- Prior to compression, a character frequency table must be built for an input string. This table contains each distinct character from the input string and each character's number of occurrences. These are often stored in a dictionary or map object.
- ```text
  FUNCTION build_character_frequency_table(input_string):
      table = NEW dictionary()
      FOR (i = 0; i < input_string.length; i++):
          current_character = input_string[i]
          IF (table HAS KEY FOR current_character):
              table[current_character] = table[current_character] + 1
          ELSE:
              table[current_character] = 1
      RETURN table
  ```
#### Huffman coding
- **Huffman coding** is a common compression technique that assigns fewer bits to frequent items, using a binary tree
- For Huffman encoded data, the dictionary must be included along with the compressed data to enable decompression. This dictionary adds to the total bits used, but because typically only large files are compressed, the dictionary is usually a tiny fraction of the total size.
#### Building a Huffman tree
- The attributes in a Huffman tree node depend on the node type
  - Leaf nodes have two attributes: a character from the input and an integer frequency for that character
  - Internal nodes have left and right child nodes, along with an integer frequency value that represents the sum of the left and right child frequencies
- ```text
  FUNCTION huffman_build_tree(input_string):
      table = CALL build_character_frequency_table(input_string)
      nodes = NEW PriorityQueue()
      FOR ((character, frequency) IN table):
          new_leaf = NEW LeafNode(frequency, character)
          ENQUEUE new_leaf INTO nodes
      WHILE (nodes.length > 1):
          left = dequeue(nodes)
          right = dequeue(nodes)
          freq_sum = right.frequency + left.frequency
          parent = NEW InternalNode(freq_sum, left, right)
          ENQUEUE parent INTO nodes
      RETURN dequeue(nodes)
  
  tree_root = huffman_build_tree("BANANAS")
  ```
- Many implementations will not use separate node types, but rather will use the same node type with different attributes
#### Getting Huffman codes
- Huffman codes for each character are built from a Huffman tree, with each character corresponding to a leaf node. The Huffman code for a character is built by tracing a path from the root to that character's left node, appending 0 when branching left or 1 when branching right
- ```text
  FUNCTION huffman_get_codes(node, prefix, output):
      IF (node IS A leaf):
          output[node.character] = prefix
      ELSE:
          huffman_get_codes(node.left, prefix + "0", output)
          huffman_get_codes(node.right, prefix + "1", output)
      RETURN output
  
  root = huffman_build_tree("BANANAS")
  codes = huffman_get_codes(root, "", NEW Dictionary())
  ```
#### Compressing data
- To compress an input string, the Huffman codes are first obtained for each character. Then each character of the input string is processed and corresponding bit codes are concatenated to produce the compressed result
- ```text
  FUNCTION huffman_compress(input_string):
      root = huffman_build_tree(input_string)
      codes = huffman_get_codes(root, "", NEW Dictionary())
      result = ""
      FOR c IN input_string:
          result += codes[c]
      RETURN result
  ```
#### Decompressing Huffman coded data
- To decompress Huffman code data, one can use a Huffman tree and trace the branches for each bit, starting at the root. When the final node of the branch is reached, the result has been found. The process continues until the entire data is decompressed
- ```text
  FUNCTION huffman_decompress(compressed_string, tree_root):
      node = tree_root
      result = ""
      FOR (bit in compressed_string):
          IF (bit == 0):
              node = node.left
          ELSE:
              node = node.right
          IF (node IS A leaf):
              result += node.character
              node = tree_root
      RETURN result
  ```
### 14.2: Heuristics
#### Heuristics
- In practice, solving a problem in the optimal or most accurate way might require more computational resources than are available or feasible. Algorithms for these problems often use a **heuristic**, which is a technique that accepts a non-optimal or less accurate solution to improve execution speed.
#### Heuristic optimization
- A **heuristic algorithm** is an algorithm that quickly determines a near optimal or approximate solution, and such an algorithm can be designed to solve the **0-1 knapsack problem**. A heuristic algorithm could use the heuristic of choosing the highest value item that fits in the knapsack's remaining space
- ```text
  FUNCTION knapsack_01(knapsack, item_list, item_list_size):
      SORT item_list DESCENDING BY VALUE
      remaining = knapsack.maximum_weight
      FOR (i = 0; i < item_list_size; i++):
          IF (item_list[i].weight <= remaining):
              PUT item_list[i] IN knapsack
              remaining -= item_list[i].weight
          ELSE:
              BREAK
  ```
#### Self-adjusting heuristic
- A **self-adjusting heuristic** is an algorithm that modifies a data structure based on how that data structure is used.
- For example, a self-adjusting heuristic can be used to speed up searches for frequently-searched-for list items by moving a list item to the front of the list when that item is searched for.

### 14.3: Python - Heuristics
#### 0-1 Knapsack problem heuristic
- The general knapsack problem seeks to maximize the total value of items placed into a knapsack such that the total weight of items in the knapsack doesn't exceed a predetermined weight. The 0-1 knapsack problem imposes the restriction that each item can be added at most once. A heuristic algorithm to solve the knapsack problem first sorts items in descending order by value, and then iteratively places the most valuable items that fit within the remaining space into the knapsack until no more items can be added.

### 14.4: Greedy algorithms
#### Greedy algorithm
- A **greedy algorithm** is an algorithm that, when presented with a list of options, chooses the option that is optimal at that point in time. The choice does not consider subsequent options and consequently, may not arrive at an optimal solution.
#### Fractional knapsack problem
- The **fractional knapsack problem** is the knapsack problem with the potential to take each item a fractional number of times. For example, a 4 pound, $10 item could be taken 0.5 times to fill a knapsack with a two pound limit.
- Compared to the greedy solution for the 0-1 knapsack problem, a greedy solution for the fractional knapsack problem is optimal. First, sort items in descending order based on their value-to-weight ratio. Then, take one of each item from the list, in order, until taking 1 of the next item would exceed the weight limit. A fraction of the next item in the list is taken to fill the remaining weight.
#### Activity selection problem
- The **activity selection problem** is a problem where one or more activities are available, each with a start/finish time and the goal is to build the largest set of activities without time conflicts.
- A greedy algorithm can provide an optimal solution for the activity selection problem. First, create an empty set of chosen activities. Activities are then sorted in ascending order by finish time. The first activity is marked as the current activity and added to the set of chosen activities. The algorithm then iterates through all activities after the first, looking for the next activity that starts after the current activity ends. When such an activity is found, the next activity is added to the set of chosen activities, and the next activity is reassigned as the current. After iterating through all activities, the chosen set of activities contains the maximum possible number of non-conflicting activities.

### 14.6: Dynamic programming
#### Dynamic programming overview
- **Dynamic programming** is a problem-solving technique that splits a problem into smaller subproblems, computes and stores solutions to subproblems in memory, then uses the stored solutions to solve the larger problem. An example is Fibonacci numbers, which can be calculated with an iterative approach, storing the previous two numbers, instead of making recursive calls that recompute the same term many times over
#### Longest common substring
- The **longest common substring** algorithm takes two strings as input and determines the longest substring that exists in both strings, using dynamic programming. An N * M integer matrix keeps track of matching substrings, where N is the length of the first string and M the length of the second. Each row is a character from the first string and each column is a character from the second string. An entry at (i, j) in the matrix indicates the length of the longest common substring that ends at character i in the first string and character j in the second. An entry will be 0 only if the two characters the entry corresponds to are not the same. The matrix is built one row at a time, from the top row to the bottom row. Each row's entries are filled from left to right. An entry is set to 0 if the two characters do not match, otherwise, the entry at (i, j) is set to 1 + the entry in (i-1, j-1)
- The longest common substring algorithm operates on two strings of length N and M, with a runtime complexity of $O(N \cdot M)$ and a space complexity of $O(N \cdot M)$
#### Common substrings in DNA
- A real-world application of the longest common substring algorithm is to find common substrings in DNA strings
- An optimization for the longest common substring can be implemented so only the previously computed row and the largest matrix entry's location and value are stored in memory. The makes the storage complexity $O(N)$, but the runtime remains $O(N \cdot M)$