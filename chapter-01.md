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
##### `break`, `continue`, and `pass` statements
- The `break` statement is used to immediately terminate the loop, if you are using this in nested structures, it will terminate the most immediately enclosing loop
- The `continue` statement is used to stop the current iteration of the loop, but subsequent iterations will continue as expected
- The `pass` statement does nothing, but can be used syntactically as the body of a control structure, allowing that block to occur with nothing performed

### 1.6: Functions
- Functions (which are distinct from methods) are a "traditional, stateless function that is invoked without the context of a particular class or an instance of that class".
  - Method is used to describe a member function that is invoked upon a specific object using object-oriented dot-notation syntax (ex. `data.sort()`)
```python
# basic function definition syntax
def count(data, target):
    n = 0
    for item in data:
        if item == target:
            n += 1
    return n
```
- The first line, which begins with `def` is the function's **signature**, which gives a new identifier and the parameters. As Python is dynamically typed, parameter types do not have to be specified, nor the return type (though you should). These types should be stated in the function documentation though and can be enforced in the function itself
- The rest of the function is called the **body** and is usually an indented block of code
- When a function is called, an **activation record** is created for the current call. This includes the **namespace** to manage all identifiers with **local scope**, such as the function parameters or other identifiers defined within the function. Note that identifiers in the scope of the function call have no relation to any identifier with the same name in the calling scope
#### `return` statement
- The `return` statement is used to tell the function to cease execution immediately and return a value to the caller. If `return` is executed without an explicit value, it will return the `None` value (also if a function completes without executing a `return` statement)
- Multiple return statements can be defined in a function, but only one will ever be executed
#### Information passing
- The identifiers for expected parameters specified in the function signature are known as **formal parameters** and the objects that are sent by the caller when invoking the function are **actual parameters**. Parameter passing in Python follows the standard **assignment statement** semantics. When the function is called, each formal parameter is assigned to the respective actual parameter provided by the caller, in the context of the function's local scope
- The return value from the function to the caller also is implemented as an assignment.
- One advantage to this method of information passing is that objects are not copied
##### Mutable parameters
- Need to exercise caution when modifying mutable parameters as a part of a function, you cannot change the caller's variable through an assignment statement within the function
##### Default parameter values
- Python allows for functions to have more than one possible calling signature, these functions are referred to as **polymorphic**. To achieve this, functions can declare default formal parameters, which allows a caller to specify varying numbers of actual parameters. If you define one parameter as having a default in your function signature, all parameters following it must also have a default value
  - An example of this is Python's `range()` function. You can call it as `range(n)`, `range(start, stop)`, or `range(start, stop, step)`
