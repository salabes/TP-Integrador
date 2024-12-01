def elegir_monedas(monedas):
    sophia_puntuacion = 0
    mateo_puntuacion = 0

    primer_moneda = 0
    ultima_moneda = len(monedas)-1

    pasos = []

    while primer_moneda <= ultima_moneda:
        #primero elije Sophia
        if monedas[primer_moneda] > monedas[ultima_moneda]:
            sophia_puntuacion += monedas[primer_moneda]
            primer_moneda += 1
            pasos.append(" Primera moneda para Sophia")
        else:
            sophia_puntuacion += monedas[ultima_moneda]
            ultima_moneda -= 1
            pasos.append(" Última moneda para Sophia")

        #Elije sophia para mateo en caso de que siga habiendo monedas
        if primer_moneda <= ultima_moneda:
            if monedas[primer_moneda] < monedas[ultima_moneda]:
                mateo_puntuacion += monedas[primer_moneda]
                primer_moneda += 1
                pasos.append(" Primera moneda para Mateo")
            else:
                mateo_puntuacion += monedas[ultima_moneda]
                ultima_moneda -= 1
                pasos.append(" Última moneda para Mateo")
            
    return sophia_puntuacion,pasos

# en este caso por cada iteracion quitamos 2 monedas, a menos que quede 1 sola, 
# por lo que iteramos sobre el arreglo n/2 veces, siendo n la cantidad de monedas
# dentro de la iteracion las operaciones son O(1). La complejidad es O(n/2) = 1/2 . O(n) = O(n)









