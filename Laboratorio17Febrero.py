import matplotlib.pyplot as plt
import numpy as np
with open("resultadosAltura.txt") as data:
    mins, proms, maxs = [], [], [] # instanciar los arreglos que vamos a graficar

    for line in data: # leer y limpiar la data
        arreglo = line.split(',')
        arreglo.pop(len(arreglo)-1)
        mins.append(float(arreglo[0]))
        proms.append(float(arreglo[1]))
        maxs.append(float(arreglo[2]))


    print(mins)
    print(proms)
    print(maxs)

    n = [50, 100, 500, 1000, 2000, 5000]
    nn = np.array(n)
    nproms= np.array(proms)
    nmins = np.array(mins)
    nmaxs = np.array(maxs)
    plt.plot(nn, nproms, marker='*', color = 'purple')
    plt.plot(nn, nmins, color = 'red', linestyle= '--')
    plt.plot(nn, nmaxs, color='blue', linestyle='--')
    plt.fill_between(nn, nproms, nmaxs, where= (nmaxs > nproms), interpolate = True, alpha = .25)
    plt.fill_between(nn, nproms, nmins, where=(nmins < nproms), interpolate=True, alpha=.25)

    plt.title("Plotting trees height behaviour")
    plt.xlabel("n")
    plt.ylabel("tree height")
    lista = ["promedios", "minimos", "maximos"]
    plt.legend(lista)
    '''
    plt.plot(n, proms, marker='*', color = 'purple')
    plt.fill_between(x=n, y1=mins, y2=maxs, alpha=.5, linewidth=0)
    plt.title("Plotting trees height behaviour")
    plt.xlabel("n")
    plt.ylabel("tree height")
    '''

    plt.show()






