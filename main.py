from helpers import Menu, matrizPrint, Canva, Opciones
from multiprocessing import Process, Pipe
import datetime
from time import sleep

def cuadrado_1(p):
    print('Dibujando Fondo...', end='')
    canva = Canva()
    for col in range(len(canva[0])):
        canva[0][col] = '*'
        canva[-1][col] = '*'
    for row in range(1, 15):
        for col in range(0, 6):
            inv = (col+1)*-1
            canva[row][col] = '*'
            canva[row][inv] = '*'
    print('Dibujado ')
    p.send(canva)

def cuadrado_2(p):
    print('Dibujando Borde...', end='')
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
    print('Dibujado ')
    p.send(canva)

def cuadrado_3(p):
    print('Dibujando Relleno...', end='')
    canva = Canva()
    for row in range(2, 14):
        for col in range(7, 36):
            canva[row][col] = ' '
    print('Dibujado ')
    p.send(canva)


def triangulo_1(p):
    print('Dibujando Fondo...', end='')
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
    print('Dibujado ')
    p.send(canva)

def triangulo_2(p):
    print('Dibujando Borde...', end='')
    canva = Canva()
    col = 21
    for row in range(1, 14):
        canva[row][col] = '/' 
        canva[row][-col] = '\\'
        col-=1
    for col in range(9, 35):
        canva[14][col] = '-'
    print('Dibujado ')
    p.send(canva)

def triangulo_3(p):
    print('Dibujando Relleno...', end='')
    canva = Canva()
    start = 21
    colums = start+2
    for row in range(2, 14):
        for col in range(start, colums):
            canva[row][col] = ' '
        start-=1
        colums+=1
    print('Dibujado ')
    p.send(canva)


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
    
    for n in range(len(process)):
        process[n].start()  
        print('Proceso '+str(n+1)+': '+str(process[n].pid))
        process[n].join()
        sleep(0.1)
    for n in range(3):
        canv = child.recv()
        for row in range(len(canv)):
            for col in range(len(canv[0])):
                if canv[row][col] != '':
                    canva[row][col] = canv[row][col]
    matrizPrint(canva)


if __name__ == "__main__":
    main()