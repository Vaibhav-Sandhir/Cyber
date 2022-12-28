numbers = [16,9,3,15,3,20,6,20,8,5,14,21,13,2,5,18,19,13,1,19,15,14]
flag = ""
n = len(numbers)

for x in range(0,n):
        numbers[x] = numbers[x] + 96
        flag = flag + chr(numbers[x])
        

print(flag)        