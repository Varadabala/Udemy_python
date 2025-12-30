n = int(input("Enter a number : "))

a, b = 0,1
print(a,b,end = " ")
for i in range(2,n):
    c = a + b
    print(c,end = " ")
    a = b
    b = c

"""
o/p:
Enter a number : 5
0 1 1 2 3 

"""
