# #Sum of n natural nos
# num1 = int(input("Enter a number :"))
# sum = 0
# if num1 > 0 :
#     print(f"{num1} is a natural no .")
# elif num1 < 0:
#     print(f"{num1} is a negative number.")
#     print("Please Enter natural no .")
# else:
#     print(f"{num1} is a zero . Not a natural number .")
#     print("Enter the required natural number .")
# for i in range (1,num1+1):
#     sum  = sum + i
# print(sum)

# s = "Python"
# print(s)
# print(s[::2])
# print(s[0:4:2])
# print(s[::-1])
# print(s[3:])


# def print_info(**general):
#     for key,values in general.items():
#         print(f"{key} : {values}")
# print_info(name = "Atharva", age = 18, city ="Pune")
with open("source.txt", "r") as src, open("destination.txt", "w") as dst:
    while True:
        char = src.read(1)
        if not char:
            break
        if char == '.':
            dst.write(',')
        elif char.islower():
            dst.write(char.upper())
        elif char.isupper():
            dst.write(char.lower())
        else:
            dst.write(char)
print("Content copied with modifications.")