num = int(input("Enter a Number : "))
temp = num
reverse_num = 0
while num!= 0:
    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    num = num // 10

print("Reversed Number is ",reverse_num) 

if temp == reverse_num:
    print("Palindrome")
else:
    print("Not a palindrome")    

"""
o/p:
Enter a Number : 1234321 
Reversed Number is  1234321
Palindrome

Enter a Number : 123421
Reversed Number is  124321
Not a palindrome
"""
#one line to check a palindrome    
n = input("Enter a number :")
print("palindrome" if n == n[::-1] else "not a plaindrome")