'''
Terms

Class,
Class Variables.
Data Member,
Instance Variable,
Inheritance,
Instance,
Initiation,
Method,
Object,
Operator overloading

'''


class Person:
    def __init__(self,gender,name):
        self.gender = gender
        self.name = name
    def display(self):
        print("Your a ", self.gender ,", and your name is ", self.name)


people = Person('Male',"alex")

people.display()

class Employee:
    'Common base class for all Employees'
    empCount = 0 # Shared amoung all Instances of this class

    '''
    __init__() is a special methid which is called class constrcutor
    or initialization method that python call when you creat a new instance of this calss
    '''
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount +=1

    def displayCount(self):
        print("total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount



class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "vector(%d, %d)" % (self.a,self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)

print v1 + v2


'''
Data Hiding
'''

class JustCounter:
    __secertCount = 0

    def count(self):
        self.__secertCount += 1
        print(self.__secertCount)


counter = JustCounter()
counter.count()
counter.count()
print(counter.__secertCount)
