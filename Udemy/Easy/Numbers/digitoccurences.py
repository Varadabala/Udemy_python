n = int(input("Enter a number : "))
digit_to_count = int(input("Enter a digit to count: "))
count = 0

while n!= 0:
    digit = n % 10
    if digit == digit_to_count:
        count += 1
    n = n // 10

print(f"Number of times a digit {digit_to_count} occured is",count)    


'''
o/p:

Enter a number : 13456543233433333
Enter a digit to count: 3
Number of times a digit 3 occured is 9
'''