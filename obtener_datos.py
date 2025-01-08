def obtener_monedas(ruta):
    monedas = []
    with open (ruta,'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            if linea.startswith("# Los valores de las monedas"):
                monedas = list(map(int,lineas[lineas.index(linea) + 1].strip().split(";")))
                break

    return monedas

def obtener_resultados(ruta):
    resultados = {}

    with open(ruta, "r") as archivo:
        datos = archivo.read().strip()

    ejemplos = datos.split("\n\n")

    for ejemplo in ejemplos:
        lineas = ejemplo.split("\n")
        nombre_archivo = lineas[0] 
        
        jugadas_sophia = []
        jugadas_mateo = []
        ganancia_sophia = 0
        ganancia_mateo = 0

        for linea in lineas[1:]:
            if "Ganancia Sophia" in linea:
                ganancia_sophia = int(linea.split(":")[1].strip())  
            elif "Ganancia Mateo" in linea:
                ganancia_mateo = int(linea.split(":")[1].strip())
            elif ";" in linea:

                jugadas = linea.split(";") 
                for jugada in jugadas:
                    jugada = jugada.strip()

                    if "Sophia" in jugada:
                        numero = int(jugada.split("(")[-1].strip(")"))
                        jugadas_sophia.append(numero)

                    elif "Mateo" in jugada:
                        numero = int(jugada.split("(")[-1].strip(")"))
                        jugadas_mateo.append(numero)
        
        resultados[nombre_archivo] = {
            "Sophia": jugadas_sophia,
            "Mateo": jugadas_mateo,
            "Ganancia Sophia": ganancia_sophia,
            "Ganancia Mateo": ganancia_mateo
        }
    return resultados









