def perfect(num):
    sum = 0
    for i in range(1,num):
        if num % i == 0:
            sum = sum + i
    return sum == num

num = int(input("Enter a number : "))
print("Perfect" if perfect(num) else "Not a perfect number")        