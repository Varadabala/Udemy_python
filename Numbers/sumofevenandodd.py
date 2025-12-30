num=int(input("Enter any number"))

sumofeven=0
sumofodd=0
while num!=0:
    digit=num%10
    if digit %2==0:
        sumofeven=sumofeven+digit
    else:
        sumofodd=sumofodd+digit
    num=num//10

print("Sum of Even Numbers is ",sumofeven)
print("Sum of Odd Numbers is ",sumofodd)


"""
o/p:
Enter any number1234567
Sum of Even Numbers is  12
Sum of Odd Numbers is  16
"""