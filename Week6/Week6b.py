class Person:

  def __init__(self, first, last): # Constructor
    self.first = first
    self.last = last

  def full_name(self): # Method to return full name
    return f"{self.first} {self.last}"
  
  def __str__(self): # String representation
    return self.full_name()
  

per1 = Person("John", "Smith")
print(per1.full_name())
print(per1) # Calls __str__ method


