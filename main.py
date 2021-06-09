from helpers import Menu, matrizPrint, Canva, Opciones, Secret
from multiprocessing import Process, Pipe, Queue
from datetime import datetime
from time import sleep

def cuadrado_1(p):
    print('Dibujando Fondo...', end='')
    startTime = datetime.now()
    canva = Canva()
    for col in range(len(canva[0])):
        canva[0][col] = '*'
        canva[-1][col] = '*'
    for row in range(1, 15):
        for col in range(0, 6):
            inv = (col+1)*-1
            canva[row][col] = '*'
            canva[row][inv] = '*'
    endTime = (datetime.now()-startTime).microseconds
    print('Dibujado  '+str(endTime)+' microseg')
    p.send(canva)

def cuadrado_2(p):
    print('Dibujando Borde...', end='')
    startTime = datetime.now()
    canva = Canva()
    for row in [1, -2]:
        for col in range(6, 37):
            if col in [6, 36]:
                canva[row][col] = '+'
            else:
                canva[row][col] = '-'
    for row in range(2, 14):
        canva[row][6] = '|'
        canva[row][-7] = '|'
    endTime = (datetime.now()-startTime).microseconds
    print('Dibujado  '+str(endTime)+' microseg')
    p.send(canva)

def cuadrado_3(p):
    print('Dibujando Relleno...', end='')
    startTime = datetime.now()
    canva = Canva()
    for row in range(2, 14):
        for col in range(7, 36):
            canva[row][col] = ' '
    endTime = (datetime.now()-startTime).microseconds
    print('Dibujado  '+str(endTime)+' microseg')
    p.send(canva)


def triangulo_1(p):
    print('Dibujando Fondo...', end='')
    startTime = datetime.now()
    canva = Canva()
    for col in range(len(canva[0])):
        canva[0][col] = '*'
        canva[-1][col] = '*'
    colums = 21
    for row in range(1,15):
        for col in range(colums):
            inv = -(col+1)
            canva[row][col] = '*'
            canva[row][inv] = '*'
        if colums > 9:
            colums-=1
    endTime = (datetime.now()-startTime).microseconds
    print('Dibujado  '+str(endTime)+' microseg')
    p.send(canva)

def triangulo_2(p):
    print('Dibujando Borde...', end='')
    startTime = datetime.now()
    canva = Canva()
    col = 21
    for row in range(1, 14):
        canva[row][col] = '/' 
        canva[row][-col] = '\\'
        col-=1
    for col in range(9, 35):
        canva[14][col] = '-'
    endTime = (datetime.now()-startTime).microseconds
    print('Dibujado  '+str(endTime)+' microseg')
    p.send(canva)

def triangulo_3(p):
    print('Dibujando Relleno...', end='')
    startTime = datetime.now()
    canva = Canva()
    start = 21
    colums = start+2
    for row in range(2, 14):
        for col in range(start, colums):
            canva[row][col] = ' '
        start-=1
        colums+=1
    endTime = (datetime.now()-startTime).microseconds
    print('Dibujado  '+str(endTime)+' microseg')
    p.send(canva)

def S_1(q):
    print('Dibujando Fondo...', end='')
    startTime = datetime.now()
    canva = Canva()
    for col in range(len(canva[0])):
        canva[0][col] = '*'
        canva[-1][col] = '*'
    for row in range(1, 15):
        for col in range(12):
            canva[row][col] = '*'
            canva[row][-(col+1)] = '*'
    for row in [5, 10]:
        if row == 5:
            start = 18
            columns = start+13
        else:
            start = 12
            columns = start+13
        for col in range(start, columns):
            canva[row][col] = '*'
    endTime = (datetime.now()-startTime).microseconds
    print('Dibujado  '+str(endTime)+' microseg')
    q.put(canva)

def S_2(q):
    print('Dibujando Borde...', end='')
    startTime = datetime.now()
    canva = Canva()
    for row in [1, 4, 6, 9, 11, 14]:
        if row in [1, 14]:
            start = 11
            columns = start+21
        elif row in [4, 6]:
            start = 17
            columns = start+15
        else:
            start = 11
            columns = start+15
        for col in range(start, columns):
            if col in [start, columns-1]:
                canva[row][col] = '+'
            else:
                canva[row][col] = '-'
    for col in [11, 17, 25, 31]:
        excpt = []
        if col == 11:
            start = 2
            end = 14
            excpt = [9, 10, 11]
        elif col == 17:
            start = 5
            end = 6
        elif col == 25:
            start = 10
            end = 11
        else:
            start = 2
            end = 14
            excpt = [4, 5, 6]
        for row in range(start, end):
            if row not in excpt:
                canva[row][col] = '|'
    endTime = (datetime.now()-startTime).microseconds
    print('Dibujado  '+str(endTime)+' microseg')
    q.put(canva)

def S_3(q):
    print('Dibujando Relleno...', end='')
    startTime = datetime.now()
    canva = Canva()
    for row in [2, 3, 7, 8, 12, 13]:
        for col in range(12, 31):
            canva[row][col] = ' '
    for row in [4, 5, 6, 9, 10, 11]:
        if row in [4, 5, 6]:
            start = 12
        else:
            start = 26
        for col in range(start, start+5):
            canva[row][col] = ' '
    endTime = (datetime.now()-startTime).microseconds
    print('Dibujado  '+str(endTime)+' microseg')
    q.put(canva)

def main():
    Menu()
    while(True):
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion not in Opciones():
                raise Exception
            else:
                break
        except:
            print("¡Error! Ingresa una opcion valida") 

    print()
    parent, child = Pipe()
    queue = Queue()
    process = []
    canva = Canva()

    if opcion == 1:
        process.append(Process(target=cuadrado_1, args=([parent])))
        process.append(Process(target=cuadrado_2, args=([parent])))
        process.append(Process(target=cuadrado_3, args=([parent])))
    elif opcion == 2:
        process.append(Process(target=triangulo_1, args=([parent])))
        process.append(Process(target=triangulo_2, args=([parent])))
        process.append(Process(target=triangulo_3, args=([parent])))
    elif opcion == 3:
        process.append(Process(target=S_1, args=([queue])))
        process.append(Process(target=S_2, args=([queue])))
        process.append(Process(target=S_3, args=([queue])))
    else:
        Secret()
        main()
    if len(process) > 0:
        for n in range(len(process)):
            process[n].start()  
            print('Proceso '+str(n+1)+': '+str(process[n].pid))
            process[n].join()
            sleep(0.1)
        if opcion in [1, 2]:
            canvas = [child.recv() for canva in range(3)]
        else:
            canvas = [queue.get() for canva in range(3)]
        for canv in canvas:
            for row in range(len(canv)):
                for col in range(len(canv[0])):
                    if canv[row][col] != '':
                        canva[row][col] = canv[row][col]
        matrizPrint(canva)


if __name__ == "__main__":
    main()