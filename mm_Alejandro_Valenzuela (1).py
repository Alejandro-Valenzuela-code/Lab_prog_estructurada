def mm(A,B):   #Se define una funcion que recibe dos matrices llamada "mm"
    BT = list(zip(*B)) #zip sirve para tranponer B

    C = [] #matriz resultado que esta vacia 
    for fila in A:  #Recorre cada fila en A
        nueva_fila = [] #Crea una fila vacia para los resultados 
        for col in BT:   #Recorre cada columna de B ya traspuesta 
            valor = sum(x*y for x,y in zip(fila,col)) #multiplica las matrices 
            nueva_fila.append(valor) #Agrega el resultado a la nueva fila
        C.append(nueva_fila) #Agrega la nueva fila a la matriz final 
    return C    #Entrega la matriz resultante 

#EJEMPLO
A=[[1,2,3],
   [4,5,6]]    #Primera matriz 

B= [[7,8],
    [9,10],
    [11,12]] #Segunda matriz 

for fila in mm(A,B):
    print(fila)        