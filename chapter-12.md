# Chapter 12: Sets

### 12.1: Set abstract data type
#### Set abstract data type
- A **set** is a collection of distinct elements. The set **add** operation adds an element to the set, provided an equal element doesn't already exist. Sets are also unordered, so the set 3, 7, 9 is equal to the set 9, 7, 3
#### Element keys and removal
- Set elements may be primitives such as strings or numbers, or objects with any number of attributes. When storing objects, sets will commonly distinguish elements based on the element's **key value**, which is a data value that is a unique identifier for the element. 
- Sets are commonly implemented to use keys for all element types. When storing objects, the set uses a function to retrieve the object's key (or knowledge of which property is the key value). When storing primitives, the primitive's value is the key itself
- Given a key, a set **remove** operation removes the element with the specified key from the set
#### Searching and subsets
- Given a key, a set **search** returns the set element with the specified key, or null if no such element exists. Search can be used to implement a subset test, where set X is a **subset** of set Y only if every element of X is also an element of Y. Each set is always a subset of itself

### 12.2: Set operations
#### Union, intersection, and difference
- The **union** of sets X and Y, denoted as $X \cup Y$ is a set that contains every element from X, every element from Y and no additional elements
- The **intersection** of sets X and Y, denoted as $x \cap Y$, is a set that contains every element that is in both X and Y, and no additional elements
- The **difference** of sets X and Y, denoted as $X \\ Y$ is a set that contains every element that is in X, but not in Y, and no additional elements
- Union and intersection operations are commutative
#### Filter and map
- A **filter** operation on set X produces a subset containing only elements from X that satisfy a particular condition and the condition for filtering is commonly represented by a **filter predicate**, which is a function that takes an element as an argument and returns a boolean indicating whether that element will be in the filtered subset
- A **map** operation on set X creates a new set by applying some function F to each element

### 12.3: Static and dynamic set operations
- A **dynamic set is a set that can change after it has been constructed, while a **static set** doesn't change. A static set is usually constructed with a collection of elements
- Static sets support most set operations by returning a new set with the operation's result.

| Operation                                | Dynamic set support? | Static set support? |
|------------------------------------------|----------------------|---------------------|
| Construction from a collection of values | Yes                  | Yes                 |
| Count number of elements                 | Yes                  | Yes                 |
| Search                                   | Yes                  | Yes                 |
| Add element                              | Yes                  | No                  |
| Remove element                           | Yes                  | No                  |
| Union (returns new set)                  | Yes                  | Yes                 |
| Intersection (returns new set)           | Yes                  | Yes                 |
| Difference (returns new set)             | Yes                  | Yes                 |
| Filter (returns new set)                 | Yes                  | Yes                 |
| Map (returns new set)                    | Yes                  | Yes                 |