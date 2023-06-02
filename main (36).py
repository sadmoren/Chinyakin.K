day= int(input())
mes = int(input())
god = int(input())
mesa = [1, 3, 5, 7, 8, 10, 12]
def chislo(a, b, c):
    if 1<=a<=31 and 1<=b<=12 and 1<=c:
        if c%4==0  and c%400==0:
            if b == 2:
                if a == 29:
                    print('True')
        elif b in mesa and 1<=a<=31:
                print('true')
        else: 
            print('true')
    else: 
        print('Ошибка')
        
chislo(day, mes, god)