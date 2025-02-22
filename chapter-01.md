# Chapter 1: Python Primer

### 1.1: Python overview
#### Python Interpreter
- Python is an `interpreted` langauge, with commands executed through software known as the Python interpreter. The interpreter receives the command, evaluates it, and then reports the results of the command.
- Interpreter can be used interactively, but is often used with commands written in advance (in `source code`/`scripts`), saved in .py files, and then executed.
#### Preview of a Python program
- Python relies heavily on whitespace, which is used to delimit bodies of control structures and terminate statements. Comments are annotated with a `#` character, which marks the remained of a line as a comment
```python
print('Welcome to the GPA calculator.')
print('Please enter all your letter grades, one per line.')
print('Enter a blank line to designate the end.')
# dictionary maps from letter grade to point value
points = {'A+':4.0, 'A':4.0, 'A-':3.67, 'B+':3.33, 'B':3.0, 'B-':2.67,
          'C+':2.33, 'C':2.0, 'C':1.67, 'D+':1.33, 'D':1.0, 'F':0.0}
num_courses = 0
total_points = 0
done = False
while not done:
    grade = input()                        # read line from user
    if grade == '':                        # empty line was entered
        done = True
    elif grade not in points:              # unrecognized grade entered
        print(f"Unknown grade '{grade}' being ignored")
    else:
        num_courses += 1
        total_points += points[grade]
if num_courses > 0:                        # avoid division by zero
    print(f'Your GPA is {total_points/num_courses:.3f}')
```

### 1.2: Objects in Python
- Python is object-oriented and `classes` form the basis of all data types (built-in examples include `int` (integers) and `float` (floating-point values))
#### Identifiers, objects, and the assignment statement
- Example is `temperature = 98.6`, where *temperature* is the `identifier` (name) and the associated `object` is on the right hand side, in this instance 98.6
##### Identifiers
- Identifiers are case-sensitive, so `temperature != Temperature`. Identifiers can be almost any combination of letters, numbers, and underscore characters (but cannot begin with a number), and cannot be a reserved word. Python identifiers are similar to Java variables/pointer variable in C++. Each identifier is associated with the memory address of the object it references. Python identifiers can reference the special object `None`, which is similar to `null` in Java or `nullptr` in C++
- Python is `dynamically-typed`, which means that the types for identifiers are not declared in advance and any identifier can be associated/reassociated with any type of object. However, the objects themselves have a fixed type. You can assign multiple identifiers to an existing object, which can create an `alias`
#### Creating and using objects
##### Instantiation
- Creating a new instance of a class is called `instantiation` and generally, the syntax for instantiating an object is by invoking the `constructor` of the class (ex. `w = Widget()`, or `w = Widget(a, b, c)`). Many Python built-in classes support constructors, but also support a `literal` form of designating new class instances. You can also indirectly instantiate a class by calling a function that returns an instance of that class
##### Calling methods
- Python supports traditional functions (ex. `sorted(data)`) with parameters, but many Python classes also define one or more `methods`/`member functions` (ex. `data.sort()`), where the object on the left of the dot is the object open which the method is invoked. When using a method, it's important to know if an object only accesses data about the state of the object (`accessors`) or if it changes the state of the object (`mutators`/`update methods`)
#### Python's built-in classes
- Certain classes in Python are immutable, which means objects of those classes have fixed values once instantiated and cannot be changed

