# allowed_country=['India', 'Canada', 'USA']
# country=input("Enter the Country Name: ")
# if country in allowed_country:
#     print("Country Mentioned is Available")
# else:
#     print("Country Mentioned not Available")
# from importlib.metadata import pass_none

#Oneway################################
num=eval(input("Enter the Number :"))
if num==1:
    print("Yes This is a number")
#
# str='Nanda'
# if str=='Nanda':
#     print("Yes This is String")

# str=input("Enter the String :")
# if str=='Nanda':
#     print("Yes This is String")

#Two way##############################
# num=eval(input("Enter the Number One :"))
# if num==1:
#     print("Yes - This is a Valid number")
# else:
#     print("No - This is not a Valid number")

# num=int(input("Enter The Number, we can find ODD or EVEN: "))
# if num%2==0:    # % - Reminder after Divide
#     print("This is a EVEN Number")
# else:
#     print("This is a ODD Number")

#Multi Branching##############################
# num=int(input("Enter The Number: "))
# if num>0:
#     print(num, "is greater than zero")
# elif num<0:
#     print(num, "is smaller than zero")
# elif num==0:
#     print(num, "is zero")
# else:
#     pass    #Nothing Happens

#Error Handling#################################
# try:
#     num = int(input("Enter The Number: "))
#     if num > 0:
#         print(num, "is greater than zero")
#     elif num < 0:
#         print(num, "is smaller than zero")
#     elif num == 0:
#         print(num, "is zero")
#     else:
#         pass  # Nothing Happens
# except:
#     print("Enter a valid number")

#Nested IF#######################################
# name='python'
# if 'o' in name:
#     if 'th' in name:
#         if 'p' in name:
#             print("Correct")
# else:
#     print("Incorrect")

#Nested IF third condition not satisfied
# name='python'
# if 'o' in name:
#     if 'th' in name:
#         if 'z' in name:
#             print("Correct")
#         else:
#             print("Third condition not satisfied")
# else:
#     print("Incorrect")

#Another way
# name = 'python'
# if any(sub in name for sub in ['y', 'th', 'p']):
#     print("Correct")
# else:
#     print("Incorrect")