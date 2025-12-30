n = int(input("Enter a number : "))

if n<=0:
    print(n,"is invalid")
else:
    if(n % 2 == 0):
        print(n,"is Even Number")
    else:
        print(n,"is Odd Number")  