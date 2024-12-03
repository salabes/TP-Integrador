#!/usr/bin/env python3
import sys
import timeit
from lectorArchivos import leer_archivo
from backtracking import resolver_problema

def main():
    if len(sys.argv) != 3:
        print("Por favor, proporciona exactamente 2 argumentos.")
        sys.exit(1)

    # Los argumentos se pasan como cadenas, puedes convertirlos según sea necesario
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]

    time,demanda_cumplida,tablero = prueba(arg1)

    print(f"Tiempo de ejecución: {time} segundos")
    print(f"demanda solicitada : {arg2}")
    print(f"demanda obtenida : {demanda_cumplida}")





def prueba(arg1):

    demandas_filas, demandas_columnas, barcos = leer_archivo(arg1)
    n = len(demandas_filas)
    m = len(demandas_columnas)

    # Medir tiempo con timeit
    start_time = timeit.default_timer()
    demanda_cumplida , tablero = resolver_problema(n,m,barcos,demandas_filas,demandas_columnas)
    end_time = timeit.default_timer()
    time = end_time - start_time
    return time,demanda_cumplida,tablero

main()