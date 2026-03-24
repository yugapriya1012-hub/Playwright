file= open("test.txt")
# print(file.read()) #what is read it a function when we use it
# file.seek(0)

# for line in file.readlines():
#     print(line)

# line = file.readline()
# while line!= "":
#     print(line.strip()) # strips na new line na remove panno
#     line=file.readline()

# file.close()

#read the file and stored all the lines in list
#reverse the list
#write the list back to the file


with open('test.txt','r') as reader:
    content =reader.readlines()
    reversed(content)
    with open('test.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)


