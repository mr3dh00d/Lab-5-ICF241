def Menu():
    print("*************************************************************************************************")
    print("       .____          ___.                        __               .__          .________ ")
    print("       |    |   _____ \_ |__   ________________ _/  |_  ___________|__| ____    |   ____/ ")
    print("       |    |   \__  \ | __ \ /  _ \_  __ \__  \\\   __\/  _ \_  __ \  |/  _ \   |____  \ ")
    print("       |    |___ / __ \| \_\ (  <_> )  | \// __ \|  | (  <_> )  | \/  (  <_> )  /       \ ")
    print("       |_______ (____  /___  /\____/|__|  (____  /__|  \____/|__|  |__|\____/  /______  / ")
    print("               \/    \/    \/                  \/                                     \/  ")
    print("*************************************************************************************************")
    print("Elige cuidadosamente que figura quieres que construya el programa:\n")
    print("\t1.Cuadrado")
    print("\t2.Trianguilo")
    print("\t3.S\n")

def matrizPrint(m):
    print()
    for row in m:
        for col in row:
            print(col, end='')
        print()
    print()

def Canva():
    return list(map(lambda x: ['']*43, range(16)))

def Opciones():
    return [1, 2, 3, 11]