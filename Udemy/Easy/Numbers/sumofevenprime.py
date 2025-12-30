n = int(input("Enter a number : "))
result = 0
while n!= 0:
    digit = n % 10
    if digit in (2,3,5,7):
        result = result + digit
    n = n //10

print("Sum of prime is ",result)    

"""
o/p:
Enter a number : 234567
Sum of prime is  17
"""