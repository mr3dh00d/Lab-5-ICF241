from helpers import Menu, matrizPrint, Canvas, Opciones, Secret
from multiprocessing import Process, Pipe, Queue
from datetime import datetime
from time import sleep

def cuadrado_1(p):
    print('Dibujando Fondo...', end='')
    startTime = datetime.now()
    canvas= Canvas()
    for col in range(len(canvas[0])):
        canvas[0][col] = '*'
        canvas[-1][col] = '*'
    for row in range(1, 15):
        for col in range(0, 6):
            inv = (col+1)*-1
            canvas[row][col] = '*'
            canvas[row][inv] = '*'
    endTime = (datetime.now()-startTime).microseconds
    print('Dibujado  '+str(endTime)+' microseg')
    p.send(canvas)

def cuadrado_2(p):
    print('Dibujando Borde...', end='')
    startTime = datetime.now()
    canvas= Canvas()
    for row in [1, -2]:
        for col in range(6, 37):
            if col in [6, 36]:
                canvas[row][col] = '+'
            else:
                canvas[row][col] = '-'
    for row in range(2, 14):
        canvas[row][6] = '|'
        canvas[row][-7] = '|'
    endTime = (datetime.now()-startTime).microseconds
    print('Dibujado  '+str(endTime)+' microseg')
    p.send(canvas)

def cuadrado_3(p):
    print('Dibujando Relleno...', end='')
    startTime = datetime.now()
    canvas= Canvas()
    for row in range(2, 14):
        for col in range(7, 36):
            canvas[row][col] = ' '
    endTime = (datetime.now()-startTime).microseconds
    print('Dibujado  '+str(endTime)+' microseg')
    p.send(canvas)


def triangulo_1(p):
    print('Dibujando Fondo...', end='')
    startTime = datetime.now()
    canvas= Canvas()
    for col in range(len(canvas[0])):
        canvas[0][col] = '*'
        canvas[-1][col] = '*'
    colums = 21
    for row in range(1,15):
        for col in range(colums):
            inv = -(col+1)
            canvas[row][col] = '*'
            canvas[row][inv] = '*'
        if colums > 9:
            colums-=1
    endTime = (datetime.now()-startTime).microseconds
    print('Dibujado  '+str(endTime)+' microseg')
    p.send(canvas)

def triangulo_2(p):
    print('Dibujando Borde...', end='')
    startTime = datetime.now()
    canvas= Canvas()
    col = 21
    for row in range(1, 14):
        canvas[row][col] = '/' 
        canvas[row][-col] = '\\'
        col-=1
    for col in range(9, 35):
        canvas[14][col] = '-'
    endTime = (datetime.now()-startTime).microseconds
    print('Dibujado  '+str(endTime)+' microseg')
    p.send(canvas)

def triangulo_3(p):
    print('Dibujando Relleno...', end='')
    startTime = datetime.now()
    canvas= Canvas()
    start = 21
    colums = start+2
    for row in range(2, 14):
        for col in range(start, colums):
            canvas[row][col] = ' '
        start-=1
        colums+=1
    endTime = (datetime.now()-startTime).microseconds
    print('Dibujado  '+str(endTime)+' microseg')
    p.send(canvas)

def S_1(q):
    print('Dibujando Fondo...', end='')
    startTime = datetime.now()
    canvas= Canvas()
    for col in range(len(canvas[0])):
        canvas[0][col] = '*'
        canvas[-1][col] = '*'
    for row in range(1, 15):
        for col in range(12):
            canvas[row][col] = '*'
            canvas[row][-(col+1)] = '*'
    for row in [5, 10]:
        if row == 5:
            start = 18
            columns = start+13
        else:
            start = 12
            columns = start+13
        for col in range(start, columns):
            canvas[row][col] = '*'
    endTime = (datetime.now()-startTime).microseconds
    print('Dibujado  '+str(endTime)+' microseg')
    q.put(canvas)

def S_2(q):
    print('Dibujando Borde...', end='')
    startTime = datetime.now()
    canvas= Canvas()
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
                canvas[row][col] = '+'
            else:
                canvas[row][col] = '-'
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
                canvas[row][col] = '|'
    endTime = (datetime.now()-startTime).microseconds
    print('Dibujado  '+str(endTime)+' microseg')
    q.put(canvas)

def S_3(q):
    print('Dibujando Relleno...', end='')
    startTime = datetime.now()
    canvas= Canvas()
    for row in [2, 3, 7, 8, 12, 13]:
        for col in range(12, 31):
            canvas[row][col] = ' '
    for row in [4, 5, 6, 9, 10, 11]:
        if row in [4, 5, 6]:
            start = 12
        else:
            start = 26
        for col in range(start, start+5):
            canvas[row][col] = ' '
    endTime = (datetime.now()-startTime).microseconds
    print('Dibujado  '+str(endTime)+' microseg')
    q.put(canvas)

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
    canvas= Canvas()
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
            canvases = [child.recv() for canvas in range(len(process))]
        else:
            canvases = [queue.get() for canvas in range(len(process))]
        for canv in canvases:
            for row in range(len(canv)):
                for col in range(len(canv[0])):
                    if canv[row][col] != '':
                        canvas[row][col] = canv[row][col]
        matrizPrint(canvas)


if __name__ == "__main__":
    main()