from helpers import Menu, matrizPrint
from multiprocessing import Process, Pipe
import datetime
from time import sleep

def cuadrado_1(p):
    print('Dibujando Fondo...', end='')
    canva = list(map(lambda x: ['']*44, range(16)))
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
    canva = list(map(lambda x: ['']*44, range(16)))
    for row in [1, -2]:
        for col in range(6, 38):
            if col in [6, 37]:
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
    canva = list(map(lambda x: ['']*44, range(16)))
    for row in range(2, 14):
        for col in range(7, 37):
            canva[row][col] = ' '
    print('Dibujado ')
    p.send(canva)

def main():
    Menu()
    opcion = input("Ingrese una opcion: ")
    print()
    parent, child = Pipe()
    process = []
    canva = list(map(lambda x: ['']*44, range(16)))
    process.append(Process(target=cuadrado_1, args=([parent])))
    process.append(Process(target=cuadrado_2, args=([parent])))
    process.append(Process(target=cuadrado_3, args=([parent])))
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