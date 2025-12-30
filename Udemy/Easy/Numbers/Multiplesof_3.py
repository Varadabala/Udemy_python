n = int(input("Enter a number : "))
result = 0
while n!= 0:
    digit = n % 10
    if digit in (3,6,9):
        result = result + digit


    n = n //10

print("Sum of multiple of 3 is ",result)

"""
o/p:
Enter a number : 367189
Sum of multiple of 3 is  18
"""