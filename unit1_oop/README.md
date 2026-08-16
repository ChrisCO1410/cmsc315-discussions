# Unit 1 Discussion Implementation Documentation

## Overview
Implemented a parent-child class hierarchy in Python to demonstrate core object-oriented programming concepts including inheritance, method overriding, custom attributes and copying behaviors.

## Implementation Details
- Parent Class: Created `ParentClass` with class-level organizational variables, unique instance variables (`name`, `member_id`) and an information summary method.
- Child Class: Created `ChildClass` inheriting from `ParentClass`, using `super().__init__()` to maintain code reuse. Added student attributes, an overridden `get_details()` method and a custom `calculate_workload()` extension method.
- Namespaces: Used `__dict__` to inspect dynamic object modification and differentiate between shared class variables and instance attributes.
- Copying: Utilized Python's `copy` module to contrast shallow copy reference sharing against deep copy recursive duplication.

## Discussion Board Reflection

1. Concepts Learned: Deepened understanding of class inheritance, namespace attribute resolution and the operational differences between shallow and deep copying in Python.
2. Challenges Overcome: Managing shared mutable references inside objects required careful testing using `deepcopy()` to prevent unintended side effects across instances.
3. OOP vs. Procedural Programming: Procedural programming organizes code around sequential functions and logic, whereas OOP binds data and behaviors into self-contained objects. OOP provides far better modularity for scaling complex software.
4. Maintainability and Reusability: Designing modular classes reduces code duplication, simplifies debugging and allows future software expansions without disrupting foundational code.