| Class       | Description                                   | Immutable? |
|-------------|-----------------------------------------------|------------|
| `bool`      | Boolean value                                 | yes        |
| `int`       | integer (arbitrary magnitude)                 | yes        |
| `float`     | floating-point number                         | yes        |
| `list`      | mutable sequence of objects                   | no         |
| `tuple`     | immutable sequence of objects                 | yes        |
| `str`       | character string                              | yes        |
| `set`       | unordered set of distinct objects             | no         |
| `frozenset` | immutable form of set class                   | yes        |
| `dict`      | dictionary (also known as an associative map) | no         |
##### The `bool` class
- `bool` class is used to manipulate logical (Boolean) values, only two instances are the literals `True` and `False`, and the default constructor `bool()` returns `False`. You can use `bool(object)` to create a boolean from an object, numbers evaluate to `False` if they are zero/`True` if they are nonzero. Sequences and collections (strings, lists, etc.) evaluate to `False` if they are empty and `True` if they are not empty. This class has important applications for control structures
##### The `int` class
- `int` and `float` are primary numeric types. `int` represents integers, with Python choosing an appropriate internal representation of the integer object based on its magnitude (so no short, long, int, like in Java). One can also represent an integer in binary/octal/hexadecimal with the prefix of `0` and then a character to represent the base, such as `0b1011` (binary), `0o52` (octal), and `0x7f` (hexadecimal). The constructor `int()` returns 0 by default, but can be used to create integers from values of other types, such as `int(3.14) == 3` or `int("3") == 3`
##### The `float` class
- `float` is the only floating-point type in Python, with fixed-precision representation. The `float()` constructor returns `0.0` by default, but can also be used with an object as a parameter, which it will try to convert

### 1.3: Operators and Expressions
- Existing values of objects can be combined into **expressions** with a variety of symbols/keywords known as **operators**, such as `a + b`, with the specific operation performed depending on the object's types. Python follows a specific order of operations, but this can be overridden by using parentheses.
#### Arithmetic operators
| Syntax   | Operation           |
|----------|---------------------|
| `a + b`  | addition            |
| `a - b`  | subtraction         |
| `-a`     | unary negation      |
| `a * b`  | multiplication      |
| `a / b`  | true division       |
| `a // b` | integer division    |
| `a % b`  | the modulo operator |
- If one or both operands are `float`, then the result will be a `float` object
##### Treatment of division
- In Python, `/` is used to designate **true division**, where we receive a floating-point value of the computation (ex, `27 / 4 == 6.75`). You can use `//` for integral division, where you will receive the floor of the division as your result, so `27 // 4 == 6`. Using `%` will return the remainder of the integral division, so `27 // 4 == 3`
##### Bitwise operators
- Python has a number of bitwise operators that can be used for manipulation of individual bits of binary represented with an integer. 

| Syntax   | Operation                                                 |
|----------|-----------------------------------------------------------|
| `a & b`  | bitwise and                                               |
| `a \| b` | bitwise or                                                |
| `a ^ b`  | bitwise exclusive-or                                      |
| `a << k` | shift `a` left by `k` bits, filling in with zeros         |
| `a >> k` | shift `a` right by `k` bits, filling in with the sign bit |
| `-a`     | bitwise complement (unary)                                |

##### Extended assignment operators
- For each binary operator, Python supports an extended assignment operator, such as `count += 5`, which is the same as `count = count + 5`. Remember, that for immutable types (numbers/strings, etc), this extended assignment will create a newly constructed object and then assign it to the original identifier
##### Comparison operators
- Certain data types may have defined natural orders that use the following operators

| Syntax   | Operation                |
|----------|--------------------------|
| `a < b`  | less than                |
| `a <= b` | less than or equal to    |
| `a > b`  | greater than             |
| `a >= b` | greater than or equal to |
- Comparing numeric types with these operators is straightforward, but for types like strings, there may be unintuitive comparisons (for example, strings are case-sensitive and determined lexicographically)
##### Equality operators
| Syntax       | Operation            |
|--------------|----------------------|
| `a is b`     | same identity        |
| `a is not b` | different identity   |
| `a == b`     | equivalent value     |
| `a != b`     | not equivalent value |
- It is important to note that `a is b` and `a == b` are not the same. `a is b` evaluates to `True` if the identifiers `a` and `b` are aliases for the *same object*, while `a == b` tests more general equivalence, which is "are the values equal (even if not the same literal object)". In most instances, it is probably the correct choice to use `==` and `!=`
##### Logical operators
- There are a few keyword operators for boolean values

