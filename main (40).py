life = 3
def zadachi():

    a = input()
    if a == "висит":
        b = input()
        while b != "груша":
            if life != 0:
                life -= 1
                print("у вас осталось", life)
                b = input()
            else:
                print("закончились попытки")
                break
    a = input()
    if a == "река":
        b = input()
        while b != "сухой":
            if life != 0:
                life -= 1
                print("у вас осталось", life)
                b = input()
            else:
                print("закончились попытки")
                break
    a = input()
    if a == "застежки":           
        b = input()
        while b != "лук":
            if life != 0:
                life -= 1
                print("у вас осталось", life)
                b = input()
            else:
                print("закончились попытки")
                break
            
            
zadachi()








































