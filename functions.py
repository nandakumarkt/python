# def test(name):
#     print("hello", name)
# test("Nanda")
# test("Menaka")
# test("Prajay")
# test("Ridhamika")

# def test(name):
#     print(f"The name is {name}")  # format string
# test("Nanda")
# test("Menaka")
# test("Prajay")
# test("Ridhamika")


# def sum(a,b):
#     c=a+b
#     print("sum=", c)
# sum(1,2)


# def sum(a,b):
#     return a+b
# print(sum(1,2))

#Meaning Full Error#
# try:
#     def sum(a,b):
#         return a+b
#     print(sum(10))
# except Exception as err:
#     print(err)

#### WHY FUNCTION WITH PRINT IS NOT USEFUL################################
# def sum(a,b): #This line defines a function named sum that takes two arguments, a and b.
#     c=a+b #Inside the function, it calculates the sum of a and b and stores the result in a local variable c
#     print("First Function Sum is",c) #This line prints the string "First Function Sum is " followed by the value of c to the console.
# #Key point: This function performs an action (printing) but does not explicitly return any value. In Python, if a function doesn't have a return statement, it implicitly returns None
# def display(c): #This line defines a function named display that takes one argument, c.
#     print(c) #Inside the function, it prints the value of its argument c to the console.
# #Key point: Similar to the sum function, display also performs an action (printing) but does not explicitly return any value. It also implicitly returns None
# d=sum(2,3)
# #Inside sum, c becomes 2 + 3 = 5
# #Since sum doesn't have a return statement, it implicitly returns None. Therefore, the variable d is assigned the value None
# print("Second Function Sum is", display(d))
# #The display function is called with d, which is currently None
# #Now, the outer print statement evaluates to print("Second Function Sum", None)

###############WHY RETURN IS IMPORTANT FOR FUNCTION#######################################

# def sum(a,b):
#     return a+b
# def display(c):
#     return c
# d=sum(3,2)
# print("Second Function Sum is", display(d))

########################################################################################
# def sum_numbers(a, b):
#     """Calculates the sum of two numbers."""
#     return a + b
#
# def subtract_numbers(a, b):
#     """Calculates the difference between two numbers."""
#     return a - b
#
# def display_result(operation_name, result):
#     """
#     Displays the result of an operation with its given name.
#     """
#     print(f"The result of {operation_name} is: {result}")
#
# # Using display_result for the sum operation
# sum_outcome = sum_numbers(10, 5)
# display_result("Sum", sum_outcome) # Calls display_result with the name "Sum"
#
# # Using display_result for the subtract operation
# subtract_outcome = subtract_numbers(10, 5)
# display_result("Subtraction", subtract_outcome) # Calls display_result with the name "Subtraction"

#################################################
# def even_odd(num):
#     if num%2==0:
#         return "even"
#     else:
#         return "odd"
# num=int(input("Enter a number, we can find odd or even:\n"))
# result=even_odd(num)
# print(num, 'is', result)
####################################################
##This program takes a number as input and tells you if it's positive, negative, or zero.
# def type(num):
#     if num==0:
#         return "Number is Zero"
#     elif num>0:
#         return "Number is Positive"
#     elif num<0:
#         return "Number is Negative"
#     else:
#         None
# try:
#     num = int(input("Enter a number, we can find zero or negative or positive:\n"))
#     result = type(num)
#     print(num, 'is', result)
# except ValueError:
#     print("Invalid Number")

#####################################################################
####Grade Calculator: This program takes a student's score as input and returns their corresponding letter grade (e.g., A, B, C, D, F). You'll need to define your own grading scale.
# def gradecalc(grade):
#     if grade>=90:
#         return "A"
#     elif grade>=70:
#         return "B"
#     elif grade>=50:
#         return "C"
#     elif grade<50:
#         return "D"
#     else:
#         None
# i=0
# while i<3:
#     try:
#         grade=int(input("What is your score? \n"))
#         result=gradecalc(grade)
#         print("Your grade is", result)
#     except ValueError:
#         print("Incorect Input")
#     i=i+1
#############################################################################

# def is_even(num):
#     return num%2==0
# def square(num):
#     return num**2
# def cube(num):
#     return num**3
#
# try:
#     result=int(input("Input the number: "))
#     if is_even(result):
#         print(f"{result} is even")
#     else:
#         print(f"{result} is even")
#     print(f"The square of {result} is {square(result)} and the Cube of {result} is {cube(result)}")
# except ValueError:
#     print("Incorect Input")

######################################################################################
##################Different ways to find Length##########
##################Repeated For Loop######################
# name="Nandakumar"
# print(len(name))
# print('#################')
# name="Prajay"
# length=0
# for n in name:
#     length+=1
# print(length)
# print('#################')
# name="Ridhamika"
# length=0
# for n in name:
#     length+=1
# print(length)
##########simple code to find length using Function##########
def find_length(name):
    length=0
    for n in name:
        length+=1
    return length
print(find_length("Nandakumar"))
print(find_length("Menaka"))
print(find_length("Prajay"))
print(find_length("Ridhamika"))
#############################################################





