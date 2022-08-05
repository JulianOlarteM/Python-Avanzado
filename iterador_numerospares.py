class EvenNumbers:
    '''
    Esta clase implementa un iterador de todos los
    numeros pares  desde 0 hasta un maximo valor. 
    '''

    def __init__(self, max=None): #lo que necesitamos del usuario es el nuemro maximo a llegar
        self.max = max
    
    def __iter__(self):  #solo nececstio cada numero de cada iteracion, este froma permite almacenar mi dato y retornarlo asi mismo,  y tenerlo dispobile para despues.
        self.num = 0 
        return self
    
    def __next__(self): #Me permite extraer cada auno de los elementos de mi itrador, en este caso los numeros pares.
        if not self.max or self.num <= self.max: #si no existe self.max o no se me paso valor maximo como parametro, o el numero que estoy recorriendo  es menor o igual al maximo
            result = self.num 
            self.num += 2 
            return result
        else:
            raise StopIteration