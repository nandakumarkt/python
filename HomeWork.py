#Number Comparison: Write a program that takes two numbers as input and prints out which one is larger, or if they are equal.
# number1=int(input("Enter the First Number: "))
# number2=int(input("Enter the Second Number: "))
# if number1>number2:
#     print(number1, "is greater than", number2)
# elif number2>number1:
#     print(number2, "is greater than", number1)
# elif number2==number1:
#     print("Both are Equal")
# else:
#     pass

#Vowel or Consonant: Write a program that takes a character as input and prints whether it's a vowel or a consonant.
# ch=input("Enter the vowel :")
# if ch in ['a','e','i','o','u']:
#     print("Yes, This is vowel!")
# else:
#     print("No, This is not vowel")

#Calculator: Write a simple calculator program that takes two numbers and an operator (+, -, *, /) as input and performs the corresponding operation.
# a=int(input("Input the First Number: "))
# b=int(input("Input the Second Number: "))
# c=int(input("Enter the number for Mathematics operation you want to do "
#             "1. Add "
#             "2. Subtract "
#             "3. Multiply "
#             "4. Division "
#             "5. Floor Division "
#             "6. Remainder "
#             "7. Exponentiation "
#             ))
# if c==1:
#     print("You Chose Addition, answer is:", a+b)
# elif c==2:
#     print("You Chose Substraction, answer is:", a-b)
# elif c==3:
#     print("You Chose Multiply, answer is:", a*b)
# elif c==4:
#     print("You Chose Division, answer is:", a/b)
# elif c==5:
#     print("You Chose Floor Division, answer is:", a//b)
# elif c==6:
#     print("You Chose Remainder, answer is:", a%b)
# elif c==7:
#     print("You Chose Exponentiation, answer is:", a**b)
# else:
#     pass
##############################################################################
a=int(input("Input the First Number: "))
b=int(input("Input the Second Number: "))

c=input("Enter the Mathematics operation (+, -, *, /) you want to do ")
if c=='+':
    print("You Chose Addition, answer is:", a+b)
elif c=='-':
    print("You Chose Substraction, answer is:", a-b)
elif c=='*':
    print("You Chose Multiply, answer is:", a*b)
elif c=='/':
    print("You Chose Division, answer is:", a/b)
else:
    pass