num = int(input("Enter a Number : "))
reverse_num = 0
while num!= 0:
    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    num = num // 10

print("Reversed Number is ",reverse_num)    


"""
o/p:

Enter a Number : 2345543
Reversed Number is  3455432
"""

#reverse a number - single line

print(input("Enter a Number : ")[::-1])