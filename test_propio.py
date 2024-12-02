from generador_monedas import GeneradorDeMonedas
import parte2

def probar_ejemplos():
    generador = GeneradorDeMonedas()

    # Casos con un patrón predeterminado y variación de número específico.
    ejemplos = [
        ("Monedas de mismo número", generador.generar_ejemplo_de_mismo_numero(10)),
        ("Monedas de dos números intercalados", generador.generar_ejemplo_dos_numeros_intercalados(10)),
        ("Monedas con valor grande centrado", generador.generar_ejemplo_con_un_valor_grande_centrado(10)),
        ("Monedas con valores grandes centrados", generador.generar_ejemplo_grandes_centrados(10)),
        ("Monedas con valores grandes en los laterales", generador.generar_ejemplo_grandes_en_los_laterales(10)),
        ("Moendas de Pequeños y grandes intercalados", generador.generar_ejemplo_pequeños_grandes_intercalados(10)),
        ("Monedas aleatorio", generador.generar_ejemplo_aleatorio(10)),
    ]

    for descripcion, monedas in ejemplos:
        sophia_monedas, ganancia_sophia, mateo_monedas, mateo_ganancia, jugadas = parte2.obtener_maxima_monedas(monedas)
        mostrar_resultado(descripcion, monedas, sophia_monedas, ganancia_sophia, mateo_monedas, mateo_ganancia, jugadas)

def mostrar_resultado(descripcion, monedas, sophia_monedas, ganancia_sophia, mateo_monedas, mateo_ganancia, jugadas):
    assert ganancia_sophia >= mateo_ganancia, (
        f"Error en '{descripcion}': Sophia no tiene más ganancia que Mateo.\n"
        f"Ganancia Sophia: {ganancia_sophia}, Ganancia Mateo: {mateo_ganancia}\n"
        f"Monedas: {monedas}"
    )
    print(f"Ejemplo: {descripcion}")
    print(f"monedas: {monedas}")
    print(jugadas)
    print(f"Sophia_monedas: {sophia_monedas}")
    print(f"Sophia_Ganancia: {ganancia_sophia}")
    print(f"Mateo_monedas: {mateo_monedas}")
    print(f"Mateo_Ganancia: {mateo_ganancia}")
    print()


if __name__ == "__main__":
    probar_ejemplos()

