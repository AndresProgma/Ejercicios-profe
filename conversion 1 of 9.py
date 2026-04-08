class Conversion:
    def celsius_a_fahrenheit(self, celsius):
        farenheit= (celsius * 9/5)+32
        return farenheit



        """
        Convierte temperatura de Celsius a Fahrenheit.
        celsius
        Args:
            celsius (float): Temperatura en grados Celsius
            
        Returns:
            float: Temperatura en grados Fahrenheit
            
        Fórmula: F = (C × 9/5) + 32
        
        Ejemplo:
            celsius_a_fahrenheit(0) -> 32.0
            celsius_a_fahrenheit(100) -> 212.0
        """
        
    
    def fahrenheit_a_celsius(self, fahrenheit):
        celsiuss= (fahrenheit -32)*5/9
        return celsiuss
        """
        Convierte temperatura de Fahrenheit a Celsius.
        
        Args:
            fahrenheit (float): Temperatura en grados Fahrenheit
            
        Returns:
            float: Temperatura en grados Celsius
            
        Fórmula: C = (F - 32) × 5/9
        
        Ejemplo:
            fahrenheit_a_celsius(32) -> 0.0
            fahrenheit_a_celsius(212) -> 100.0
        """
        
    
    def metros_a_pies(self, metros):
        pies= metros* 3.28084
        return pies
        """
        Convierte distancia de metros a pies.
        
        Args:
            metros (float): Distancia en metros
            
        Returns:
            float: Distancia en pies
            
        Factor: 1 metro = 3.28084 pies
        
        Ejemplo:
            metros_a_pies(1) -> 3.28084
        """
        
    
    def pies_a_metros(self, pies):
        metros= pies*0.3048
        return metros
        """
        Convierte distancia de pies a metros.
        
        Args:
            pies (float): Distancia en pies
            
        Returns:
            float: Distancia en metros
            
        Factor: 1 pie = 0.3048 metros
        
        Ejemplo:
            pies_a_metros(3.28084) -> 1.0
        """
        
    
    def decimal_a_binario(self, decimal):
        Binario=bin(decimal)
        return Binario
        """
        Convierte un número decimal a su representación binaria.
        
        Args:
            decimal (int): Número decimal (positivo)
            
        Returns:
            str: Representación binaria como string
            
        Ejemplo:
            decimal_a_binario(10) -> "1010"
            decimal_a_binario(255) -> "11111111"
        """
        
    def binario_a_decimal(self, binario):
        """
        Convierte un número binario a decimal.
        
        Args:
            binario (str): Representación binaria como string
            
        Returns:
            int: Número decimal
            
        Ejemplo:
            binario_a_decimal("1010") -> 10
            binario_a_decimal("11111111") -> 255
        """

        decimal = int(binario, 2)
        return decimal
        
    
    def decimal_a_romano(self, numero):
        Diccionario_Romano = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
           
        Diccionario_numeros=[1,4,5,9,10,40,50,90,100,400,500,900,1000]

        numero1= ""
        
        for i in range(len(Diccionario_numeros)-1,-1,-1):
            while numero >= Diccionario_numeros[i]:
                numero1= numero1+ Diccionario_Romano[i]
                numero=numero-Diccionario_numeros[i]

               
        """
        Convierte un número decimal a numeración romana.
        
        Args:
            numero (int): Número decimal entre 1 y 3999
            
        Returns:
            str: Número romano
            
        Ejemplo:
            decimal_a_romano(9) -> "IX"
            decimal_a_romano(1994) -> "MCMXCIV"
        """
        
    
    def romano_a_decimal(self,romano):
        Diccionario_Romano = ["I","V","X","L","C","D","M"]
        Diccionario_numeros = [1,5,10,50,100,500,1000]

        total = 0
        anterior = 0

        for i in range(len(romano)-1, -1, -1):
            
            
            for j in range(len(Diccionario_Romano)):
                if romano[i] == Diccionario_Romano[j]:
                    valor = Diccionario_numeros[j]

            
            if valor < anterior:
                total -= valor
            else:
                total += valor

            anterior = valor

        return total

                
            
        
        """
        Convierte un número romano a decimal.
            
        Args:
        romano (str): Número romano válido
                
        Returns:
        int: Número decimal
                
        Ejemplo:
        romano_a_decimal("IX") -> 9
        romano_a_decimal("MCMXCIV") -> 1994
    """
      
    
    def texto_a_morse(self,texto):
        morse = {
            'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
            'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
            'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
            'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
            'Q': '--.-',  'R': '.-.',   'S': '...',
            'T': '-',     'U': '..-',   'V': '...-',  'W': '.--',
            'X': '-..-',  'Y': '-.--',  'Z': '--..',
            '0': '-----', '1': '.----', '2': '..---',
            '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...',
            '8': '---..', '9': '----.'
        }

        for i in range(len(texto)):
            letra=texto[i].upper()
            return (morse[letra])

        

        """
        Convierte texto a código Morse.
        
        Args:
            texto (str): Texto a convertir (letras y números)
            
        Returns:
            str: Código Morse separado por espacios
            
        Ejemplo:
            texto_a_morse("SOS") -> "... --- ..."
            texto_a_morse("HELLO") -> ".... . .-.. .-.. ---"
        """
        
    
    def morse_a_texto(self,morse):
    



        diccionario = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
        '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
        '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
        '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
        '--.-': 'Q', '.-.': 'R', '...': 'S',
        '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W',
        '-..-': 'X', '-.--': 'Y', '--..': 'Z',
        '-----': '0', '.----': '1', '..---': '2',
        '...--': '3', '....-': '4', '.....': '5',
        '-....': '6', '--...': '7',
        '---..': '8', '----.': '9'
    }
        texto_preparado=""
        lista_separada=[]
        
        texto=""
        for i in range(len(morse)):
            if morse[i] != " ":
                 
                 
                texto_preparado= texto_preparado + morse[i]
            if morse[i] == " ":
                lista_separada.append(texto_preparado)
                texto_preparado=""
            
        if texto_preparado != "":
            lista_separada.append(texto_preparado)


        for j in range(len(lista_separada)):
            conversion=lista_separada[j]
            texto= texto + diccionario[conversion]
             


        return texto

        

    """
    Convierte código Morse a texto.
        
    Args:
    morse (str): Código Morse separado por espacios
            
    Returns:
    str: Texto decodificado
            
    Ejemplo:
    morse_a_texto("... --- ...") -> "SOS"
    morse_a_texto(".... . .-.. .-.. ---") -> "HELLO"
    """
    