class employee():
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary

    def show(self):
        print("name:",self.name)
        print("id:",self.id)
        print("salary:",self.salary)


e1=employee("prathmesh",89,50000)
e1.show()











class Employee:
    company_name = "TCS"   # Class attribute

    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print("Company:", Employee.company_name)
        print("Name:", self.name)
        print("ID:", self.emp_id)
        print("Salary:", self.salary)
        print("----------------------")

# Creating 4 objects
e1 = Employee("Amit", 101, 30000)
e2 = Employee("Rahul", 102, 35000)
e3 = Employee("Sneha", 103, 40000)
e4 = Employee("Pooja", 104, 45000)

# Display info
e1.display()
e2.display()
e3.display()
e4.display()
