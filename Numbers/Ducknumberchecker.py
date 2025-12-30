num = int(input("Enter a Number : "))
is_duck_number = False
while num!= 0:
    digit = num % 10
    if digit == 0:
        is_duck_number = True
        break
    num = num //10

if is_duck_number:
    print("Duck Number")
else:
    print("Not a Duck Number")    


"""
o/p: 
Enter a Number : 1230987
Duck Number

Enter a Number : 987
Not a Duck Number
"""  
#one line program to find a duck number
print("\nDuck Number" if "0" in input("Enter a number : ")  else "Not a Duck number")