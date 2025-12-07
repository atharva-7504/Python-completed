#Write a program to print sum of all numbers between 1 and n using recursive and non recursive fn.


#non-recursive fn for addition from 1 to n
def non_recursive_addition(num: int)->int:
    sum = 0
    for counter in range(1, num+1):
        sum += counter
    return sum 


#recursive fn for addition from 1 to n
sum = 0
def recursive_addition(num: int)->int:
    if num != 0:
        return num + recursive_addition(num-1)
    return
    

if __name__ == "__main__":
    while True:
        num = input("Enter a natural number: ")
        temp = num
        if num[0] in ['-']:
            print("Invalid number.")
            continue
        if num[0] in ['+']:
            temp = num[1::]
        temp = temp.strip()
        if not temp.isdigit():
            print("Invalid number.")
        else:
            num = int(num)
            break

print(f"The sum of all numbers from 1 to {num} is {non_recursive_addition(num)}")