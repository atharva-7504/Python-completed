# File Handling: 1)Textual 2)Binary
# Modes : "wt" or "w" write - where t is default 
#           "r" -Read (default file opening mode)
#           "a" - Append (at last of the cotents)
#           "x" - 

# open("Filepath","modes",encoding="UTF-8")             
# In windows encoding not specified by default cp1252         #utf-8/16(unicode text formating)


f = open(r"D:\File Handling\abc.txt","w",encoding = "utf-8")     #Any such a operation on a file which involves writing the contents onto a file ,
                                                                 #then in such a scenario,if the file is not available on the gives path, then it will
f.tell()                                                         #be created by the operating System with the same name and same extension .
data = f.read()
print(data)
print(f.tell())
print(f.seek(0))
print(f.read(4))  
print(f.readline())   
print(f.readline())
print(f.readline())
data = f.readlines()
print(data)
print(len(data))
print(f.tell()) 
f.close()                                                             #"w" mode When the file is opened in "w" mode, then it will erase all the existing contents of the file
                                                                      # and allow us to add fresh data onto a file.
# f.write("Impetus !")                                                                
# print(f.mode)
# print(f.encoding)
# print(f.closed)
# print(f.name)
# print(f.writable())
# print(f.readable())
# print(f.fileno())
# print(f.close())

