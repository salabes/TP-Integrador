#!/usr/bin/env python3

from parte1 import elegir_monedas
import sys
import time
import matplotlib.pyplot as plt
import numpy as np


def main():
    tiempos = []
    tamanos = [100, 1000, 10000, 20000]

    # Llamamos a las funciones de prueba y almacenamos los tiempos
    prueba1()
    prueba2()
    prueba3()
    prueba4()
    prueba5()
    pruebaCatedra()
    pruebaCatedra2()
    pruebaCatedra3()

    # Medir el tiempo de las pruebas Cátedra
    tiempo1 = pruebaCatedra4()
    tiempo2 = pruebaCatedra5()
    tiempo3 = pruebaCatedra6()
    tiempo4 = pruebaCatedra7()
    tiempos.append(tiempo1)
    tiempos.append(tiempo2)
    tiempos.append(tiempo3)
    tiempos.append(tiempo4)


    # Realizar el ajuste lineal
    coeficientes = np.polyfit(tamanos, tiempos, 1)

    # Los coeficientes son la pendiente (m) y la intersección (b)
    pendiente = coeficientes[0]
    interseccion = coeficientes[1]

    print(f"Pendiente del ajuste lineal: {pendiente}")

    # Graficar los tiempos de ejecución vs tamaño de entrada
    plt.figure(figsize=(10, 6))
    plt.plot(tamanos, tiempos, 'o-', label="Tiempos Medidos")
    plt.xlabel("Tamaño de Entrada")
    plt.ylabel("Tiempo de Ejecución (segundos)")
    plt.title("Correlación entre Tamaño de Entrada y Tiempo de Ejecución")
    plt.grid(True)

    # Ajuste lineal con la técnica de cuadrados mínimos (modelo O(n))
    ajuste = np.polyval(coeficientes, tamanos)  # Aplicar el modelo a los tamaños

    # Graficar el ajuste
    plt.plot(tamanos, ajuste, 'r--', label="Ajuste Lineal (O(n))")
    plt.legend()
    plt.show()

    # Calcular el error absoluto entre los tiempos observados y los tiempos predichos
    error_abs = np.abs(np.array(tiempos) - ajuste)

    # Graficar el error absoluto
    plt.figure(figsize=(10, 6))
    plt.plot(tamanos, error_abs, 'o-', label="Error Absoluto")
    plt.xlabel("Tamaño de Entrada")
    plt.ylabel("Error Absoluto (segundos)")
    plt.title("Error Absoluto vs Tamaño de Entrada")
    plt.grid(True)
    plt.show()

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
    archivo = 'pruebas/20.txt'  
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
    archivo = 'pruebas/25.txt'  
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
    archivo = 'pruebas/50.txt'  
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
    archivo = 'pruebas/100.txt'  
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
    archivo = 'pruebas/1000.txt'  
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
    archivo = 'pruebas/10000.txt'  
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
    archivo = 'pruebas/20000.txt'  
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
    with open('pruebas/ResultadosEsperados.txt', 'r') as file:
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