| Syntax    | Operation       |
|-----------|-----------------|
| `not a`   | unary negation  |
| `a and b` | conditional and |
| `a or b`  | conditional or  |
- The `and` and `or` operators **short-circuit**, which is that they do not evaluate the second half of a comparison if the result can be determined by the first value, this can be helpful in many programming situations
##### Compound expressions and operator precedence
- Formal order of precedence in Python is shown in the table below, where higher precedence operations are performed before those with lower precedence, but can be changed with parentheses

| Type                                               | Symbols                                            |
|----------------------------------------------------|----------------------------------------------------|
| member access                                      | `expr.member`                                      |
| function/method call<br>collection subscript/slice | `expr(...)`<br>`expr[...]`                         |
| exponentiation                                     | `**`                                               |
| unary operators                                    | `+expr` `-expr` `~expr`                            |
| multiplication, division                           | `*` `/` `//` `%`                                   |
| addition, subtraction                              | `+` `-`                                            |
| bitwise shift                                      | `<<` `>>`                                          |
| bitwise and                                        | `&`                                                |
| bitwise exclusive-or                               | `^`                                                |
| bitwise or                                         | `\|`                                               |
| comparisons<br>containment                         | `is, is not, ==, !=, <, <=, >, >=`<br>`in, not in` |
| logical not                                        | `not expr`                                         |
| logical and                                        | `and`                                              |
| logical or                                         | `or`                                               |
| ternary conditional                                | `expr1 if cond else expr2`                         |
| assignments                                        | `=, +=, -=, *=` etc                                |
##### Chained expressions
- Python allows for **chained expressions**, where multiple identifiers are assigned to the rightmost value, ex. `x = y = 0`
- Additionally, Python allows for the **chaining** of comparison operators, such as `1 <= x + y <= 10`, which is equivalent to `(1 <= x + y) and (x + y <= 10)`
#### Participation Activity
- `1 + 2 * 3 + 4 == 11`: multiplication operator has the highest precedence
- `10-3 - 4+1 == 4`: spacing in this example is irrelevant and is misleading, these operators have the same precedence so they are evaluated left-to-right
- `7 + 8 // 3 == 9`: division operator has precedence over addition
- `2 + 3 * 4 == 14`: multiplication has precedence over addition
- `8 - 3 + 1 == 6`: Python evaluates this from left to right
- `4 * (2 + 5) == 28`: Python computes the portion in parentheses prior to multiplication

