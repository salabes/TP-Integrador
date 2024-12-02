#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) != 3:
        print("Por favor, proporciona exactamente 2 argumentos.")
        sys.exit(1)

    # Los argumentos se pasan como cadenas, puedes convertirlos según sea necesario
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]

    prueba(arg1,arg2)


def prueba(setDatos,resultados):
    archivo = f'pruebas/{setDatos}'  
    monedas = leerMonedasDesdeArchivo(archivo)
    _,ganancia_sophia = buscarResultadosEsperados(setDatos,resultados)
    ganancia_recibida,ganancia_mateo= elegir_monedas(monedas)
    correcto = False

    if ganancia_recibida  > ganancia_mateo:
        correcto = True

    print(correcto)


def leerMonedasDesdeArchivo(archivo):
    with open(archivo, 'r') as file:
        file.readline()
        contenido = file.read().strip()
        monedas = list(map(int, contenido.split(';')))
    return monedas


def buscarResultadosEsperados(archivoABuscar,resultados):
    with open(f'pruebas/{resultados}', 'r') as file:
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

def elegir_monedas(monedas):
    sophia_puntuacion = 0
    mateo_puntuacion = 0

    primer_moneda = 0
    ultima_moneda = len(monedas)-1

    while primer_moneda <= ultima_moneda:
        #primero elije Sophia
        if monedas[primer_moneda] > monedas[ultima_moneda]:
            sophia_puntuacion += monedas[primer_moneda]
            primer_moneda += 1
        else:
            sophia_puntuacion += monedas[ultima_moneda]
            ultima_moneda -= 1

        #Elije sophia para mateo en caso de que siga habiendo monedas
        if primer_moneda <= ultima_moneda:
            if monedas[primer_moneda] < monedas[ultima_moneda]:
                mateo_puntuacion += monedas[primer_moneda]
                primer_moneda += 1
            else:
                mateo_puntuacion += monedas[ultima_moneda]
                ultima_moneda -= 1
            
    return sophia_puntuacion,mateo_puntuacion


main()