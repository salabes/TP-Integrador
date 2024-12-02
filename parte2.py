def obtener_maxima_monedas(monedas):
    n = len(monedas)
    valores_acumulados = [[0] * n for _ in range(n)]
    elecciones = [[""] * n for _ in range(n)]

    for i in range(n):
        valores_acumulados[i][i] = monedas[i]
        elecciones[i][i] = "primero"

    for intervalo in range(2, n + 1):
        for i in range(n - intervalo + 1):
            j = i + intervalo - 1
            valores_acumulados[i][j], elecciones[i][j] = decidir_extremo(monedas, i, j, valores_acumulados)

    sophia_monedas, mateo_monedas, ganancia_sophia, ganancia_mateo, jugadas = recuperar_elecciones_optimas(monedas, elecciones)
    return sophia_monedas, ganancia_sophia, mateo_monedas, ganancia_mateo, jugadas

def decidir_extremo(monedas, i, j, valores_acumulados):
    siguiente = valores_acumulados[i + 2][j] if i + 2 <= j else 0
    ultimo = valores_acumulados[i + 1][j - 1] if i + 1 <= j - 1 else 0
    elegir_izquierda = monedas[i] + min(siguiente, ultimo)

    primero = valores_acumulados[i + 1][j - 1] if i + 1 <= j - 1 else 0
    anteultimo = valores_acumulados[i][j - 2] if i <= j - 2 else 0
    elegir_derecha = monedas[j] + min(primero, anteultimo)
    if elegir_izquierda >= elegir_derecha:
        return elegir_izquierda, "primero"
    else:
        return elegir_derecha, "ultimo"

def recuperar_elecciones_optimas(monedas, elecciones):
    n = len(monedas)
    i, j = 0, n - 1
    sophia_monedas = []
    mateo_monedas = []
    jugadas = []
    turno_sophia = True 

    while i <= j:
        if turno_sophia:  # Turno de Sophia
            if elecciones[i][j] == "primero":
                sophia_monedas.append(monedas[i])
                jugadas.append(f"Sophia elige {monedas[i]} de la izquierda")
                i += 1
            else:
                sophia_monedas.append(monedas[j])
                jugadas.append(f"Sophia elige {monedas[j]} de la derecha")
                j -= 1
        else:  # Turno de Mateo
            if elecciones[i][j] == "primero":
                mateo_monedas.append(monedas[i])
                jugadas.append(f"Mateo elige {monedas[i]} de la izquierda")
                i += 1
            else:
                mateo_monedas.append(monedas[j])
                jugadas.append(f"Mateo elige {monedas[j]} de la derecha")
                j -= 1
        turno_sophia = not turno_sophia

    ganancia_sophia = sum(sophia_monedas)
    ganancia_mateo = sum(mateo_monedas)
    return sophia_monedas, mateo_monedas, ganancia_sophia, ganancia_mateo, jugadas


