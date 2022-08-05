

def decorador(func):
    def tipo_funcion(*args,**kwargs):
     
        if  (type(args[0]) == int) and (type(args[1]) == int):
            print("Es una funcion con parametros de entrada de enteros. ") 

        if (type(args[0]) == str) and (type(args[1]) == str):  
            print("Es una funcion con parametros de entrada de strings. ") 

        if ((type(args[0]) == str) and (type(args[1]) == int)) or ((type(args[0]) == int) and (type(args[1]) == str)):  
            print("Es una funcion con parametros de entrada de combinadas en string y enteros. ")
        
        else:
            pass
                    
    return  tipo_funcion

@decorador
def numericos(a: int, b: str)  :
    return a + b
@decorador
def cadenas(a: str, b: str) -> str :
    return a + b

@decorador
def combinado(a, b):
    return a*b
    
if __name__ == '__main__':
    numericos(2,3)
    cadenas("Hola", "Como estas")
    combinado("ja", 2)
    combinado(2, "ja")