### 1.4: Collection Types
- Python has a number of built-in classes that can represent collections of other objects, which includes `str`, `list`, `tuple`, `set`, `frozenset`, and `dict`
#### The `str` class
- The `str` class represents an immutable sequence of text characters, using [Unicode](https://home.unicode.org/). Strings are used to represent all text characters, including strings of just one character. Strings can be enclosed in single quotes (`'`) or double quotes (`"`).
- The string delimiter itself can be represented in a string by using a backslash `\`, called an *escape character*. Backslashes themselves must be escaped to show up in strings (`\\`). Other common escape characters are `\n` (newline) and `\t` (tab)
- Can also use triple quotes to begin and end a string literal, which allows you to create multi-line strings
- Strings are an **array-based** structure, characters are stored sequentially within consecutive cells of memory. Characters of a string can be accessed via a numeric index, with Python being a zero-indexed language. You can also use negative indices (starting from -1) to count from the end of a string
- Python uses slicing notation to create substrings of a string, ex. `"sample"[:2] == "sa"` (note the stop index is excluded). String lengths can be calculated with `len()`. The `+` operator concatenates two strings, the `*` operator repeats concatenation, and the syntax `pattern in s` checks to see if `pattern` is in the string `s`
- Strings can be compared with operators like `<`, but note that this comparison is based on lexicographical order, performing an element by element comparison
#### The `list` and `tuple` classes
- `list` and `tuple` classes are general classes that can represent sequences of arbitrary objects. `list` instances are mutable (items can be added/removed/replaced), while tuples are immutable. These two classes are **referential** structures, storing sequences of **references** to objects that are elements of the sequences
  - See Python documentation for [lists](https://docs.python.org/3/library/stdtypes.html#lists) and [tuples](https://docs.python.org/3/library/stdtypes.html#tuples)
- You can verify that a list is mutable by using the code sample below, which uses the [`id()`](https://docs.python.org/3/library/functions.html#id) built-in function
```python
initial_list = [1, 3, 4]
list_identity = id(initial_list)
initial_list.append(4)
assert initial_list == [1, 2, 3, 4]
new_identity = id(initial_list)
assert new_identity == list_identity
```
- Lists and tuples support indexing, similar to strings

| List Operator Syntax | Description                                                                                   |
|----------------------|-----------------------------------------------------------------------------------------------|
| `s[j]`               | element at index `j`                                                                          |
| `s[start:stop]`      | slice including elements from index `start` up to but not including `stop`                    |
| `s[start:stop:step]` | slice including indices `start`, `start+step`, `start+2*step`, up to but not including `stop` |
| `len(s)`             | the length of the sequence                                                                    |
| `s + t`              | concatenation of sequences `s` and `t`                                                        |
| `s * k`              | shorthand for `s + s + ... + s` (repeated `k` times)                                          |
| `val in s`           | `True` if `val` is an element of the sequence (or substring, when `s` is a string)            |
| `val not in s`       | more readable form equivalent to `not val in s`                                               |
| `s == t`             | equivalent (element by element)                                                               |
| `s != t`             | not equivalent                                                                                |
| `s < t`              | lexicographically less than                                                                   |
| `s <= t`             | lexigraphically less than or equal to                                                         |
| `s > t`              | lexicographically greater than                                                                |
| `s >= t`             | lexicographically greater than or equal to                                                    |
- List delimiters are `[]` (which is an empty list) and the `list()` constructor creates an empty list by default. However, you can pass any parameter of an **iterable** type to the constructor
- Lists support syntax that allows you to replace or delete items at specific indexes
```python
ls = [1]
ls[0] = 2
assert ls == [2]
del ls[0]
assert ls == []
```
- Tuple delimiters are `()` (which is an empty tuple). Be careful when using tuples that only contain one value as they need to have a comma after the value, for example `(17, )`
#### The `set` and `frozenset` classes
- The **set** class is used to represent a mathematical set (collection of elements) without duplicates and with no inherent order. A big advantage of sets over lists is they are very optimized for checking if an item is present in the set (based on **hash tables**)
  - See Python documentation [here](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)
- Important to note that sets do not maintain items in any particular order and only and only objects of immutable types (integers, strings, etc.) can be contained in sets
- Curly braces `{}` are used as set delimiters (ex. `{'red', 'green', 'blue'}`), but note that `{}` does not create an empty set, it creates an empty dictionary, you must use `set()` to create the empty set.

| Set Operator Syntax | Description |
|---------------------|-------------|
| `key in s`          | containment check |
| `key not in s`      | equivalent to `not key in s` |
| `s1 == s2`          | `s1` is equivalent to `s2` |
| `s1 != s2`          | `s1` is not equivalent to `s2` |
| `s1 <= s2`          | s1 is a subset of s2 |
| `s1 < s2`           | s1 is a proper subset of s2 |
| `s1 >= s2`          | s1 is a superset of s2 |
| `s1 > s2`           | s1 is a proper superset of s2 |
| `s1 \| s2`          | the union of s1 and s2 |
| `s1 & s2`           | the intersection of s1 and s2 |
| `s1 - s2`           | the set of elements in s1, but not s2 |
| `s1 ^ s2`           | the set of elements in precisely one of s1 or s2 |
- Because sets do not have guaranteed orders, the comparison operators are not lexicographic like for lists, but rather are like the mathematical operators
#### The `dict` class
- Python's **dict** class is a dictionary, or mapping, of a set of distinct **keys** to associated **values**. Dictionaries are implemented very similarly to sets, with curly braces `{}` (in this instance, this is the empty dictionary), for example, `{"ga": "Irish", "de": "German"}`. Dictionaries are not inherently ordered
  - Python documentation [here](https://docs.python.org/3/library/stdtypes.html#dict)
- Most common behavior of a dictionary is accessing a value associated with a particular key, through `d[k]`

| Dictionary Operator Syntax | Description                                                                                                                         |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `d[key]`                   | value associated with given key                                                                                                     |
| `d[key] = value`           | set (or reset) the value associated with given key                                                                                  |
| `del d[key]`               | remove key and its associated value from dictionary                                                                                 |
| `key in d`                 | containment check                                                                                                                   |
| `key not in d`             | non-containment check                                                                                                               |
| `d1 == d2`                 | d1 is equivalent to d2                                                                                                              |
| `d1 != d2`                 | d1 is not equivalent to d2                                                                                                          |
| `d1 \| d2`                 | returns a new dictionary including entries from d1 and d2. If a key exists in both d1 and d2, the result includes the entry from d2 |
#### Extended assignment operators
- There are some slight differences when using operators like `+=` with mutable collections. The example `primes = primes + [17, 19]` creates a new list on the right hand side of the operator, then reassigns `primes` to the new list. If an alias existed for the original list, that original list would not be updated. However, when actually using the `+=` operator, the original list is mutated
```python
numbers = [1, 2, 3, 4]
numbers_alias = numbers
assert id(numbers) == id(numbers_alias)
numbers += [5, 6]
assert numbers == numbers_alias
numbers = numbers + [7, 8]
assert numbers == [1, 2, 3, 4, 5, 6, 7, 8]
assert numbers_alias == [1, 2, 3, 4, 5, 6]
```
### 1.5: Control Flow
- Control structures, such as conditional statements and loops, are delimited by a colon `:` and subsequent lines are indented, which designate the extent of that block of code (similar to how function bodies and class bodies are designated)
#### Conditionals
- Conditionals, also called **if statements**, execute a given block of code based on the evaluation of one or more boolean expressions
```python
if first_condition:
    first_body
elif second_condition:
    second_body
elif third_condition:
    third_body
else:
    fourth_body
```
- The conditions are all boolean expressions and the bodies are one or more commands to be executed. Once one of the bodies is executed, no further conditions are evaluated or bodies executed.
- Control structures may be nested, which relies on further indentation
#### Loops
- Python has two different looping constructs, a **while loop** and a **for loop**. While loops allow repetition based on repeated testing of a boolean condition, while for loops iterate through values from a defined series
##### While loops
- General syntax is as follows, where `condition` can be any boolean expression and the `body` can be any block of code (including nested control structures). If the condition is true, the body is executed, if it is false, the loop is exited
```python
while condition:
    body
```
##### For loops
- For loops can be used on any type of iterable, such as a list, tuple, str, set, dict, or file, general syntax is as follows
```python
for element in iteratable:
    body
```
- The loop body executes once for each element in the sequence and the identifier (`element` in this instance) is available within the loop body
- For loops have simplicity in that you do not need to manage indexes or create boolean conditions
##### Index-based for loops
- For loops are nice, but they do not tell you where an element resides in the sequence. If you want to loop through the series of indices of a sequence, use the following
```python
data = "string length"
for j in range(len(data)):
    print(data[j])
```
##### `break` and `continue` statements
- The `break` statement is used to immediately terminate the loop, if you are using this in nested structures, it will terminate the most immediately enclosing loop
- The `continue` statement is used to stop the current iteration of the loop, but subsequent iterations will continue as expected
