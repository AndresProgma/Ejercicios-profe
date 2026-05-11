def suma_digitos(n):
        """
        Calcula la suma de los dígitos de un número.
        
        Args:
            n (int): Número para sumar sus dígitos
            
        Returns:
            int: La suma de los dígitos de n
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
             


suma_digitos(0)