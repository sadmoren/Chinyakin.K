


#девятая
num = int(input("Введите число больше 200 "))
if num > 200:
    for i in range(200, num + 1):
        if i % 7 == 0:
            print(i)
            break
else:
    print("Введите число больше 200")


#десятая
num = int(input())
if num % num == 1 and num > 600:
    for i in range(600, num + 1):
        if i % 28 == 0:
print(i)

#одиннадцатая
kilometr = 10
day = 0
while kilometr < 20:
    kilometr += kilometr * 0.1
    day += 1
print(day)

#двенадцатая
num = int(input())
y = 0
for i in range(1, num + 1):
    
#тринадцатая
num = int(input())
count = 0
total = 1
for _ in range(num + 1):
    count += total
    total *= -1/2
print(count)
    
#четырнадцатая
num = int(input())
if num < 100:
    for i in range(1, num + 1):
        if i % 11 == 0:
            print(i)
            i += 1
    
S, a = int(input()), int(input())
P = a / S
print(P)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    