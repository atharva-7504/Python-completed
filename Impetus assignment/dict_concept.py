# Dictionary :- 1) It is mutable
              # 2) It is a collection of key and value 
              # 3) It is ordered 
              # 4) Values can be Duplicate 
              # 5) Key must be Immutabe and unique

 # to create empty list :
    # 1) {}
    # 2) dict()


# Key can be repeated but latest value of key is Accepted and appear in previous position .

d2 = {101:"Atharva",102:"Apurva",103:"Om",104:"Prem",101:"Krishna"}
print(d2)

# Converting list into dict.
list_tuples = [(101,"Atharva"),(102,"Prachi")]
d3 = dict(list_tuples)
print(d3)

d4 = list(d3)
print(d4)

d5 = [[1,2],[2,4],{1:3},{"Atharva"},(12,3,4)]
print(d5)

# Accesing elements from Dict.
d2 = {101:"Atharva",102:"Apurva",103:"Om",104:"Prem",101:"Krishna"}
print(d2[103])
print(d2[101])

# Updating elements in dict.
d2[102] = "Parth"
print(d2)

# Creating new key value.
d2[105] = "Khatri"
print(d2)

s =  {1:"ABC",2.5:45,'name':"ABC",("Phy","Chem"): [81,65]}
print(s)
# s =  {1:"ABC",2.5:45,'name':"ABC",["Phy","Chem"]: [81,65]}
# print(s)
# s =  {1:"ABC",2.5:45,'name':"ABC", "marks": [81,65,90]}
# print(s["marks"][2])
# sum(s("marks"))



s = {
    "name":"Sachin",
    "spouce": "Anjali",
    "kids": ("Sara","Arjun"),
    "age":52,
    "city":"MUMBAI",
     }

print(f"{s["name"]} got maried to {s["spouce"]}")
print(f"{s["name"]} has 2 kids.")
print(f"{s['kids'][0]} is elder than {s['kids'][1]}")
print(f"{s["spouce"]} and {s["name"]} are blessed with 2 kids. ")
print(f"{s["age"]} years old {s["name"]} lives in {s["city"]}.")


s = {
    1:{"roll" : 101, "name" : "Sindhu"},
    2:{"roll" : 105, "name": "Saina" , "per" : 9.2},
    3:{"roll":109,"name":"Virat", "city": "MUMBAi"},
}

print(f"WELCOME TO IMPETUS {s[2]["name"]}.")
s[3]["city"] = "Pune"
print(F"Virat live in {s[3]["city"]}.")

d = {1:1,2:4,3:9}
print(d.get(2))
print(d.get(5))
print(list(d.keys()))
print(d.values())
print(d.items())
lst_tup = [{5,25},{6,36}]
print(d.update(lst_tup))
print(d.pop(2))
print(d.popitem())
print(d.pop(4,"This given key does not exist."))
print(d.pop(1,"This given key does not exist."))
print(d)



# Iterating over a dictionary.

d1 = {1:1,2:8,3:27}
mykeys = d1.keys()
for k in mykeys:
    print(k,d1[k]) 

data = d1.items()
for k,v in data:
    print(k,"==",v)




# Write a program to concatenate following dictionaries into new one .

d1 = {1:10,2:20}
d2 = {3:30,4:40}
d3 = {5:50,6:60}

d = {}
# d.update(d1)
# d.update(d2)
# d.update(d3)
# print(d)

list1 = [d1,d2,d3]
for i in list1:
    d.update(i)
print(d)

d = {**d1, **d2, **d3}
print(d)