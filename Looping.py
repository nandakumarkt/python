#While Loop
# i=-0
# while i<3:
#     print(i)
#     i=i+1

#while i < 4:: This is the start of a while loop. The code inside this loop will keep running as long as the condition i < 4 is true. This means the loop will execute four times (when i is 0, 1, 2, and 3).
# i=0
# while i<4:
#     num=int(input("Enter the number: "))
#     if num==0:
#         print("Number is Zero")
#     elif num>0:
#         print("Positive Number")
#     else:
#         print("Negative Number")
#     i=i+1
###############################################
# n=int(input("How may times: "))
# i=0
# while i<n:
#     num=int(input("Enter the number: "))
#     i=i+1
###############################################
# i=100
# while i>=100 and i<=110:
#     print(i)
#     i=i+2
##############################################
# i=100
# while i>=100 and i<=110:
#     print(i, end=' ')   #Horizontal printing
#     i=i+2
###################FOR#######################
# name='python'
# for t in name:
#     print(t)
#This (for t in name:) is a for loop. When used with a string, a for loop iterates over each character in the string, one by one
#print(t): Inside the loop, this line prints the current character stored in t.
#Because print() by default adds a new line character at the end, each character will appear on its own line.
#############################################
# fruits_list=["apple", "banana", 'grapes']
# for fu in fruits_list:
#     print(fu)
##############################################
# for i in range(5):
#     print(i)
###########################################
# for i in range(4,8):
#     print(i)
#########PYTHON DEBUGGER#############
# num_list=[10,20,30,40]
# sum=0
# for num in num_list:
#     import pdb;  #import debugger
#     pdb.set_trace() #using debugger
#     sum=sum+num
# print(sum)
#######Continue and Break###############
# name="python"
# for n in name:
#     print(n)
#     if n=='y':
#         continue
#     elif n=='o':
#         break
##############Nested Loop###################
# list1=[10,20,30]
# list2=[1,2,3]
# for i in list1:
#     for j in list2:
#         print(i+j)
#########################################
fruits_list=["apple", "banana", 'grapes']
for fu in fruits_list:
    print()
    print(fu)
    for f in fu:
        print(f, end=' ')
########################################


