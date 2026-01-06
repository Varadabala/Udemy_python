#Reverse a string 

#1st method
s = input("Enter a string : ")

empty = " "

for i in s:
    empty = i + empty

print(empty) 

#2nd method

T = input("Enter a string : ")
print(T[::-1])

#3rd method
arr = list(map(int, input("Enter elements: ").split()))

start = 0
end = len(arr) - 1

while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1

print(arr)
