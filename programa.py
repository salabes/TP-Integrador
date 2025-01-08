#!/usr/bin/env python3
import sys
import obtener_datos
import parte2


def main():
    if len(sys.argv) != 2:
        print("Por favor, proporciona exactamente 1 argumento.")
        sys.exit(1)

    # Los argumentos se pasan como cadenas, puedes convertirlos según sea necesario
    arg1 = sys.argv[1]

    prueba(arg1)
 

def prueba(setDatos):
    MONEDAS_1 = obtener_datos.obtener_monedas(setDatos)
    sophia_moneda, sophia_ganancia, mateo_monedas, mateo_ganancia = parte2.obtener_maxima_monedas(MONEDAS_1)

    print(f"Las moneds de sophia son: {sophia_moneda}")
    print(f"Ganancia obtenida de sophia es: {sophia_ganancia}")
    print(f"Las moneds de mateo son: {mateo_monedas}")
    print(f"Ganancia obtenida de mateo es: {mateo_ganancia}")

main()