##### Keyword parameters
- Traditionally, matching actual parameters sent by the caller to formal parameters declared by the function is through **positional arguments**, meaning the order of the actual parameters is matched with the order of the formal parameters, and values are assigned accordingly.
- Python supports **keyword arguments** where the actual parameter is explicitly assigned to the formal parameter by name, for example `foo(c=5)`
#### Python's built-in functions
- Python has a number of built-in functions that can be found [here](https://docs.python.org/3/library/functions.html)

### 1.7: Simple input and output
#### Console input and output
##### The `print` function
- The `print()` function generates standard output to the console and can be customized through different keyword parameters
  - `sep`: the desired separating string between each pair of arguments, defaults to " " a single space
  - `end`: the trailing string to output after the final argument, defaults to a newline
  - `file`: used to send output to an output file stream
##### The `input` function
- The `input()` function is the primary means for getting information from the user console. This function displays a prompt (if specified) then waits until the user enters a sequence of characters, followed by the return key
- `input()` returns a string of characters, so any type conversions must be done manually, with other functions like `int()`
##### A sample program
```python
age = int(input('Enter your age in years: '))
max_heart_rate = 206.9 - (0.67 * age)
target = 0.65 * max_heart_rate
print(f"Your target max heart rate is {max_heart_rate:.1f}.")
print(f'Your target fat-burning heart rate is {target:.1f}.')
```
#### Files
- Files are usually accessed through the built-in function `open()`, which takes as parameters the file name and an optional parameter to specify the access mode (read/write/etc.). Common file methods are shown below

| Syntax                  | Description                                                                                                                                                                            |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `fp.read()`             | Return the (remaining) contents of a readable file as a string                                                                                                                         |
| `fp.read(k)`            | Return the next k bytes of a readable file as a string                                                                                                                                 |
| `fp.readline()`         | Return (remainder of) the current line of a readable file as a string                                                                                                                  |
| `fp.readlines()`        | Return all (remaining) lines of a readable file as a list of strings                                                                                                                   |
| `for line in fp:`       | Iterate all (remaining) lines of a readable file                                                                                                                                       |
| `fp.seek(k)`            | Change the current position to be at the k^th byte of the file                                                                                                                         |
| `fp.tell()`             | Return the current position, measured as byte-offset from the start                                                                                                                    |
| `fp.write(string)`      | Write the given string at the current position of the writable file                                                                                                                    |
| `fp.writelines(seq)`    | Write each of the strings of the given sequence at the current position of the writable file; this command does not insert any newlines, beyond those that are embedded in the strings |
| `print(..., file = fp)` | Redirect the output of the print function to the file proxy fp                                                                                                                         |
##### Reading from a file
- The most basic command for reading from a file is `file.read(k)`, with k being the number of bytes to read. Without k, the entire file will be read. You can use the `readline()` method to get a single line at a time, or `readlines()` will return a list of lines
##### Writing to a file
- Text can be written to a file with the `write()` or `writelines()` methods

### 1.8 Exception Handling
- Exceptions are unexpected events that occur during a program's execution and they may come from logical errors or unanticipated conditions. **Exceptions** (or **errors**) are objects that are **raised** (or **thrown**) by code that runs into unexpected events, like running out of memory. Raised errors may be **caught** by code that *handles* the exception, but if exceptions are uncaught, they will cause the interpreter to stop executing and report the error to the console
#### Common exception types
- There are many types of exception classes and the `Exception` class is a base class for most other error types

| Class               | Description                                                                                          |
|---------------------|------------------------------------------------------------------------------------------------------|
| `Exception`         | A base class for most error types                                                                    |
| `AttributeError`    | Raised by syntax obj.foo, if obj has no member named foo                                             |
| `EOFError`          | Raised if the "end of file" is reached when reading console or file input                            |
| `IOError`           | Raised upon failure of an input/output operation (such as trying to open a file that does not exist) |
| `IndexError`        | Raised if an index to a sequence is out of bounds                                                    |
| `KeyError`          | Raised if a nonexistent key is requested from a set or dictionary                                    |
| `KeyboardInterrupt` | Raised if the user presses the keys ctrl-c while the program is executing                            |
| `NameError`         | Raised if a nonexistent identifier is used                                                           |
| `StopIteration`     | Raised by next(iterator) if no element; see Section 1.9                                              |
| `TypeError`         | Raised when the wrong type of parameter is sent to a function                                        |
| `ValueError`        | Raised when a parameter has an invalid value (e.g., sqrt(-5))                                        |
| `ZeroDivisionError` | Raised when any operator related to division is used with 0 as the divisor                           |
#### Raising an exception
- An exception can be thrown/raised using the `raise` statement, along with the instance of an exception class that addresses the problem, for example `raise ValueError("x cannot be negative")`. The syntax raises a new instance of the ValueError class, and the error message is a parameter to the constructor. If the exception is not caught, it will continue propagating up to broader contexts
- If checking validity of parameters, it is common to verify that parameters are of the correct type first using `isinstance(obj, cls)`, then to verify an appropriate value
- How much error-checking to perform in functions is debatable, adding type and value checks for every parameter adds execution time and can muddle the code
#### Catching an exception
- One strategy for managing exception cases is **"look before you leap"**, where validations are performed proactively to avoid exceptions
- Another strategy is **"it is easier to ask for forgiveness than it is to get permission"**, where we do not spend extra time safeguarding against every possible exception case, as long as we can handle problems after they arise. This is implemented with the **try-except** control structure
```python
try:
    ratio = x / y
except ZeroDivisionError:
    error_handling
```
- The `try` block is the primary code, which is followed by one or more `except` cases, that can define logic for different types of exceptions
- Exception handling is very useful when working with user input, or reading/writing files, as these interactions are often less predictable
- You can also use `except ZeroDivisionError as e`, where `e` is the instance of the thrown exception, which then can be utilized in the handling block
- Can also use `except (ValueError, EOFError)` to handle multiple types of exceptions within the single except clause
- Multiple `except` clauses can be used if different errors should be handled differently
- In an `except` clause, you can use the `raise` statement without any argument to re-raise the same exception that is currently being handled
- You can use `except:` without specifying any error types to catch any errors, however, this should not be used regularly
- A try/except statement can also have a `finally` class, which will always be executed. This is often used for cleanup actions, like closing a file

### 1.9: Iterators and Generators
- Many object types in Python are iterable, such as lists, tuples, and sets. The mechanism for iteration in Python is based on the conventions below
  - An **iterator** is an object that manages the iteration of a series of values. If `it` is an iterator object, then `next(it)` produces the next value from the series, and a `StopIteration` exception is raised when all elements are processed
  - An **iterable** is an object that produces an iterator via the syntax `iter(obj)`
- While instances of objects like lists are not iterators themselves, they are iterable. However, you can create an iterator by using `iter(data)` and then calling `next()` on the iterator will produce the next value 
- In the study of data structures, we'll explore techniques for supporting iteration, with a key issue being what happens if a collection is modified between when `iter()` is called to create the iterator and when `next()` is called. **Snapshot iterators** ensure that the iterator reports the values of the object at the time it was created, even if the objects have changed
- Python iterators often use a technique known as **lazy iteration** (as opposed to using a snapshot iterator) where the iterator waits until the next value is called before doing any necessary work. However, if the contents of the data structure of modified while iteration is underway, the iterator will report updated contents of the iterable, as it maintains its state as an index in the original object
#### Generators
- The most convenient technique for creating iterators in Python is through the use of **generators**, which is very similar to a function, but instead of return values, a **yield** statement is executed
```python
def factor_function(n):               # traditional function that computes factors
    results = []              # store factors in a new list
    for k in range(1,n+1):
        if n % k == 0:        # divides evenly, thus k is a factor
            results.append(k) # add k to the list of factors
    return results            # return the entire list

def factor_generator(n):             # generator that computes factors
    for k in range(1,n+1):
        if n % k == 0:      # divides evenly, thus k is a factor
            yield k         # yield this factor as next result
```
- Note that you cannot combine `yield` and `return` to indicate a result (other than a zero argument return, which will cause the generator to end execution)
- Generators can have multiple `yield` statements, which can be determined by flow of control

### 1.10: Additional Python Conveniences
#### Conditional expressions
- Python's **conditional expression** syntax can replace simple control structures and is generally expressed as `expr1 if condition else expr2`
- This evaluates expr1 if the condition is true, otherwise evaluates expr2
- these conditional expressions can serve as parameters to functions or can be assigned to variables
- This should really only be used when it increases the readability of the source code
#### Comprehension syntax
- Common programming task is to produce one series of values based on the processing of another series, which can often be accomplished through **comprehension syntax** such as **list comprehensions**
```python
# List comprehension format
n = 5
squares = [k * k for k in range(1, n + 1)]

# for loop format
squares = []
n = 5
for k in range(1, n + 1):
    squares.append(k * k)
```
- Other comprehension syntax is shown below for sets, generators, and dictionaries

| Syntax                               | Description              |
|--------------------------------------|--------------------------|
| `[ k*k for k in range(1, n+1) ]`     | list comprehension       |
| `{ k*k for k in range(1, n+1) }`     | set comprehension        |
| `( k*k for k in range(1, n+1) )`     | generator comprehension  |
| `{ k : k*k for k in range(1, n+1) }` | dictionary comprehension |
#### Packing and unpacking of sequences
- Tuples and other sequence types can be treated in a few different ways, the first is excluding the parentheses for a tuple if assigning a comma-separated list of values to a variable, this is called **automatic packing**
- Conversely, a tuple can be **unpacked**, where you assign a series of identifiers to the elements of a sequence, unpacking can be used with any iterable type
```python
# "automatic packing" of a tuple
data = 2, 4, 6, 8
assert type(data) == tuple

# "unpacking" of a tuple
a, b, c, d = data
assert a == 2
assert b == 4
assert c == 6
assert d ==8
```
##### Simultaneous assignments
- Combining automatic packing and unpacking is a technique known as **simultaneous assignment**. This can be a convenient way to swap the values of two variables, for example, `j, k = k, j`. Without this technique, this swap is more complicated
```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b
```

### 1.11: Scopes and Namespaces
- The process of determining values that are associated with each identifier is called **name resolution**. When an identifier is assigned to a value, the definition is made within a specific **scope**. Top-level assignments are usually made in what is called the **global** scope and assignments within a function have a scope that is **local** to the function call. Scope are represented using a **namespace**, which manages all identifiers that are currently defined in a given scope. Python gives each namespace its own dictionary that makes identifiers to their associated values. The function `dir()` reports the names of identifiers in a given namespace, while `vars()` returns the entire dictionary
- When an identifier is referenced, the most local namespace is searched first, followed by the next outer scope, etc.
- Each object has its own namespace and classes each have their own namespace as well
#### First-class objects
- **First-class objects** are types of objects that can be assigned to an identifier, passed as a parameter, or returned by a function. Data types (such as int, str, etc.) are first class objects, as well as functions and classes.

### 1.12 Modules and the import statement
- There are approximately 130-150 definitions that are included in Python's built-in namespace, but beyond that, there are thousands of other values, functions, and classes that are organized into libraries, known as **modules**, which can be **imported** into a program. Python's **import** statement loads modules into the current namespace can be used in a few different ways
```python
# import syntax examples
from math import pi, sqrt

from math import *

import math
```
#### Creating a new module
- To create a module, you just have to put functions into a file named with the **.py** suffix, which can then be imported like any other module
- Top-level commands with the module source code are executed when the module is first imported, but there is a way to embed commands that will only be executed if the module is directly invoked, not when it is imported. This approach can often be used to embed **unit tests** within the module itself
```python
if __name__ == "__main__":
    "code block goes here"
```
#### Existing modules
- There are a number of modules that are relevant to data structures and algorithms

| Module        | Description                                                                                   |
|---------------|-----------------------------------------------------------------------------------------------|
| `array`       | Provides compact array storage for primitive types                                            |
| `collections` | Defines additional data structures and abstract base classes involving collections of objects |
| `copy`        | Defines general functions for making copies of objects (see Section 2.6)                      |
| `heapq`       | Provides heap-based priority queue functions                                                  |
| `math`        | Defines common mathematical constants and functions                                           |
| `os`          | Provides support for interactions with the operating system                                   |
| `random`      | Provides random number generation                                                             |
| `re`          | Provides support for processing regular expressions                                           |
| `sys`         | Provides additional level of interaction with the Python interpreter                          |
| `time`        | Provides support for measuring time, or intentionally delaying a program                      |
##### Pseudorandom number generation
- The `random` module in Python provides the ability to generate pseudorandom numbers, which are numbers that are statistically random, but not necessarily truly random. **Pseudorandom number generator** uses a deterministic formula to generate the next number in a sequence based on one or more past numbers. A sample pseudorandom number generate is as follows
```python
# choose next number based on most recently chosen number
a = 3
b = 4
n = 7
cur = 2
next = (a * cur + b) % n
```
- Python uses a technique known as [**Mersenne twister**](https://en.wikipedia.org/wiki/Mersenne_Twister), but this should not be utilized in an application where on needs truly unpredictable random sequences. Instead, use something like sample radio static coming from outer space..
- As a pseudorandom number generator is determined by the previous number(s), the generator needs a place to start, called a **seed**. The sequence of numbers generated from a seed will always be the same
- Python's `random` module provides support for pseudorandom number generation by defining the `Random` class, this allows different parts of the application to create their own pseudorandom number generation. The functions/methods shown in the table below are top-level functions in the `random` module and methods supported by the `Random` class

| Syntax                       | Description                                                                             |
|------------------------------|-----------------------------------------------------------------------------------------|
| `seed(hashable)`             | Initialize the pseudorandom number generator based upon the hash value of the parameter |
| `random()`                   | Return a pseudorandom floating-point value in the interval [0.0, 1.0)                   |
| `randint(a,b)`               | Return a pseudorandom integer in the closed interval $[a, b]$ for parameters $a \leq b$ |
| `randrange(start,stop,step)` | Return a pseudorandom integer in the standard Python range indicated by the parameters  |
| `choice(seq)`                | Return an element of the given sequence chosen pseudorandomly                           |
| `shuffle(seq)`               | Reorder the elements of the given sequence pseudorandomly                               |

### 1.13: Exercises
- Write a short Python function, `is_multiple(n, m)` that takes two integer values and returns `True` if $n$ is a multiple of $m$ (that is, if $n = m \cdot i$ for some integer $i$), and `False` otherwise

### 1.14: Chapter notes
- Additional references
  - Mark Lutz - "Learning Python" and "Programming Python"
  - John Zelle - "Python Programming: An Introduction to Computer Science"
  - David Beazley - "Python Essential Reference"
  - Mark Summerfield - "Python in Practice" and "Programming in Python 3"
  - Ljiljana Perkovic - "Introduction to Computing Using Python"