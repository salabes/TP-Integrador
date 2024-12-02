import random
class GeneradorDeMonedas:
    def generar_ejemplo_de_mismo_numero(self, longitud):
        """Genera monedas donde todos las moendas son iguales."""
        valor = random.randint(1, 100)
        return [valor] * longitud

    def generar_ejemplo_dos_numeros_intercalados(self, longitud):
        """Genera monedas intercalando dos tipos de moneda."""
        a, b = random.randint(1, 100), random.randint(1, 100)
        return [random.choice([a, b]) for _ in range(longitud)]

    def generar_ejemplo_con_un_valor_grande_centrado(self, longitud):
        """Genera monedas con una moneda muy grande centrada."""
        res = [random.randint(1, 100) for _ in range(longitud - 1)]
        res.insert(longitud // 2, 1000)
        return res

    def generar_ejemplo_grandes_centrados(self, longitud):
        """Genera monedas con varia moneda grande centrada en el medio."""
        return [
            random.randint(500, 1000) if longitud * 0.4 <= i < longitud * 0.6 else random.randint(10, 500)
            for i in range(longitud)
        ]

    def generar_ejemplo_grandes_en_los_laterales(self, longitud):
        """Genera monedas con moendas grandes en los laterales."""
        return [
            random.randint(500, 1000) if i <= longitud // 4 or i >= (longitud * 3) // 4 else random.randint(10, 300)
            for i in range(longitud)
        ]

    def generar_ejemplo_pequeños_grandes_intercalados(self, longitud):
        """Genera monedas alternando moendas pequeños y grandes."""
        return [random.randint(1, 100) if i % 2 == 0 else random.randint(100, 1000) for i in range(longitud)]
    
    def generar_ejemplo_aleatorio(self, longitud):
        """Genera monedas de valores aleatorios. """
        return [random.randint(1,1000) for _ in range(longitud)]