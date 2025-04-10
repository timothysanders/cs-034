# Chapter 8: Hash Tables

### 8.1: Hash Tables
#### Hash table overview
- **Hash table** is a data structure that stored unordered items by mapping/hashing each item to a location in an array/vector
- The main advantage of hash tables is that searching/inserting/removing an item is a constant time operation (`O(1)`), compared to `O(N)` for searching a list or `O(log N)` for binary search.
- An item's **key** is the value used to map to an index and keys are ideally unique, so that the search algorithm can find a specific item by a particular key
- Each hash table array element is called a **bucket**, and a **hash function** computes a bucket index from the item's key
- Normally, items being stored in a hash table are objects with several fields and whatever unique ID is present can be used for storage
#### Hash table operations
- A common hash function is the **modulo operator `%`**, which computes an integer remainder when dividing two numbers
- The hash table operations of insert, remove, and search use the hash function to determine an item's bucket
##### Empty Cells
- How you determine if a cell is empty depends on the implementation, if the elements are pointers, it could be represented as null/None
#### Collisions
- A **collision** occurs when an item being inserted into a hash table maps to the same bucket as an existing item in the table. Different techniques are used to handle these collisions during insertions, such as chaining or open addressing
- **Chaining** is a collision resolution technique where each bucket has a list of items
- **Open addressing** is a collision resolution technique where collisions are resolved by looking for an empty bucket elsewhere
- Given an example of a hash function of `key % 10`, 55 is inserted into bucket 5
  - Chaining: later inserting 75 gives you `[55, 75]` at bucket 5
  - Open addressing: might put 75 in bucket 6

### 8.2: Chaining
- **Chaining** handles hash collisions by use a list for each bucket and each list can store multiple items that map to the same bucket. Insert uses the item's key to first determine the bucket, then inserts the item into that bucket's list. Searching first determines the bucket, then searches the bucket's list. Removes follow the same pattern

### 8.3: Linear Probing
#### Linear Probing Overview
- A hash table with **linear probing** handles collisions by starting at the key's mapped bucket, then linearly searching subsequent buckets until an empty bucket is found
#### Empty bucket types
- Linear probing distinguishes between two types of empty buckets, an **empty-since-start** bucket (which has been empty since the table was created) and an **empty-after-removal** bucket, which had an item, but it was removed. In these instances, searching only stops for empty-since-start buckets
#### Inserts using linear probing
- When using linear probing, a hash table insert algorithm uses the item's key to determine the initial bucket, linearly probes (checks) each bucket, then inserts the item in the next empty bucket (here the empty bucket type does not matter). If probing reaches the last bucket, then probing continues at bucket 0. The algorithm returns true if the item was inserted and false otherwise (all buckets are occupied)
#### Removals using linear probing
- Using linear probing, the hash table remove algorithm uses the sought item's key to determine the initial bucket, then checks each bucket until a matching item is found, an empty-since-start bucket is found, or all buckets have been probed. If the item is found, it is removed, and the bucket marked empty-after-removal
- If the algorithm encounters an empty-after-removal bucket, the algorithm keeps going, because the searched item may be in a subsequent bucket
#### Searching using linear probing
- In search with linear probing, the sought item's key is used to determine the initial bucket. The algorithm then probes each bucket until either a match is found (which returns the item), an empty-since-start bucket is found (returns none), or all buckets are probed without a match (none is returned). Empty after removal buckets do not stop the search

### 8.4: Quadratic Probing
#### Overview and Insertion
- Hash table with **quadratic probing** handles a collision by starting at a key's mapped bucket, then quadratically searching buckets until an empty bucket is found
  - If an item's mapped bucket is `H`, the formula $(H + c_1 \cdot i + c_2 \cdot i^2)\text{ mod }(\text{tablesize})$ is used to determine the item's index in the hash table. $c_1$ and $c_2$ are programmer defined constants for probing. Inserting a key uses a formula starting with `i = 0` to repeatedly search the hash table until an empty bucket is found, incrementing by 1 each time an empty bucket is not found. Iterating through sequential values of `i` to obtain the desired index is called the probing sequence.
    - $h(k, i) = (h(k) + c_1 \cdot i + c_2 \cdot i^2) \bmod (\text{tablesize})$
