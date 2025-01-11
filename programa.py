#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) != 2:
        print("Por favor, proporciona exactamente 2 argumentos.")
        sys.exit(1)

    # Los argumentos se pasan como cadenas, puedes convertirlos según sea necesario
    arg1 = sys.argv[1]

    prueba(arg1)


def prueba(setDatos):
    archivo = f'pruebas/{setDatos}'  
    monedas = leerMonedasDesdeArchivo(archivo)
    ganancia_recibida,ganancia_mateo, pasos= elegir_monedas(monedas)

    print("ganancia sophia: ")
    print(ganancia_recibida)
    print("Pasos:")
    print(pasos)


def leerMonedasDesdeArchivo(archivo):
    with open(archivo, 'r') as file:
        file.readline()
        contenido = file.read().strip()
        monedas = list(map(int, contenido.split(';')))
    return monedas

def elegir_monedas(monedas):
    sophia_puntuacion = 0
    mateo_puntuacion = 0
    pasos = []

    primer_moneda = 0
    ultima_moneda = len(monedas)-1

    while primer_moneda <= ultima_moneda:
        #primero elije Sophia
        if monedas[primer_moneda] > monedas[ultima_moneda]:
            sophia_puntuacion += monedas[primer_moneda]
            primer_moneda += 1
            pasos.append(" Primera moneda para Sophia")
        else:
            sophia_puntuacion += monedas[ultima_moneda]
            ultima_moneda -= 1
            pasos.append(" Última moneda para Sophia")

        #Elije sophia para mateo en caso de que siga habiendo monedas
        if primer_moneda <= ultima_moneda:
            if monedas[primer_moneda] < monedas[ultima_moneda]:
                mateo_puntuacion += monedas[primer_moneda]
                primer_moneda += 1
                pasos.append(" Primera moneda para Mateo")
            else:
                mateo_puntuacion += monedas[ultima_moneda]
                ultima_moneda -= 1
                pasos.append(" Última moneda para Mateo")
            
    return sophia_puntuacion,mateo_puntuacion,pasos


main()
