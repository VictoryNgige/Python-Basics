#Built-in Function/Standard Library Functions
x = max(67, 89, 90, 90, 17, 23, 45)
print("The Maximum Number is", x)

y = min(67, 89, 90, 90, 17, 23, 45)
print("The Minimum Number is", y)

z = pow(2,3)
print("The Power of 2 is", z)

#User Defined Function
def greeting():
    print("Hello World!")
greeting() #Calling a Function

def school():
    print("My coding school is eMobilis")
school()

#Parameter and Argument
def add(num1, num2):
    print(num1 + num2)
add(5, 10)
add(10, 20)

def student(FullName, Course, Gender):
    print(FullName, Course, Gender)
student("Mary Sayyid", "MIT", "Female")
student("James Kamau", "MIT", "Male")
student("Sera Msoni", "MIT", "Female")

#A Python Program that Displays Details at FinTech using Parameter and Argument
# (FullName, Email, Age, Position, Salary, Marriage Status)

def employees(FullName, Email, Age, Position, Salary, MarriageStatus):
    print(FullName, Email, Age, Position, Salary, MarriageStatus)
employees("Pierina Wangui", "pierinawangui1@gmail.com", 30, "FinTech CEO", 500000, "Engaged")
employees("Simon Samuel", "simonsamuel2@gmail.com", 35, "Deputy CEO", 450000, "Married")
employees("Abigael Samoei", "abigaelsamoei3@gmail.com", 25, "Secretary", 50000, "Single")
employees("Andrew Aiden", "andrewaiden4@gmail.com", 28, "Treasurer", 400000, "Married")
employees("Alyshia Makena", "alyshiamakena5@gmail.com", 23, "Personal Assistant", 300000, "Single")















