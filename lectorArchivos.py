
def leer_archivo(path):
    # Inicializamos las listas vacías para almacenar los datos
    demanda_filas = []
    demanda_columnas = []
    longitudes_barcos = []

    # Abrimos el archivo en modo lectura
    with open(f'pruebas/TP3/{path}', 'r') as f:
        # Leemos todas las líneas del archivo
        lineas = f.readlines()

    # Filtramos solo las líneas de comentarios (comienzan con #) y mantenemos las líneas vacías
    lineas = [linea.strip() for linea in lineas if not linea.startswith('#')]

    # Imprimimos las líneas procesadas para ver el contenido después de quitar comentarios
   # print("Líneas procesadas:", lineas)

    # Separamos las secciones usando una lista auxiliar
    secciones = []
    seccion_actual = []

    for linea in lineas:
        if linea == "":  # Si encontramos una línea vacía, guardamos la sección actual
            if seccion_actual:  # Si la sección actual no está vacía, la agregamos
                secciones.append(seccion_actual)
                seccion_actual = []  # Reiniciamos la sección
        else:
            seccion_actual.append(linea)

    # Asegurarnos de agregar la última sección si no está vacía
    if seccion_actual:
        secciones.append(seccion_actual)

    # Imprimimos las secciones encontradas para depurar
    #print("Secciones encontradas:", secciones)

    # Verificamos cuántas secciones se han encontrado
    if len(secciones) != 3:
        raise ValueError(f"El archivo debe contener exactamente 3 secciones. Se encontraron {len(secciones)}.")

    # Primer bloque: demandas de las filas
    demanda_filas = list(map(int, secciones[0]))

    # Segundo bloque: demandas de las columnas
    demanda_columnas = list(map(int, secciones[1]))

    # Tercer bloque: longitudes de los barcos
    longitudes_barcos = list(map(int, secciones[2]))

    return demanda_filas, demanda_columnas, longitudes_barcos

