def obtener_maxima_monedas(monedas):
    n = len(monedas)
    valores_acumulados = [[0] * n for _ in range(n)]

    for i in range(n):
        valores_acumulados[i][i] = monedas[i]
    
    k = n % 2
    for intervalo in range(2 + k, n + 1, 2):
        for i in range(n - intervalo + 1):
            j = i + intervalo - 1
            valores_acumulados[i][j] = decidir_extremo(monedas, i, j, valores_acumulados)

    return recuperar_elecciones_optimas(monedas, valores_acumulados) 
 
def decidir_extremo(monedas, i, j, valores_acumulados):
    siguiente = valores_acumulados[i + 2][j] if i + 2 <= j else 0
    ultimo = valores_acumulados[i + 1][j - 1] if i + 1 <= j - 1 else 0

    if monedas[i + 1] > monedas[j]:
        elegir_izquierda = monedas[i] + siguiente
    else:
        elegir_izquierda = monedas[i] + ultimo
    
    primero = valores_acumulados[i + 1][j - 1] if i + 1 <= j - 1 else 0
    anteultimo = valores_acumulados[i][j - 2] if i <= j - 2 else 0

    if monedas[i] > monedas[j - 1]:
        elegir_derecha = monedas[j] + primero
    else:
        elegir_derecha = monedas[j] + anteultimo 

    if elegir_izquierda > elegir_derecha:
        return elegir_izquierda
    else:
        return elegir_derecha

def contar_monedas(monedas, monedas_jugador):
    monedas_jugador = [monedas[i] for i in monedas_jugador]
    ganancia_jugador = sum(monedas_jugador)

    return ganancia_jugador, monedas_jugador

def recuperar_elecciones_optimas(monedas, valores_acumulados):
    i = 0
    j = len(monedas) - 1
    jugada_sophia = []
    jugada_mateo = []
    ganancia_esperanza = valores_acumulados[i][j]

    jugada_sophia, jugada_mateo =_recuperar_elecciones_optimas(monedas, valores_acumulados, i, j, jugada_sophia, jugada_mateo, ganancia_esperanza)
    
    ganancia_sophia = sum(jugada_sophia)
    ganancia_mateo = sum(jugada_mateo)

    return ganancia_sophia, jugada_sophia, ganancia_mateo, jugada_mateo


def _recuperar_elecciones_optimas(monedas, valores_acumulados, i, j, monedas_sophia, monedas_mateo, ganancia_esperanza):
    ganancia_actual = 0

    while True:

        if (len(monedas_sophia) + len(monedas_mateo) == len(monedas)) or ganancia_esperanza == ganancia_actual:
            break

        if i == j:
            monedas_sophia.append(monedas[i])
            return monedas_sophia, monedas_mateo

        ultimo = monedas[j]
        siguiente = monedas[i + 1]
        if ultimo >= siguiente:
            siguiente_pos = i + 1
            ultimo_pos = j - 1
        else:
            siguiente_pos = i + 2
            ultimo_pos = j

        if ganancia_esperanza == monedas[i] + valores_acumulados[siguiente_pos][ultimo_pos]:
            eleccion_sophia(monedas, i, monedas_sophia)
            eleccion_mateo(monedas, i + 1, siguiente_pos, j, monedas_mateo)
            ganancia_esperanza = ajustar_esperanza(ganancia_esperanza, monedas[i]) 

        else:
            
            anteultima = monedas[j - 1]
            primera = monedas[i]
            if anteultima > primera:
                siguiente_pos = i 
                ultimo_pos = j - 2
            else:
                siguiente_pos = i + 1
                ultimo_pos = j - 1

            eleccion_sophia(monedas, j, monedas_sophia)
            eleccion_mateo(monedas, i, siguiente_pos, j - 1, monedas_mateo)
            ganancia_esperanza = ajustar_esperanza(ganancia_esperanza, monedas[j])
                                                  
        i, j = siguiente_pos, ultimo_pos
    return monedas_sophia, monedas_mateo

def eleccion_mateo(monedas, pos, siguiente_pos, moneda_elegida_pos, monedas_mateo):
    if pos == siguiente_pos:
        monedas_mateo.append(monedas[moneda_elegida_pos])
    else:
        monedas_mateo.append(monedas[pos])

def eleccion_sophia(monedas, eleccion, monedas_sophia):
    monedas_sophia.append(monedas[eleccion])

def ajustar_esperanza(esperanza, ganancia_parcial):
    esperanza -= ganancia_parcial
    return esperanza