```python
def quadratic_probe(h: int, c1: int, c2: int, i: int = 0) -> int:
    """
    
    """
    return h + (c1 * i) + (c2 * i^2)
```
#### Search and removal
- The search algorithm uses the probing sequence until the key being searched for is found or an empty-since-start bucket is found. If the removal algorithm finds the key to remove, it will remove it and mark the bucket as empty-after-removal

### 8.5: Double hashing
#### Overview
- **Double hashing** is an open-addressing collision resolution technique that uses two different hash functions to compute bucket indices. Using hash functions h1 and h2, a key's index in the table is computed by $(h1(key) + i \cdot h2(key))\text{ mod }(tablesize)$. Starting with i=0, inserting the key repeatedly uses the formula to search hash table buckets until an empty bucket is found. Each time an empty bucket is not found, `i` is incremented by 1. Iterating through sequential `i` values to find a particular table index is called the **probing sequence**
```python
def double_hash(key: int, i: int) -> int:
    """
    Example implementation of double hashing.
    
    Parameters
    ----------
    key : int
    i : int
    
    Returns
    -------
    int
    """
    return (key % 11 + i * (5 - key % 5)) % 11
```
#### Insertion, search, and removal
- Using double hashing, a hash table search algorithm probes/checks each bucket using the probing sequence composed of two hash functions. The search continues until a matching item is found (returning the item), an empty-since-start bucket is found (returning null), or all buckets are probed without a match (returning null)
- A hash table insert probes each bucket using the probing sequence, and inserts the item in the next empty bucket (empty kind does not matter)
- A hash table removal first searches for the item's key. If it is found, the item is removed, and the bucket is marked empty-after-removal

### 8.6: Hash table resizing
#### Resize operation
- A hash table **resize** increases the number of buckets, while preserving all existing items. Hash tables with $N$ buckets are usually resized to the next prime number $\geq N \cdot 2$. This allocates a new array and all old items are re-inserted into the new array, which makes the time complexity of the resize operation $O(N)$
#### When to resize
- A hash table's **load factor** is the number of items in the hash table, divided by the number of buckets. For example, a hash table with 18 items and 31 buckets has a load factor of $18 \div 31 = 0.58$. This load factor can be used to determine when to resize a table.
- The implementation of a hash table can choose to resize when one or more of the following values exceeds a given threshold
  - Load factor
  - When using open-addressing, the number of collisions during an insertion
  - When using chaining, the size of a bucket's linked list

### 8.7: Common hash functions
#### A good hash function minimizes collisions
- Hash tables are fast if they minimize collisions. A **perfect hash function** maps items to buckets with no collisions. A perfect hash function can be created if the number of items and all possible item keys are known beforehand. This can make the runtime $O(1)$ for insert, search, and remove.
- Good hash functions distribute items evenly into buckets. When using chaining, short hash functions distribute results into short lists, which makes inserts, searches, and removes fast. With linear probing, a good hash function will avoid hashing multiple items to consecutive buckets and this helps minimize the average linear probing length to get fast inserts, searches, and removals. On average, a good hash function achieves $O(1)$ inserts, searches, and removals, but in the worst case may require $O(N)$
- The performance of a hash function depends on the hash table size and knowledge of the expected keys
#### Modulo hash function
- A **modulo hash** uses the remainder from division of the key by hash table size $N$
```python
def modulo_hash(key: int, n: int) -> int:
    """
    Return the remainder of the key divided by the hash table size.
    """
    return key % n
```
#### Mid-square hash function
- A **mid-square hash** squares the key, extracts $R$ digits from the result's middle, and returns the remainder of the middle digits divided by the hash table size $N$. For $N$ buckets, $R$ must be greater than or equal to $[log_{10}N]$ to index. The process of squaring and extracting middle digits reduces the likelihood of keys mapping to just a few buckets.
  - Example: hash table of 100 entries and key of 453, decimal (base 10) mid-square hash function computes 453 * 453 = 205209, returning the middle digits 52
