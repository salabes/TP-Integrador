#!/usr/bin/env python3
import sys
import unittest
import obtenerDatos
import parte2



def main():
    if len(sys.argv) != 3:
        print("Por favor, proporciona exactamente 2 argumentos.")
        sys.exit(1)

    # Los argumentos se pasan como cadenas, puedes convertirlos según sea necesario
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]

    MONEDAS_1 = obtenerDatos.obtener_monedas(arg1)
    ganancia_sophia_minima = arg2

    sophia_moneda, sophia_ganancia, mateo_monedas, mateo_ganancia, jugadas = parte2.obtener_maxima_monedas(MONEDAS_1)

    print(f"Ganncia Esperada minima de sophia: {ganancia_sophia_minima}")
    print(f"Ganncia obtenida de sophia: {sophia_ganancia}")


main()