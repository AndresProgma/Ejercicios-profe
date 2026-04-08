class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):


        lista_inversa=[]
        for i in range(len(lista),-1,-1):
            lista_inversa[i]=lista[i]

        print(lista_inversa)

        """
        Invierte el orden de los elementos en una lista sin usar reversed() o lista[::-1].
        
        Args:
            lista (list): Lista a invertir
            
        Returns:
            list: Lista con los elementos en orden inverso
        """
        
    
    def buscar_elemento(self, lista, elemento):
        
        for i in range(len(lista)):
            if lista[i] ==elemento:
                return i
        print("elemento no encontrado")
        
        
        """
        Busca un elemento en una lista y devuelve su índice (o -1 si no existe).
        Implementación manual sin usar index().
        
        Args:
            lista (list): Lista donde buscar
            elemento: Elemento a buscar
            
        Returns:
            int: Índice del elemento o -1 si no se encuentra
        """
        
    
    def eliminar_duplicados(self, lista):

        
        nueva_lista = []

        for elemento in lista:
            if elemento not in nueva_lista:
                nueva_lista.append(elemento)

        return nueva_lista




        """
        Elimina elementos duplicados de una lista sin usar set().
        Mantiene el orden original de aparición.
        
        Args:
            lista (list): Lista con posibles duplicados
            
        Returns:
            list: Lista sin elementos duplicados
        """
        
    
    def merge_ordenado(self, lista1, lista2):
        
        lista3=lista1+lista2

        for i in range(len(lista3)):
            for j in range(0,len(lista3)-i-1):
                if lista3[j] > lista3[j+1]:
                    lista3[j],lista3[j+1]= lista3[j+1],lista3[j]

        return lista3
        




        """
        Combina dos listas ordenadas en una sola lista ordenada.
        
        Args:
            lista1 (list): Primera lista ordenada
            lista2 (list): Segunda lista ordenada
            
        Returns:
            list: Lista combinada y ordenada
        """
    
    
    def rotar_lista(self, lista, k):
        repeticiones=k%len(lista)

        list_to_add=[0]*repeticiones
        
        for i in list_to_add:
            lista.insert(0,lista.pop())
            
        return lista
        
        "[1,2,3,4,5]"
        "lista[-2:] → [4,5]   # últimos k"
        "lista[:-2] → [1,2,3]   # TOD0 menos los últimos k"


       
        
        """
        Rota los elementos de una lista k posiciones a la derecha.
        
        Args:
            lista (list): Lista a rotar
            k (int): Número de posiciones a rotar
            
        Returns:
            list: Lista rotada
        """
        
    
    def encuentra_numero_faltante(lista):
        for i in range(len(lista)):
            if lista[i] != i+1:
                
                return i+1





        """
        Encuentra el número faltante en una lista de enteros del 1 al n.
        
        Args:
            lista (list): Lista de enteros del 1 al n con un número faltante
            
        Returns:
            int: El número que falta en la secuencia
        """
        
    
    def es_subconjunto(self, conjunto1, conjunto2):
        
        for i in conjunto1:

            if i not in conjunto2:
                return False
        return True


                

        """
        Verifica si conjunto1 es subconjunto de conjunto2 sin usar set.
        
        Args:
            conjunto1 (list): Posible subconjunto
            conjunto2 (list): Conjunto principal
            
        Returns:
            bool: True si conjunto1 es subconjunto de conjunto2, False en caso contrario
        """
        
    
    def implementar_pila(self):
        
        pila = []

        def push(x):
            pila.append(x)

        def pop():
            if pila:
                return pila.pop()
            return None

        def peek():
            if pila:
                return pila[-1]
            return None

        def is_empty():
            return len(pila) == 0

        return {
            "push": push,
            "pop": pop,
            "peek": peek,
            "is_empty": is_empty
        }
            
        




        """
        Implementa una estructura de datos tipo pila (stack) usando listas.
        
        Returns:
            dict: Diccionario con métodos push, pop, peek y is_empty
        """
        
    
    def implementar_cola(self):

        pila=[]

        def enqueue(x):
            pila.insert(0,x)

        def dequeve():
            if pila:
                pila.pop()
            return None

        def peek():
            if pila:
                return pila[-1]
            return None
        
        def is_empty():
                return len(pila) == 0
        

        return{
            "enqueve":enqueue,
            "dequeve": dequeve,
            "peek": peek,
            "is_empty": is_empty


        }
            



        """
        Implementa una estructura de datos tipo cola (queue) usando listas.
        
        Returns:
            dict: Diccionario con métodos enqueue, dequeue, peek y is_empty
        """
        
    
    def matriz_transpuesta(self, matriz):
       def matriz_transpuesta(matriz):
        filaa=range(len(matriz))
        columna=range(len(matriz[0]))
        matriz_transpuesta1=[]
        for i in columna:
                fila=[] 

                for j in filaa:
                        fila.append(matriz[j][i])
                
                matriz_transpuesta1.append(fila)
                

        return matriz_transpuesta1




        """
        Calcula la transpuesta de una matriz.
        
        Args:
            matriz (list): Lista de listas que representa una matriz
            
        Returns:
            list: Matriz transpuesta
        """
        