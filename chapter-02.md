# Chapter 2: Object-Oriented Programming

### 2.1: Goals, principles, and patterns
- The main "actors" in object-oriented programming are **objects**. Every object is an **instance** of a **class**. Each class is a consistent view of the objects that are instances of the class. The class definition typically defines **instance variables**, sometimes called **data members**, for the object, as well as **methods** (sometimes called **member functions**) that the object can execute.
#### Object-oriented design goals
- Software implementations should aim to achieve robustness, adaptability, and reusability
##### Robustness
- In addition to the output of our software being "correct" in all circumstances, we want our program to be robust, which means capable of handling unexpected inputs and gracefully recovering from errors. This is particularly critical for software that can cause injuries or loss of life (think medical applications)
##### Adaptability
- Software needs to evolve over time to adjust to the conditions in its environment. This is adaptability (or evolvability), and it is related to portability, meaning the ability of software to run on different types of hardware, with minimal changes. Python provides significant portability
##### Reusability
- Along with adaptability, software should be reusable, meaning the same code can be used as a component for multiple different systems. However, this does not mean to simply copy/paste code from one project to another
#### Object-oriented design principles
- The chief principles of object-oriented design are **modularity**, **abstraction**, and **encapsulation**
##### Modularity
- Modern software systems often have multiple different components that interact, and these components must be well organized. **Modularity** refers to a principle of organizing components of a software system into separate functional units
- Modularity helps increase robustness, as we have individual, separate components, that can be more easily tested/debugged as they are integrated into larger systems. Additionally, if a bug shows up later in a component, it can more easily be fixed in isolation, without disturbing the rest of the system.
##### Abstraction
- Abstraction is meant to distill complicated systems down to their most fundamental parts. Describing parts of the system involves naming them and explaining their functionality. Applying abstraction paradigms to design of data structures gives rise to **abstract data types (ADTs)**. ADT is a mathematical model of a data structure that specifies type of data stored, the operations supported on them, and the types of parameters of the operations. It specifies what each operation does, but not how it does it. This can be referred to as a **public interface**.
- Python allows for great latitude in specifications of an interface and Python traditionally treats abstractions implicitly using **duck typing** ("if it walks like a duck and quacks like a duck, then it's a duck"). Formally, Python supports abstract data types using **abstract base classes (ABC)**, which cannot be instantiated (you cannot directly create an instance of that class), but it defines one or more common methods that all implementations of the abstraction must have. An ABC is realized by one or more **concrete classes**, which inherit from the abstract base class, while providing implementations for the methods declared in the ABC. Python supports this through the `abc` module and there are some existing ABCs coming from Python's `collections` module.
##### Encapsulation
- Components of a software system should not reveal the internal details of their respective implementations. It gives a programmer freedom to implement details, without having to worry that others are writing code depending on those specific implementation details. Encapsulation allows for implementation details to change without adversely affecting other parts of the program, making it easier to add functionality or fix bugs. Python provides only loose support for encapsulation, the convention is for data members and member functions that are non-public to be named starting with a single underscore
#### Design patterns
- In order to write effective object-oriented code, you need to understand and effectively use object-oriented design techniques. A **design pattern** describes a "typical" software design problem and provides a general template solution. Design patterns tend to fall into two groups, patterns for solving algorithm design problems and patterns for solving software engineering problems
- Algorithm design patterns
  - Recursion
  - Amortization
  - Divide-and-conquer
  - Prune-and-search, also known as decrease-and-conquer
  - Brute force
  - Dynamic programming
  - The greedy method
- Software engineering design patterns
  - Iterator
  - Adapter
  - Position
  - Composition
  - Template method
  - Locator
  - Factory method