class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """
    
    def fibonacci(self, n):
        """
        Calcula el n-ésimo número de la secuencia de Fibonacci.
        
        Args:
            n (int): Posición en la secuencia (empezando desde 0)
            
        Returns:
            int: El n-ésimo número de Fibonacci
        """


        
    
    def secuencia_fibonacci(self, n):
        """
        Genera los primeros n números de la secuencia de Fibonacci.
        
        Args:
            n (int): Cantidad de números a generar
            
        Returns:
            list: Lista con los primeros n números de Fibonacci
        """
        Lista=[]
        
        for i in range(n-2):
            
            if Lista == []:
                Lista.append(0)
                Lista.append(1)
            else:
                Lista.append(Lista[-1]+Lista[-2])
        return Lista

    def es_primo(self, n):
        """
        Verifica si un número es primo.
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es primo, False en caso contrario
        """
        if n <= 1:
            return False
        for i in range(2,n-1):
            if n % 1 ==0:
                return False
        return True
    def generar_primos(self, n):
        """
        Genera una lista de números primos hasta n.
        
        Args:
            n (int): Límite superior para generar primos
            
        Returns:
            list: Lista de números primos hasta n
        """
        primos = []

        for i in range(2, n):

            for j in range(2,i):
                if i % j ==0:
                    break
            else:
                primos.append(i)

        return primos


    def es_numero_perfecto(self, n):
        """
        Verifica si un número es perfecto (igual a la suma de sus divisores propios).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número perfecto, False en caso contrario
        """

        for i in range(1,n):
            if n % i==0:
                suma+=i
        return suma == n
    
    def triangulo_pascal(filas):
        """
        Genera las primeras n filas del triángulo de Pascal.
        
        Args:
            filas (int): Número de filas a generar
            
        Returns:
            list: Lista de listas que representa el triángulo de Pascal
        """
        triangulo=[]
        for i in range(filas): 
            fila=[1]

            if triangulo:
                fila_anterior= triangulo[-1]
                for j in range(len(fila_anterior)-1):
                    fila.append(fila_anterior[j]+fila_anterior[j+1])
                fila.append(1)
                triangulo.append(fila)
            else:
                triangulo.append(fila)
        print(triangulo)      
        
    def factorial(n):
        """
        Calcula el factorial de un número.
        
        Args:
            n (int): Número para calcular su factorial
            
        Returns:
            int: El factorial de n
        """
        factorial=1
        for i in range (n,1,-1):
            factorial = factorial * i 
        print(factorial)
    

    
    def mcd(a, b):
        """
        Calcula el máximo común divisor de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El máximo común divisor de a y b
        """
        lista_divisores_a=[]
        lista_divisores_b=[]
        for i in range(1,a+1):
            if a % i == 0:
                lista_divisores_a.append(i)
        
        for i in range(1,b+1):
            if b % i == 0:
                lista_divisores_b.append(i)

        for j in lista_divisores_a:
             for h in lista_divisores_b:
                  if j == h:
                       maximo_c_divisor=j

                  



        print(lista_divisores_a)
        print(lista_divisores_b)
        print(maximo_c_divisor)


        




        
        


        
    
    def mcm(self, a, b):
        """
        Calcula el mínimo común múltiplo de dos números.
        
        Args:
            a (int): Primer número
            b (int): Segundo número
            
        Returns:
            int: El mínimo común múltiplo de a y b
        """

        
        multiplo= max(a,b)
        while True:
            if multiplo % a == 0 and multiplo % b ==0:
                minimo_c_multiplo= multiplo
                break
            else:
                multiplo+=multiplo

        print (minimo_c_multiplo)        
    
    def suma_digitos(n):
        """
        Calcula la suma de los dígitos de un número.
        
        Args:
            n (int): Número para sumar sus dígitos
            
        Returns:
            int: La suma de los dígitos de n
        """

        lista=[]
        
        for n in str(n):
            lista.append(int(n))
        suma=0
        print(lista)
        for numeros in range(0,len(lista)):
            suma=suma+lista[numeros]
            print(suma)
        print(suma)

    
    def es_numero_armstrong(self, n):
        """
        Verifica si un número es de Armstrong (igual a la suma de sus dígitos elevados a la potencia del número de dígitos).
        
        Args:
            n (int): Número a verificar
            
        Returns:
            bool: True si n es un número de Armstrong, False en caso contrario
        """
        lista=[]
        
        for digito in str(n):
            lista.append(int(digito))
        suma=0
        print(lista)
        for numeros in range(0,len(lista)):
            suma=suma+lista[numeros]**3
            
        if n == suma:
            print("si es numero anmstrong",suma)
        else:
            print("no es numero anmstrong",suma)
             
        
        
        
    
    def es_cuadrado_magico(self, matriz):
        """
        Verifica si una matriz es un cuadrado mágico (suma igual en filas, columnas y diagonales).
        
        Args:
            matriz (list): Lista de listas que representa una matriz cuadrada
            
        Returns:
            bool: True si es un cuadrado mágico, False en caso contrario
        """
        

