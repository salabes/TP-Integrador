from random import seed

from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import scipy as sp
import time
from scipy.optimize import curve_fit
from generador_monedas import GeneradorDeMonedas 
import parte2

def medir_tiempo_ejecucion():
    mediciones = []
    generador = GeneradorDeMonedas()

    for i in range(1, 1000, 100):
        monedas = generador.generar_ejemplo_aleatorio(i)
        inicio = time.time()
        parte2.obtener_maxima_monedas(monedas)
        fin = time.time()
        tiempo = fin - inicio
        mediciones.append((i,tiempo))

    return mediciones

def modelo_cuadratico(x, a, b, c):
    return a * x**2 + b * x + c

def graficar_y_ajustar_mediciones(mediciones):
    tamaños = np.array([m[0] for m in mediciones])
    tiempos = np.array([m[1] for m in mediciones])

    popt, pcov = curve_fit(modelo_cuadratico, tamaños, tiempos)

    # Coeficientes de la curva ajustada
    a, b, c = popt
    print(f"Coeficientes de la curva cuadrática ajustada: a={a}, b={b}, c={c}")

    tiempos_ajustados = modelo_cuadratico(tamaños, *popt)

    # Calcular el error y ECM
    error = tiempos - tiempos_ajustados

    ECM = np.sqrt(np.mean(error**2))
    print(f"Error cuadrático medio (ECM): {ECM}")

    plt.figure(figsize=(12, 6))

    # Subgráfico 1: Gràfico de mediciones con ajuste de la curva cuadràtica
    plt.subplot(1, 2, 1)
    plt.scatter(tamaños, tiempos, color='blue', label='Mediciones reales')
    plt.plot(tamaños, tiempos_ajustados, color='red', label='Curva ajustada')
    plt.xlabel('Tamaño de las monedas')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Ajuste de Curva Cuadrática al Tiempo de Ejecución')
    plt.legend()

    # Subgráfico 2: Gráfico de error de ajuste
    plt.subplot(1, 2, 2)
    plt.scatter(tamaños, error, color='green', label='Error')
    plt.axhline(0, color='black', linestyle='--', label='Error 0')
    plt.xlabel('Tamaño de las monedas')
    plt.ylabel('Error')
    plt.title('Error del Ajuste Cuadrático')
    plt.legend()

    # Guardar los gráficos en un archivo
    plt.tight_layout()
    plt.savefig("grafico_tiempos_y_errores.png")
    print("Gráficos guardados como 'grafico_tiempos_y_errores.png'")

mediciones = medir_tiempo_ejecucion()
print(mediciones)
graficar_y_ajustar_mediciones(mediciones)



