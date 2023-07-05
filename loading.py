import time

BARRA_LONGITUD = 30
partes_loading = ['-', '\\', '|', '/'] #elementos que utilizaré en la animación de giro

for i in range(BARRA_LONGITUD+1):
    frame = i % len(partes_loading) #con la operación de modulo la animación se repite en cada vuelta
    print(f'\r[{partes_loading[frame]*i:=<{BARRA_LONGITUD}}]', end='') 
    # f'\r[]' para que se borre la linea actual
    # partes_loading[frame]*i hace que se llene la barra de progreso
    # :=<{BARRA_LONGITUD} utilizará un igual para todo lo que falte por rellenar
    # end='' para que no haga el salto de linea al final
    time.sleep(0.3) #para controlar la velocidad de la animación

#si quiero rellenarlo en dirección contraria o desde el centro sustituir el < por un > o bien ^
for i in range(BARRA_LONGITUD+1):
    frame = i % len(partes_loading) 
    print(f'\r[{partes_loading[frame]*i:=>{BARRA_LONGITUD}}]', end='') 
    time.sleep(0.3) 

for i in range(BARRA_LONGITUD+1):
    frame = i % len(partes_loading) 
    print(f'\r[{partes_loading[frame]*i:=^{BARRA_LONGITUD}}]', end='') 
    time.sleep(0.3) 