```python
import math

def decimal_mid_square_hash(key: int, r: int) -> int:
    x = key**2
    if x == 0:
        n = 1
    else:
        n = int(math.floor(math.log10(abs(x)))) + 1
    if r > n:
        raise ValueError("The number of digits to extract cannot exceed the total number of digits in x.")
    m = (n - r) // 2
    divisor = 10 ** (n - (m + r))
    middle = (x // divisor) % (10 ** r)
    return middle
```
#### Mid-square hash function base 2 implementation
- Mid-square hash is typically implemented using binary (base 2), and not decimal, as binary implementation is faster. Decimal implementation requires converting the square of the key to a string, extracting a substring for the middle digits, and converting that substring to an integer. Binary implementation only requires a few shift and bitwise AND operations.
- Binary mid-square hash extracts the middle R bits, and returns the remainder of the middle bits divided by the hash table size N, where R is greater than or equal to $[log_2N]$
```python
def binary_mid_square_hash(key: int, r: int, n: int) -> int:
    """
    Hash a key using the Mid-Square method.
    
    Parameters
    ----------
    key : int
    r : int
    n : int
    
    Returns
    -------
    int
    """
    key_squared = key**2
    low_bits_to_remove = (32 - r) // 2
    extracted_bits = key_squared >> low_bits_to_remove
    mask = 0xFFFFFFFF >> (32 - r)
    extracted_bits &= mask
    return extracted_bits % n
```
#### Multiplicative string hash function
- A **multiplicative string hash repeatedly multiplies the hash value and adds the ASCII (or Unicode) value of each character in the string. Multiplicative hash function for strings starts with a large initial value, then for each character, multiplies the current hash value by a multiplier (usually prime) and adds the character's value. Then the function returns the remainder of the sum divided by the hash table size $N$
- A popular version of this function uses an initial value of 5381 and a multiplier of 33, which performs well for hashing short English strings
```python
def multiplicative_hash(key: str, multiplier: int, initial_value: int = 0) -> int:
    hash_value = initial_value
    for x in key:
        hash_value = (hash_value * multiplier) + ord(x)
    return hash_value
```
##### Additional references
- [Hash Functions: An Empirical Comparison](http://www.codeproject.com/Articles/32829/Hash-Functions-An-Empirical-Comparison)
- [Hash Functions and Block Ciphers](http://www.burtleburtle.net/bob/hash/index.html)

### 8.8: Direct Hashing
#### Direct hashing overview
- A **direct hash function** uses the item's key as the bucket index. A hash table with a direct hash function is called a **direct access table**. Given a key, a direct access table **search** algorithm returns the item at the index key if the bucket is not empty and returns None if empty
#### Limitations of direct hashing
- Direct access tables have the advantage of no collisions, because each key is unique, and each gets a unique bucket, so no collisions can occur. However, this imposes the following limitations
  1. All keys must be non-negative integers (though in some applications, keys may be negative)
  2. The hash table's size equals the largest key value plus 1, which can be very large

### 8.9 Hashing Algorithms: Cryptography, Password Hashing
#### Cryptography
- **Cryptography** is a field of study focused on transmitting data securely, this commonly starts with **encryption**, which is alteration of data to hide the original meaning. The counterpart to this is **decryption**, which is reconstructing original data from encrypted data
#### Hashing functions for data
- Hash functions can be used to created hash values for data in contexts other than hash tables and are often used to verify data integrity. MD5, a hashing algorithm, produces 128-bit hash values for any input. It cannot be used to reconstruct data, but it can be used to help verify that the data is not corrupted/altered.
#### Cryptographic hashing
- A **cryptographic hash function** is a hash function that is specifically designed for cryptography and is commonly used for encrypting/decrypting data
- A **password hashing function** is a cryptographic hashing function that produces a hash value for a password. Databases commonly store the password's hash instead of its plain-text value. When the user logs in, the password is hashed and then compared against the stored hash. This helps keep the passwords themselves more secure. Sometimes random extra data (a "salt") is computed and stored alongside the password hash value
