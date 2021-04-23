class Student:
      def __init__(self, name, roll_no):
            self.name = name
            self.roll_no = roll_no


student = Student('Amit', 8)

print(f"Name: {getattr(student, 'name')}")
print(f"Roll No: {getattr(student, 'roll_no')}")

