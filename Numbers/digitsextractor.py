num = int(input("Enter a Number : "))

while num!= 0:
    digit = num % 10
    print(digit , end = " ")
    num = num //10
"""
o/p:

Enter a Number : 77265283
3 8 2 5 6 2 7 7 

num = int(input("Enter a Number : "))

rev = 0
temp = num

# Step 1: Reverse the number
while temp != 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

# Step 2: Print digits in correct order
while rev != 0:
    digit = rev % 10
    print(digit, end=" ")
    rev = rev // 10

"""    