# TP-Integrador

Para correr el programa y poder ejecutarle pruebas debemos hacer los siguientes pasos:

1-El programa se core con el siguiente comando: ./programa.py [setdatos] [resultadosEsperados]

[setDatos] = "nombreArchivo.txt" [ResultadosEsperados] = "nombreArchivo.txt"

Un ejemplo seria:  "./programa.py 100.txt ResultadosEsperados.txt"

2-El set de datos debe tener esta estructura:
 
#Los valores de las monedas de la fila se muestran tal cual su orden correspondiente, separados por ;
72;165;794;892;880;341;882;570;679;725;979;375;459;603;112;436;587;699;681;83

Es exactamente la misma esctructura que los archivos de prueba de la catedra.

3- El archivo resultadosEsperados debe tener este formato:

Es posible que en función del algoritmo que se decida utilizar, estas no sean las ganancias que obtengan. Tomen esto como un ejemplo, y lo importante es que Sophia siempre gane.

20.txt
Última moneda para Sophia; Primera moneda para Mateo; Última moneda para Sophia; Primera moneda para Mateo; Primera moneda para Sophia; Última moneda para Mateo; Primera moneda para Sophia; Última moneda para Mateo; Primera moneda para Sophia; Primera moneda para Mateo; Primera moneda para Sophia; Última moneda para Mateo; Primera moneda para Sophia; Última moneda para Mateo; Primera moneda para Sophia; Última moneda para Mateo; Primera moneda para Sophia; Última moneda para Mateo; Primera moneda para Sophia; Última moneda para Mateo
Ganancia de Sophia: 7165

25.txt
Última moneda para Sophia; Última moneda para Mateo; Primera moneda para Sophia; Última moneda para Mateo; Primera moneda para Sophia; Última moneda para Mateo; Última moneda para Sophia; Primera moneda para Mateo; Última moneda para Sophia; Última moneda para Mateo; Primera moneda para Sophia; Última moneda para Mateo; Última moneda para Sophia; Última moneda para Mateo; Primera moneda para Sophia; Primera moneda para Mateo; Primera moneda para Sophia; Primera moneda para Mateo; Última moneda para Sophia; Última moneda para Mateo; Última moneda para Sophia; Primera moneda para Mateo; Primera moneda para Sophia; Última moneda para Mateo; Última moneda para Sophia
Ganancia de Sophia: 9635

...

4-En caso de no poder correr el problema por no tener autorizado el codigo: chmod +x programa.py

5-Los archivos de Prueba deben encontrarse en una carpeta llamada pruebas ubicada en el mismo directorio que el archivo programa.py

ACLARACION.

El archivo testsParte1.py son las preubas realizadas por nosotros junto con las pruebas con el set de datos brindado por la catedra.En el caso de las pruebas de catedra, corroboramos que la ganancia sea la esperada por la catedra y el orden de las jugadas sea el mismo. Sabemos que lo importante era que simplemente gane Sophia, pero en este caso sucede lo mismo quenos brinda la catedra. Si se corre este archivo se podran ver los graficos utilizados para las explicaciones y los tiempos de las pruebas elegidas.
