n = int(input("Enter a number : "))
result = 0
temp = n

while n != 0:
    digit = n % 10
    result = result + digit
    n = n // 10

print("Niven" if temp % result == 0 else "Not Niven")    