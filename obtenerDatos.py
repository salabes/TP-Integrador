def obtener_monedas(ruta):
    monedas = []
    with open (f'pruebas/TP2/{ruta}','r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            if linea.startswith("# Los valores de las monedas"):
                monedas = list(map(int,lineas[lineas.index(linea) + 1].strip().split(";")))
                break

    return monedas


def obtener_resultados(ruta):
    resultados = {}

    with open(ruta, "r") as archivo:
        datos = archivo.read().strip()  # Lee todo el contenido y elimina espacios extra

    # Divide por secciones usando el nombre de archivo como referencia
    secciones = datos.split("\n\n")  # Cada sección está separada por líneas en blanco

    for seccion in secciones:
        lineas = seccion.split("\n")
        nombre_archivo = lineas[0]  # La primera línea es el nombre del archivo
        
        # Inicializa las listas de Sophia y Mateo para este archivo
        acciones_sophia = []
        acciones_mateo = []
        
        # Procesa las líneas de elecciones (normalmente en la segunda línea)
        for linea in lineas[1:]:
            if "Ganancia" in linea:
                continue  # Ignora las líneas de ganancias
            elecciones = linea.split(";")  # Divide las elecciones separadas por ";"
            for eleccion in elecciones:
                eleccion = eleccion.strip()  # Limpia espacios extras
                if "Sophia" in eleccion:
                    # Extrae el número entre paréntesis
                    numero = int(eleccion.split("(")[-1].strip(")"))
                    acciones_sophia.append(numero)
                elif "Mateo" in eleccion:
                    # Extrae el número entre paréntesis
                    numero = int(eleccion.split("(")[-1].strip(")"))
                    acciones_mateo.append(numero)
        
        # Guarda las listas en el diccionario
        resultados[nombre_archivo] = {
            "Sophia": acciones_sophia,
            "Mateo": acciones_mateo
        }
    return resultados

#resultados = obtener_resultados("Resultados Esperados.txt")

# Muestra los resultados
#for archivo, datos in resultados.items():
    #print(f"Archivo: {archivo}")
    #print(f"  Sophia: {datos['Sophia']}")
    #print(f"  Mateo: {datos['Mateo']}")

#print(obtener_monedas("25.txt"))