def backtrack(tablero, barcos, fila_demandas, columna_demandas, indice_barco, min_demanda_incumplida,barcos_usados):
    fila_demandas_restantes = fila_demandas
    columna_demandas_restantes = columna_demandas
    orientacion = 'N'

    if indice_barco == len(barcos):
        demanda_incumplida = calcular_demanda_incumplida(fila_demandas_restantes,columna_demandas_restantes)
        return min(min_demanda_incumplida, demanda_incumplida),tablero
    
    barco = barcos[indice_barco]
    if(any(barco < fila_demandas[i]for i in range(len(fila_demandas)))and any( barco < columna_demandas[i] for i in range(len(columna_demandas)))):
       
        for fila in range(len(tablero)):
            if fila_demandas[fila] == 0: 
                continue
            for col in range(len(tablero[0])):
                if columna_demandas[col] == 0: 
                    continue
                se_puede_colocar_barco,orientacion = puede_colocar_barco(tablero, fila, col, barco,fila_demandas_restantes,columna_demandas_restantes,orientacion)
                if se_puede_colocar_barco:
                    tablero,barcos_usados = colocar_barco(tablero, fila, col, barco, fila_demandas, columna_demandas, orientacion,barcos_usados)

                    min_demanda_incumplida,tablero = backtrack(tablero, barcos, fila_demandas, columna_demandas, indice_barco + 1, min_demanda_incumplida,barcos_usados)

                    if(len(barcos_usados) -1 == len(barcos)):
                        return min_demanda_incumplida,tablero
                    if(min_demanda_incumplida > 0):
                        tablero,barcos_usados = quitar_barco(tablero, fila, col, barco, fila_demandas, columna_demandas, orientacion,barcos_usados)
                        min_demanda_incumplida,tablero = backtrack(tablero, barcos, fila_demandas, columna_demandas, indice_barco + 1, min_demanda_incumplida,barcos_usados)
               

                    if min_demanda_incumplida == 0:  
                        return 0


    min_demanda_incumplida,tablero = backtrack(tablero, barcos, fila_demandas, columna_demandas, indice_barco + 1, min_demanda_incumplida,barcos_usados)


    return min_demanda_incumplida,tablero


def calcular_demanda_incumplida(fila_demandas, columna_demandas):
   
    demanda_incumplida = 0
    demanda_incumplida = sum(fila_demandas) + sum(columna_demandas)
    
    return demanda_incumplida

def verificar_demandas_compatibles(tablero, fila, col, barco, fila_demandas, columna_demandas, orientacion):

    
    if orientacion == 'H':
    
        if   barco > fila_demandas[fila]:
            return False
    
        for i in range(col, col + barco):
            if i >= len(tablero) or columna_demandas[i] == 0:
                return False
        
    elif orientacion == 'V':

        if   barco > columna_demandas[col]:
            return False

        for i in range(fila, fila + barco):
            if i >= len(tablero) or fila_demandas[i] == 0: 
                return False
        

    return True



def verificar_barcos_adyacentes(tablero, fila, col, barco, orientacion, limite_fila, limite_columna):
    direcciones = [
        (-1, 0),  
        (1, 0),   
        (0, -1),  
        (0, 1),   
        (-1, -1), 
        (-1, 1),  
        (1, -1),  
        (1, 1)   
    ]
    
    if orientacion == 'H':
        for i in range(barco):
            for dx, dy in direcciones:
                new_fila = fila + dx
                new_col = col + i + dy
                if 0 <= new_fila < limite_fila and 0 <= new_col < limite_columna:
                    if tablero[new_fila][new_col] != 0:
                        return True
        return False
    
    if orientacion == 'V':
        for i in range(barco):
            for dx, dy in direcciones:
                new_fila = fila + i + dx
                new_col = col + dy
                if 0 <= new_fila < limite_fila and 0 <= new_col < limite_columna:
                    if tablero[new_fila][new_col] != 0:
                        return True
        return False
    
    return False

def puede_colocar_barco(tablero, fila, col, barco,fila_demandas_restantes,columna_demandas_restantes,orientacion):
    limite_fila = len(fila_demandas_restantes)
    limite_columna = len(columna_demandas_restantes)
    if col + barco - 1 < len(tablero[0]): 
        if all(tablero[fila][col + i] == 0 for i in range(barco)): 
                orientacion = 'H'
                if(verificar_demandas_compatibles(tablero,fila,col,barco,fila_demandas_restantes,columna_demandas_restantes,orientacion)):
                    if(not verificar_barcos_adyacentes(tablero,fila,col,barco,orientacion,limite_fila,limite_columna)):
                        return True,orientacion

    if fila + barco - 1 < len(tablero):  
        if all(tablero[fila + i][col] == 0 for i in range(barco)):             
            orientacion = 'V'
            if(verificar_demandas_compatibles(tablero,fila,col,barco,fila_demandas_restantes,columna_demandas_restantes,orientacion)):
                if(not verificar_barcos_adyacentes(tablero,fila,col,barco,orientacion,limite_fila,limite_columna)):
                        return True,orientacion

    return False,'N'



def colocar_barco(tablero, fila, col, barco, fila_demandas, columna_demandas, orientacion, barcos):
    barco_id = barcos[-1]
    
    if orientacion == 'H':
        for i in range(barco):
            tablero[fila][col + i] = barco_id 
            columna_demandas[col + i] -= 1    
        fila_demandas[fila] -= barco       

    elif orientacion == 'V':
        for i in range(barco):
            tablero[fila + i][col] = barco_id  
            fila_demandas[fila + i] -= 1     
        columna_demandas[col] -= barco      

    barcos.append(barco_id + 1)

    return tablero, barcos


def quitar_barco(tablero, fila, col, barco, fila_demandas, columna_demandas, orientacion,barcos):
    if orientacion == 'H':  
        for i in range(barco):
            tablero[fila][col + i] = 0 
            fila_demandas[fila]= fila_demandas[fila] +1 
            columna_demandas[col+i]= columna_demandas[col+i] + 1 
    elif orientacion == 'V':   
        for i in range(barco):
            tablero[fila + i][col] = 0  
            fila_demandas[fila+i]= fila_demandas[fila+i] + 1
            columna_demandas[col]= columna_demandas[col] + 1 

    
    barcos.pop(len(barcos)-1)

    return tablero,barcos



def resolver_problema(n, m, barcos, fila_demandas, columna_demandas):
    tablero = [[0] * m for _ in range(n)]  
    barcos_restantes = sorted(barcos, reverse=True)  
    min_demanda_incumplida = float('inf') 
    barcos_usados = [1]
    demanda =calcular_demanda_incumplida(fila_demandas,columna_demandas)
    min_demanda_incumplida,tablero = backtrack(tablero, barcos_restantes, fila_demandas, columna_demandas, 0, min_demanda_incumplida,barcos_usados)
    

    return (demanda - min_demanda_incumplida),tablero

