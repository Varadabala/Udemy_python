n = int(input("Enter a number : "))
count = 0

while n!= 0:
    count += 1
    n = n // 10

print("Number of digits =",count)    

"""
o/p:

Enter a number : 123456
Number of digits = 6
"""