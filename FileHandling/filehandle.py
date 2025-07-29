# file=open('output.txt', 'r')
# content=file.read()
# print(content)
# file.close()


# file=open('output.txt', 'r')
# content=file.readline()
# print(content)
# file.close()


#In a file content take line of servers, change it list, put in the for loop, we make use of readlines, rstrip can remove /n
#Homework

# file=open('output.txt', 'r')
# content=file.readlines()
# print(content)
# file.close()


# file=open('output.txt', 'r')
# content=file.readlines()
# print(content)
# file=open('output.txt','w')
# file.write("I am writing in the file, thanks, this will remove existing values in the file")

# file=open('output.txt', 'r')
# content=file.readlines()
# print(content)
# print('#########################################')
# file=open('output.txt','a')
# file.write("\nI am updating the file, thanks,")
# print(content)
# file.close()

# file=open('output.txt','a')
# file.write("\nNew Line 1 ")
# file.write("\nNew Line 2 ")
# file.write("\nNew Line 3 ")
# file.close()

########No need to Close the file while using 'with'#####################
# with open('output.txt', 'r') as file:
#     content=file.read()
#     print(content)


########Replace##########################################################
# with open('output.txt', 'r') as file:
#     content=file.read()
# modified_content=content.replace('Menaka', 'Nanda')
#
# with open('output.txt', 'w') as file:
#     file.write(modified_content)
# #####################Replace First One##################################
# with open('output.txt', 'r') as file:
#     content=file.read()
# modified_content=content.replace('thanks', 'regards',1)
#
# with open('output.txt', 'w') as file:
#     file.write(modified_content)
######################Replace in a Line (line index)################################
# with open('output.txt', 'r') as file:
#     lines=file.readlines()
# lines[11]=lines[11].replace('thanks', 'regards') #Line 12
#
# with open('output.txt', 'w') as file:
#     file.writelines(lines)
#####################Delete Lines##############################
def delete_lines(file_path, start_line, end_line):
    with open(file_path, 'r') as file:
        lines=file.readlines()
    del lines[start_line-1:end_line]

    with open(file_path,'w') as file:
        file.writelines(lines)
delete_lines('output.txt',3,5)

