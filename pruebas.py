def es_cuadrado_magico(matriz):
        """
        Verifica si una matriz es un cuadrado mágico (suma igual en filas, columnas y diagonales).
        
        Args:
            matriz (list): Lista de listas que representa una matriz cuadrada
            
        Returns:
            bool: True si es un cuadrado mágico, False en caso contrario
        """
        #suma filas
        suma=0
        anterior=0
        for j in range(len(matriz)):
            
            suma=0
            for i in matriz[j]:
                suma=suma+i

            if j ==0:
                anterior=suma
            elif suma !=anterior:
                print("no es cuadrado magico")
                break

        print(suma)

    
    #suma columnas
        suma1=0
        anterior=0
        for j in range(len(matriz[0])):
            
            suma1=0
            for i in range(len(matriz)):

                suma1=matriz[i][j]+suma1

            if j ==0:
                anterior=suma1
            elif suma1 !=anterior:
                print("no es cuadrado magico")
                break

        print(suma1)
        suma2=0
        for i in range(len(matriz)):
            suma2= suma2+ matriz[i][i]
        print(suma2)


        if suma1==suma==suma2:
            print("son cuadrado magico")


            
        

        



es_cuadrado_magico([
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
])