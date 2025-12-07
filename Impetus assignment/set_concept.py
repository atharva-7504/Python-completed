# creating a set 

# s1 = {}
# print(type(s1)) #create an empty dict

# #to create empty set 
# s2 = set()
# print(type(s2))

# sets = set("Atharva")
# print(sets)

# s3 = {1,2,"hi",3.2,(2+8j)}
# print(s3)

# s4 = {1,2,(3,4)}
# print(s4)

# s4 = {1,2,(3,4),[1,2]} # it contains only immutable elements.
# print(s4)

# lst = [2,3,5,7,9,0]
# s5 = set(lst)
# print(s5)

# myset = {43,5,4,3,2,9}
# s7 = set(myset)
# print(s7)


# s8 = {1,4,6,8,9}
# s8.add(2)
# print(s8)

# lst = [3,5,7,0]
# s8.update(lst)
# print(s8)

# s8.discard(1)
# print(s8)
# (len(s8))
# s8.discard(44)
# print(len(s8))

# s8.clear()
# print(s8)

# lst = []
# lst.pop()  # Index Error 

# set1 = set()
# set1.pop()   #Key Error


# s1 = {10,6,9}
# s2 = {1,9,2,6}
# s3 = s1.difference(s2)
# print(f"{s1} - {s2} = {s1 - s2}")
# print(f"{s2} - {s1} = {s2 - s1}")
# print("s1.union(s2) =",s3)
# print("s1.intersection(s2) =",s3)
# s3 = s1 | s2
# print(s3)


odd = set([1,3,5,7,9,11])
prime = set([2,3,5,7,11])


# Union - All elements are taken removing duplicate ones 
print(odd | prime)    
print(odd.union(prime))

# Intersection - All common elements are taken from two  sets 
print(odd & prime)
print(odd.intersection(prime))


# Difference - It gives difference of two sets
print(odd - prime )
print(odd.difference(prime))

# Exclusive (set symmetric difference) - Finds elements that are in either of sets but not both
print(odd^prime)
print(odd.symmetric_difference(prime))
