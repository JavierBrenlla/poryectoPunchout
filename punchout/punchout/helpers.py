def getZonaHorariaFormateada(cadena):
    cadena += cadena[len(cadena) - 1]
    resultado = ""
    
    for i in range(len(cadena)):
        if i==3:
            resultado += ":"
            continue
        resultado += cadena[i]
        
    return resultado