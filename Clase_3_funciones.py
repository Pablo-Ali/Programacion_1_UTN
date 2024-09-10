def calcular_precio_con_iva(valor_sin_iva : float, iva : float = 21 ) -> float: # ": float" y el "->"  no son restrictivos. Es para que quede en la documentación como lo esperable
    '''
    Función que se encarga de calcular el precio con iva.
    Recibe un precio sin iva y el procendaje de iva (opcional) que por defecto es 21%.
    Retorna el precio con el iva agregado
    '''
    resultado = valor_sin_iva * (1 + (iva / 100)) #valor_sin_iva * 1.21 
    return resultado 

precio_con_iva_1 = calcular_precio_con_iva(100)
precio_con_iva_2 = calcular_precio_con_iva(100, 10) # pasando parámetros por posición
precio_con_iva_3 = calcular_precio_con_iva(iva = 10, valor_sin_iva = 100) # pasando parámetros por nombre

print(precio_con_iva_1)
print(precio_con_iva_2)
print(precio_con_iva_3)