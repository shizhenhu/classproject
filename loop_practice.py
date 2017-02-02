numbers = [1, 3, 5, 7, 9, 11, 13, 14]
even = []
odd = []
while len(numbers) > 0:
    number = numbers.pop()
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
print(even)
print(odd)


while False:  # 该条件永远为true，循环将无限执行下去
    num = input("Enter a number  :")
    num = int(num)
    if num == 88:
       break
    else:
        print ("You entered: ", num)

i = 1
while i < 10:
    i += 1
    if i % 2 > 0:     # 非双数时跳过输出
        pass
    else:
        print (i)

i = 1
while i < 10:
    i += 1
    if i % 2 > 0:     # 非双数时跳过输出
        continue
    print (i)


n = input('input a number')
n = int(n)
if n > 1 and n % 1 == 0:
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            print("%d = %i"%(n,i),end="")
            m = n // i
            j = 2
            while j <= m:
                if m % j == 0:
                    print("*%d"%j,end="")
                    m = m // j
                    j = 2
                else:
                    j += 1
            break
    else:
        print("%d is a prime number"%n,end="")
else:
    print("error",end="")
    print()

