year = int(input("Enter a number : "))

if(year % 4 == 0  and year % 100 != 0) or year % 400 == 0:
    print(year,"is a leap year")
else:
     print(year,"is not a leap year")


'''
o/p : 

Enter a number : 2000
2000 is a leap year

Enter a number : 1997
1997 is not a leap year
'''     