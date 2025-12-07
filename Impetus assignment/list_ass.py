#write a program to remove duplicates from a list .(using set and without set)

# input_list = [1,2,3,4,5,4,3,6,5,4,6,7,9,7,9,1]
# print("List containing duplicate values : ",input_list)
# input_list = set(input_list)
# print("List after removing duplicate values using set: ",input_list)

# print("Converting set into list.")
# input_list = list(input_list)
# print(input_list)

# list1 = []
# for value in input_list:
#     if value not in list1:
#         list1.append(value)
# print("Without using set, List is :",list1)

#----------------------------------------------------------------------------
# Write a program to append a list to another list using (built in and without using buil in function)

# l = [1,2,3,4,5]
# print("List1 :",l)
# l1 = [6,7,8,9,10]
# print("List2 :",l1)
# add1 = l + l1
# print("Appending list without using built in function :",add1)
# add2 = l.extend(l1)
# print("Appending using built in function :",add2)

#-----------------------------------------------------------------------------------------------------------
# Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given list of strings.
# Example : MyList = [&#39;pune&#39;, &#39;ana&#39;, &#39;Indira&#39;, &#39;an&#39;, &#39;mama&#39;, &#39;12321&#39;, &#39;educate&#39; ]
# Expected Output : 3 

# list1 = ["pune","ana","mama","an","Indira","12321","educate"]
# count = 0
# for i in list1:
#     if len(i) >= 2 and  i[0] == i[-1]:
#             count = count + 1
# print(count)

#--------------------------------------------------------------------------
# Program to find the smallest and largest among the three no in list . 
# input is taken from user in list.

# num1 = int(input("Enter the first number:"))
# num2 = int(input("Enter the second number:"))
# num3 = int(input("Enter the third number:"))

# storage_list =  []
# storage_list.append(num1)
# storage_list.append(num2)
# storage_list.append(num3)

# print("The Smallest number amongst 3 number is:",(min(storage_list)))
# print("The Largest number amongst 3 number is:",(max(storage_list)))

#----------------------------------------------------------------------------

# Write a progam to find second largest number in the list.

# mylist = [3,7,4,6,9,1,9,9]
# mylist1 = set(mylist)
# print(mylist1)
# print("Second Largest =",mylist1[-2])
#----------------------------------------------------------------------------

# Write a Python program to check whether a list contains a sub-list.
# Example : MyList = [7, &quot;ICCS&quot;, 555, 6.7, [11,22,33], &quot;Pune&quot;]
# Expected Output : The given list contains sub-list at the index 4

# mylist=[7,"Iccs",55,6.7,[1,2,3,4],1,22,33,"Pune"]
# for i in mylist:
#       if type(i) == list:
#           print(f"SUBSTRING found at index no : {mylist.index(i)}")
#           break
# else:
#       print("No substrings present")
         



# s1 = [1,2,3,4,5,6,7,8,9]
# print("BEFORE :",s1)
# s1[0],s1[-1] = s1[-1],s1[0]
# print("AFTER :",s1)

#--------------------------------------------------------------------------
# Program to get Data items from a list Appearing odd number of Times.

# a = [1,2,3,4,5,1,3,3,4]
# b =[]
# for i in a :
#     if a.count(i)%2==1 and i not in b:
#         b.append(i)
# print(b)

# data = input("Enter a list:")
# print(data,type(data))

#---------------------------------------------------------------------------

# Taking input of list from user .

# input_list = []
# for i in range(1,6):
#       n = (input("Enter no:"))
#       input_list.append(n)
# print(type(input_list))
# print(input_list)

# l = eval(input("Enter the list : "))
# print(l)
# print(type(l))


#--------------------------------------------------------------------------------

# Write a Python program to find the list of words that are longer than N from
# a given list of words.
# Example : MyList = [Pune&quot;,&quot;Mumbai&quot;,&quot;Satara&quot;,&quot;Thane&quot;,&quot;Panvel&quot;]
# Accept value of N from the user. If N = 6, then expected output is
# Mumbai, Satara, Panvel.

# city = ["Pune","Mumbai","Thane","Panvel","Satara","Karad","Kolhapur"]
# n = int(input("Enter the value of n :"))
# for name in city:
#     if len(name) == n:
#         print(name)  
        


# ----------------------------------------------------------------------------------------------------------------

# Write a Python function that takes two lists and returns True if they have at
# least one common member.(Using SET and without using SET)
 
# list1 = eval(input("Enter the first list :"))
# list2 = eval(input("Enter the second list :"))
# flag = False
# for value in list1:
#     if value in list2:
#         print("True , common member is :",value)
#         flag = True
# if flag == False:
#     print("False, no common member . ")

# list1 = eval(input("Enter the first list :"))
# list2 = eval(input("Enter the second list :"))
# list3 = []
# for i in list1:
#     if i not in list2:
#         list3.append(i)
# print(list3)


#-----------------------------------------------------------------------------------------------------

# Write a python program to create a list of tupples with the first element as the number and 
# second elements as square of the number .


# l = []

# n = int(input("Enter the first element :"))
# t = ()
# for i in range(1,n+1):
#     t = (i,i**i)
#     l.append(t)
# print(l)

#-------------------------------------------------------------------------------------------------------
#Write a Python program to print 100 in last element of tupple in list .

# sample_list = [(10,20,40),(40,60,50),(970,80,100)]
# print("Old List: ",sample_list)
# l1 = []
# len(sample_list)
# for i in sample_list:
#     data = i[:-1] + (100,)
#     l1.append(data)
# print("New List : ",l1)

    
#Write a python program to insert an element before each element of a list .

sample_list = ["Red","Green","Black"]
print(sample_list)
for i in range(0,6,2):
    sample_list.insert(i,"C")
print(sample_list)