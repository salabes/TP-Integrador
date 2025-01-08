import unittest
import obtener_datos
import parte2
#"5.txt"
MONEDAS_1 = obtener_datos.obtener_monedas("5.txt")

#"10.txt"
MONEDAS_2 = obtener_datos.obtener_monedas("10.txt")

#"20.txt"
MONEDAS_3 = obtener_datos.obtener_monedas("20.txt")

#"25.txt"
MONEDAS_4 = obtener_datos.obtener_monedas("25.txt")

#"50.txt"
MONEDAS_5 = obtener_datos.obtener_monedas("50.txt")

#"100.txt"
MONEDAS_6 = obtener_datos.obtener_monedas("100.txt")

#"1000.txt"
MONEDAS_7 = obtener_datos.obtener_monedas("1000.txt")

#"2000.txt"
MONEDAS_8 = obtener_datos.obtener_monedas("2000.txt")

#"5000.txt"
MONEDAS_9 = obtener_datos.obtener_monedas("5000.txt")

#"10000.txt"
MONEDAS_10 = obtener_datos.obtener_monedas("10000.txt")

RESULTADOS_ESPERADOS = obtener_datos.obtener_resultados("Resultados Esperados.txt")


class TestMonedasElegidas(unittest.TestCase):
    def test_monedas_elegidas(self):
        for archivo, esperado in RESULTADOS_ESPERADOS.items():
            monedas = obtener_datos.obtener_monedas(archivo)
            sophia_ganancia, sophia_moneda, mateo_ganancia, mateo_monedas = parte2.obtener_maxima_monedas(monedas)

            self.assertEqual(sophia_moneda, esperado["Sophia"], f"Error en Sophia para {archivo}")
            self.assertEqual(mateo_monedas, esperado["Mateo"], f"Error en Mateo para {archivo}")
            self.assertEqual(sophia_ganancia, esperado["Ganancia Sophia"], f"Error en la ganancia de Sophia para {archivo}")
            self.assertEqual(mateo_ganancia, esperado["Ganancia Mateo"], f"Error en la ganancia de Mateo para {archivo}")

if __name__ == "__main__":
    unittest.main()
