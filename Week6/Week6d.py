class Person:

  def __init__(self, first, last): # Constructor
    self.first = first
    self.last = last

  @property
  def full_name(self): # Method to return full name
    return f"{self.first} {self.last}"
  
  def __str__(self): # String representation
    return self.full_name


class Student(Person):
  def __init__(self, first, last, gpa):
    super().__init__(first, last)
    self.gpa = gpa

  def __str__(self):
    return f"Student is {super().__str__()} with GPA {self.gpa}" # Calls __str__ method of Person class



per1 = Student("John", "Smith", 3.5)
print(per1.full_name)
print(per1) # Calls __str__ method


