n = int(input("Enter a number : "))
digit1 = n % 10
digit2 = n //10
result = (digit1 + digit2) + (digit1 * digit2)

print("Special" if result == n else "NOt Special") 


"""
o/p : 

n = 29
d1 = 29 % 10 = 9
d2 = 29 // 10 = 2
result = (9+2)+(9*2) = 29
 special

"""