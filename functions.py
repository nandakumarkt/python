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
def even_odd(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
num=int(input("Enter a number, we can find odd or even: "))
result=even_odd(num)
print(num, 'is', result)
####################################################
