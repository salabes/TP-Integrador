from parte1 import elegir_monedas
import time
import matplotlib.pyplot as plt
import numpy as np


def main():
    tiempos = []
    tamanos = [100,1000,10000,20000]
    prueba1()
    prueba2()
    prueba3()
    prueba4()
    prueba5()
    pruebaCatedra()
    pruebaCatedra2()
    pruebaCatedra3()
    tiempo1 = pruebaCatedra4()
    tiempo2 = pruebaCatedra5()
    tiempo3 = pruebaCatedra6()
    tiempo4 = pruebaCatedra7()
    tiempos.append(tiempo1)
    tiempos.append(tiempo2)
    tiempos.append(tiempo3)
    tiempos.append(tiempo4)
    # Datos empíricos (tamaños de entrada y resultados de tiempos)
    x = np.array(tamanos)  # Tamaños de entrada
    results = {}  # Tiempos de ejecución

    # Definición de la función de ajuste lineal
    f = lambda x, c1, c2: c1 * x + c2



def prueba1():
    print("Caso Alta Variabilidad")
    print("Monedas = [1, 100, 2, 99]")
    print("Esperado: ")
    print("Sophia: 199, Mateo: 3")
    print("Obtenido: ")
    monedas = [1, 100, 2, 99]
    sophia,_ = elegir_monedas(monedas)
    print(f"Sophia: {sophia}")
    print()

def prueba2():
    print("Caso Ordenado")
    print("Monedas = [10, 11, 12, 13]")
    print("Esperado: ")
    print("Sophia: 25, Mateo: 21")
    print("Obtenido: ")
    monedas = [10, 11, 12, 13]
    sophia,_ = elegir_monedas(monedas)
    print(f"Sophia: {sophia}")
    print()

def prueba3():
    print("Caso con Monedas Iguales")
    print("Monedas = [5, 5, 5, 5]")
    print("Esperado: ")
    print("Sophia: 10, Mateo: 10")
    print("Obtenido: ")
    monedas = [5, 5, 5, 5]
    sophia,_ = elegir_monedas(monedas)
    print(f"Sophia: {sophia}")
    print()

def prueba4():
    print("Caso con Variabilidad Moderada")
    print("Monedas = [7, 1, 8, 10, 4, 3]")
    print("Esperado: ")
    print("Sophia: 25, Mateo: 8")
    print("Obtenido: ")
    monedas = [7, 1, 8, 10, 4, 3]
    sophia,_ = elegir_monedas(monedas)
    print(f"Sophia: {sophia}")
    print()

def prueba5():
    print("Caso con Monedas Grande")
    print("Monedas = [20, 50, 30, 40, 60, 10]")
    print("Esperado: ")
    print("Sophia: 130, Mateo: 80")
    print("Obtenido: ")
    monedas = [20, 50, 30, 40, 60, 10]
    sophia,_ = elegir_monedas(monedas)
    print(f"Sophia: {sophia}")
    print()

def pruebaCatedra():
    print("Prueba catedra: 1")
    archivo = 'pruebas/TP1/20.txt'  
    monedas = leerMonedasDesdeArchivo(archivo)
    pasos,ganancia_sophia = buscarResultadosEsperados('20.txt')
    ganancia_recibida,pasos_recibidos = elegir_monedas(monedas)
    correcto = False
    for i in range(len(pasos)):
        if pasos[i] != pasos_recibidos[i]:
            correcto = False
        else :
            correcto = True

    if int(ganancia_sophia) != int(ganancia_recibida):
        correcto = False

    print(correcto)

def pruebaCatedra2():
    print("Prueba catedra: 2")
    archivo = 'pruebas/TP1/25.txt'  
    monedas = leerMonedasDesdeArchivo(archivo)
    pasos,ganancia_sophia = buscarResultadosEsperados('25.txt')
    ganancia_recibida,pasos_recibidos = elegir_monedas(monedas)
    correcto = False
    for i in range(len(pasos)):
        if pasos[i] != pasos_recibidos[i]:
            correcto = False
        else :
            correcto = True

    if int(ganancia_sophia) != int(ganancia_recibida):
        correcto = False
    print(correcto)

