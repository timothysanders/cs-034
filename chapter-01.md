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