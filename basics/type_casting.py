# Typecasting
# It allows to turn a variable of certain type to a different type and this can be done explicitly or implicitly
# For example, changing from string to int to be able to do arithmetic

# Important to note that user's input from terminal is always a string

name = "Goofy"
age = 38
gpa = 3.1
is_student = True

# To know the data types of variables we can use
print("\nThe types are:", type(name), type(age), type(gpa), type(is_student), sep="  ")

# In case I needed to explicitly convert gpa to int I can achieve that as follows
# To explicitly convert to another type we can --> type casting( variable )
gpa = int(gpa)
print(f"The new gpa is: {gpa}, the decimal value was removed")
print(type( gpa ))

is_student = str(is_student)
print("New type of student is:", type(is_student))

# Implicit type casting occurs when a value is converted to a different type automatically
x = 3
y = 2.5
result = x + y
print(f"The result of operation is: {result} and it's type is {type(result)}")