# Write a Python Script to add a key to a dictionary.


# k = int(input("Enter key :"))
# v = int(input("Enter value : "))

# sample_dict = {0:10,1:20}
# print(sample_dict)
# sample_dict[2] = 30
# print(sample_dict)

# sample_dict[k] = v
# pair = (k,v)
# sample_dict.update(pair)
# print(sample_dict)

# Write a program to concatenate following dictionaries into new one .

# d1 = {1:10,2:20}
# d2 = {3:30,4:40}
# d3 = {5:50,6:60}

# d = {}
# d.update(d1)
# d.update(d2)
# d.update(d3)
# print(d)

# list1 = [d1,d2,d3]
# for i in list1:
#     d.update(i)
# print(d)

# d = {**d1, **d2, **d3}
# print(d)

# Write a Program that inverts a dictionary. That is it makes key of dict as value and value as key .

# original = {"roll": 101,"name" : "Atharva","Per" :9.27}
# new = {}

# for k,v in original.items():
#     new[v] = k
# print("OLD : ",original)
# print("NEW : ",new)

# s = input("Enter any string ")
# d = {}
# for i in s:
#     if i not in d:
#          d[i] = s.count(i)
# print(d)


Eng_Hindi = {"Father" : "Pitaji",
             "Mother" : "Mataji"} 
Hindi_Marathi = {"Pitaji":"Baba",
                 "Mataji" :"Aai"}
word = input("Enter a word: ")
eh = Eng_Hindi[word]
hm = Hindi_Marathi[eh]
print("Word        Hindi          Marathi")
print("==================================")
print(word ,eh ,hm ,)


num1 = eval(input("Enter any number :"))

for i in num1:
    digit = num[i]
