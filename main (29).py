a = int(input())
b = int(input())
c = int(input())
summ = a + b 
if c == summ:
    print("Ответ верный")
else:
    print("Ответ неверный")


mil = int(input())
day = int(input())
summ = (mil%10) + (mil//100) + (mil%100//10)
if summ > day:
  print("Сброс")
  mil -= mil
  print(mil)
else:
  print("Сегодня не сломался")
  print(mil)


hr = float(input())
mn = float(input())
cr = float(input())
zp = (200*hr/(2**3))+num
need = mn + cr
if zp > need:
  print("Часов хватает, можно отдохнуть")
else:
  print("Нужно больше денег, пора работать!")

