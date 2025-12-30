def fibanocci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibanocci(n-1) + fibanocci(n-2)

n = int(input("Enter a number : "))
for i in range(0,n):
    print(fibanocci(i),end = " ")

