#!/usr/bin/python
'''
PYTHON FUNCTIONS
'''

#define the functions
def changeme(myList):
    myList.append([1,2,3,4])
    return myList

#Now you can call the function here
myList = [10,20,30]
changeme(myList)
print(myList)



## Keyword Arguments

def printme(str):
    print(str)
    return

printme(str = "Hi")


#Defining new function
def printinfo(name, age):
    print("Name: " + name)
    print("Age: " + str(age))
    return

#Now call the function printinfo
printinfo(age = 50, name = "miki")


'''
vartuple
'''
def func4(arg1, *vartuple):
    print("Output is: ")
    print arg1
    for var in vartuple:
        print var
    return

func4(10)
func4(70,60,50)

print("\n")

'''
Lamda Functions
'''

sum = lambda arg1, arg2: arg1 + arg2

print(sum(10,20))
print(sum(20,40))


'''
Global vs. Local variables
'''

total = 0

def adds(arg1, arg2):
    total = arg1 + arg2
    print(total)
    return total

adds(10,30)
print(total)
