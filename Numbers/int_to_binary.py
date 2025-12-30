num = int(input("Enter a number : "))
binary_num = []
while num != 0:
    binary_num.append(num % 2)
    num = num // 2

binary_num.reverse()
print(binary_num)    

for i in range(len(binary_num)):
    print(binary_num[i],end = " ")