
# Creating a class
class Demo:

    # Class Variable (common for all objects)
    college_name = "DY Patil College"

    # Constructor (used to initialize instance variables)
    def __init__(self, name, roll):
        # Instance Variables (different for each object)
        self.name = name
        self.roll = roll

    # Instance Method
    def show_details(self):
        print("\n--- Instance Method ---")
        print("Student Name:", self.name)
        print("Roll No:", self.roll)
        print("College:", Demo.college_name)

    # Class Method
    @classmethod
    def change_college(cls, new_name):
        print("\n--- Class Method ---")
        cls.college_name = new_name
        print("College name changed to:", cls.college_name)

    # Static Method
    @staticmethod
    def general_info():
        print("\n--- Static Method ---")
        print("This is a static method.")
        print("It does not use instance or class variables.")


# Main Program

# Creating objects
s1 = Demo("Prathmesh", 1)
s2 = Demo("Rahul", 2)

# Calling instance method
# s1.show_details()
# s2.show_details()

# Calling class method (changes class variable)
Demo.change_college("MIT College")

# Checking updated value
s1.show_details()
s2.show_details()

# Calling static method
# Demo.general_info()
print(Demo.college_name)