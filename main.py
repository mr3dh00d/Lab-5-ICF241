from helpers import Menu
from multiprocessing import Process, Pipe

def matrizPrint(m):
    for row in m:
        for col in row:
            print(col, end='')
        print()

def cuadrado_1(p, c):
    canva = c.recv()
    for col in range(len(canva[0])):
        canva[0][col] = '*'
        canva[-1][col] = '*'
    for row in range(1, 15):
        for col in range(0, 6):
            inv = (col+1)*-1
            canva[row][col] = '*'
            canva[row][inv] = '*'
    matrizPrint(canva)
    p.send(canva)

def cuadrado_2(p, c):
    canva = c.recv()
    for row in [1, -2]:
        for col in range(6, 38):
            if col in [6, 37]:
                canva[row][col] = '+'
            else:
                canva[row][col] = '-'
    for row in range(2, 14):
        canva[row][6] = '|'
        canva[row][-7] = '|'
    matrizPrint(canva)
    p.send(canva)

def cuadrado_3(p, c):
    canva = c.recv()
    for row in range(len(canva)):
        for col in range(len(canva[0])):
            if canva[row][col]  == '':
                canva[row][col] = ' '
    matrizPrint(canva)

def main():
    Menu()
    opcion = input("Ingrese una opcion: ")
    print()
    parent, child = Pipe()
    process = []
    canva = list(map(lambda x: ['']*44, range(16)))
    parent.send(canva)
    process.append(Process(target=cuadrado_1, args=([parent, child])))
    process.append(Process(target=cuadrado_2, args=([parent, child])))
    process.append(Process(target=cuadrado_3, args=([parent, child])))
    [p.start() for p in process]
    [print('proceso '+str(n)+': '+str(process[n].pid)) for n in range(len(process))]
    [p.join() for p in process]




if __name__ == "__main__":
    main()