def pruebaCatedra3():
    print("Prueba catedra: 3")
    archivo = 'pruebas/TP1/50.txt'  
    monedas = leerMonedasDesdeArchivo(archivo)
    pasos,ganancia_sophia = buscarResultadosEsperados('50.txt')
    ganancia_recibida,pasos_recibidos = elegir_monedas(monedas)
    correcto = False
    for i in range(len(pasos)):
        if pasos[i] != pasos_recibidos[i]:
            correcto = False
        else :
            correcto = True

    if int(ganancia_sophia) != int(ganancia_recibida):
        correcto = False
    
    print(correcto)

def pruebaCatedra4():
    print("Prueba catedra: 4")
    archivo = 'pruebas/TP1/100.txt'  
    monedas = leerMonedasDesdeArchivo(archivo)
    pasos,ganancia_sophia = buscarResultadosEsperados('100.txt')
    start = time.time()
    ganancia_recibida,pasos_recibidos = elegir_monedas(monedas)
    end = time.time()
    tiempo = end - start
    correcto = False
    for i in range(len(pasos)):
        if pasos[i] != pasos_recibidos[i]:
            correcto = False
        else :
            correcto = True

    if int(ganancia_sophia) != int(ganancia_recibida):
        correcto = False
    
    print(correcto)
    return tiempo

def pruebaCatedra5():
    print("Prueba catedra: 5")
    archivo = 'pruebas/TP1/1000.txt'  
    monedas = leerMonedasDesdeArchivo(archivo)
    pasos,ganancia_sophia = buscarResultadosEsperados('1000.txt')
    start = time.time()
    ganancia_recibida,pasos_recibidos = elegir_monedas(monedas)
    end = time.time()
    tiempo = end - start
    correcto = False
    for i in range(len(pasos)):
        if pasos[i] != pasos_recibidos[i]:
            correcto = False
        else :
            correcto = True

    if int(ganancia_sophia) != int(ganancia_recibida):
        correcto = False
    
    print(correcto)
    return tiempo

def pruebaCatedra6():
    print("Prueba catedra: 6")
    archivo = 'pruebas/TP1/10000.txt'  
    monedas = leerMonedasDesdeArchivo(archivo)
    pasos,ganancia_sophia = buscarResultadosEsperados('10000.txt')
    start = time.time()
    ganancia_recibida,pasos_recibidos = elegir_monedas(monedas)
    end = time.time()
    tiempo = end - start
    correcto = False
    for i in range(len(pasos)):
        if pasos[i] != pasos_recibidos[i]:
            correcto = False
        else :
            correcto = True

    if int(ganancia_sophia) != int(ganancia_recibida):
        correcto = False
    
    print(correcto)
    return tiempo

def pruebaCatedra7():
    print("Prueba catedra: 7")
    archivo = 'pruebas/TP1/20000.txt'  
    monedas = leerMonedasDesdeArchivo(archivo)
    pasos,ganancia_sophia = buscarResultadosEsperados('20000.txt')
    start = time.time()
    ganancia_recibida,pasos_recibidos = elegir_monedas(monedas)
    end = time.time()
    tiempo = end - start
    correcto = False
    for i in range(len(pasos)):
        if pasos[i] != pasos_recibidos[i]:
            correcto = False
        else :
            correcto = True

    if int(ganancia_sophia) != int(ganancia_recibida):
        correcto = False
    
    print(correcto)
    return tiempo



def leerMonedasDesdeArchivo(archivo):
    with open(archivo, 'r') as file:
        file.readline()
        contenido = file.read().strip()
        monedas = list(map(int, contenido.split(';')))
    return monedas


def buscarResultadosEsperados(archivoABuscar):
    with open('pruebas/TP1/Resultados Esperados.txt', 'r') as file:
        lineas = file.readlines()
        ahora = False 
        monedas = []
        cont = 0
        for linea in lineas:
            linea = linea.strip()
            if ahora:
                if linea.startswith("Ganancia de Sophia:"):
                    ganancia_sophia = linea.split(":")[1].strip()
                    break 
                else:
                    monedas.extend(linea.split(';'))
                    if cont == 0:
                        monedas[0] = " " + monedas[0]
                        cont += 1
            if linea == archivoABuscar:
                ahora = True
                continue
    return monedas,ganancia_sophia


main()