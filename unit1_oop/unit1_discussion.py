"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    organization = "University System"

    def __init__(self, name: str, member_id: str):
        self.name = name
        self.member_id = member_id

    def get_details(self) -> str:
        return f"Name: {self.name}, ID: {self.member_id}, Organization: {self.organization}"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    program_type = "Undergraduate"

    def __init__(self, name: str, member_id: str, major: str, courses: list = None):
        super().__init__(name, member_id)
        self.major = major
        # Mutable nested list used to demonstrate copying behavior
        self.courses = courses if courses is not None else []

    def enroll_course(self, course_name: str):
        self.courses.append(course_name)

    # Extension method (Requirement 6 from README)
    def calculate_workload(self) -> int:
        """Calculates estimated weekly study hours based on enrolled courses."""
        return len(self.courses) * 3

    def get_details(self) -> str:
        """Overrides parent method to append program, major and course details."""
        base_details = super().get_details()
        return f"{base_details}, Program: {self.program_type}, Major: {self.major}, Courses: {self.courses}"


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    # Create two child objects
    student1 = ChildClass("Alex", "S101", "Computer Science", ["CMSC 315"])
    student2 = ChildClass("Jordan", "S102", "Cybersecurity", ["SIFS 201"])

    # Access class variable through class itself and through an object instance
    print(f"Class variable accessed via Class: {ChildClass.program_type}")
    print(f"Class variable accessed via Object (student1): {student1.program_type}")

    # Dynamically add an attribute to student1 only
    student1.honors_status = True

    # Display instance namespaces
    print("\nStudent 1 Instance Namespace (__dict__):")
    print(student1.__dict__)

    print("\nStudent 2 Instance Namespace (__dict__):")
    print(student2.__dict__)

    # Display class namespace keys
    print("\nChildClass Class Namespace (__dict__ keys):")
    print([key for key in ChildClass.__dict__.keys() if not key.startswith("__")])


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    # Object containing nested mutable list data
    original_student = ChildClass("Taylor", "S103", "Data Science", ["CMSC 315", ["Module 1", "Module 2"]])

    # Perform shallow copy and deep copy
    shallow_student = copy(original_student)
    deep_student = deepcopy(original_student)

    # Modify the original object's nested list at index 1
    original_student.courses[1].append("Module 3")

    # Output results
    print(f"Original Object Courses: {original_student.courses}")
    print(f"Shallow Copy Courses:   {shallow_student.courses}")
    print(f"Deep Copy Courses:      {deep_student.courses}")

    """
    EXPLANATION OF DIFFERENCE:
    - Shallow Copy (copy()): Creates a new outer object, but copies references to any
      nested mutable objects inside. Therefore, altering the nested inner list
      modifies both the original object and the shallow copy.

    - Deep Copy (deepcopy()): Recursively creates a completely independent clone of
      the object and all nested items inside it. Modifying nested data in the original
      has no impact on the deep copy.
    """


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n--- Parent Class Object ---")
    parent_obj = ParentClass("Morgan", "P500")
    print(parent_obj.get_details())

    print("\n--- Child Class Object ---")
    child_obj = ChildClass("Sam", "S200", "Software Engineering", ["CMSC 210", "MATH 140"])
    child_obj.enroll_course("CMSC 315")

    # Demonstrating inherited/overridden methods and extension method
    print(child_obj.get_details())
    print(f"Estimated Weekly Workload: {child_obj.calculate_workload()} hours")

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()