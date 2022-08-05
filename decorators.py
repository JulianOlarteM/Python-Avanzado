'''
Cuento tiempo tarda en ejecutar una funcion. 

'''
from datetime import datetime


def execution_time(func):
    def wrapper(*args, **kwargs): # los parametros *args y **kwargs es que no importa la cantidad de argumentos pocionales (*args) o parametros nombrados **kwargs, la funcion los recibira, y
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed  = final_time - initial_time
        print("Pasaron"+" "+ str( time_elapsed.total_seconds())+ " "+"segundos")
    return wrapper

@execution_time
def random_func():              # como es una funcion que no teiene parametros de entrada, la funcion wrapper no necesitaria paramtros de entrada, pero es mejor dejarla estandar para varios tipos de funciones 
    for _ in range (1, 100000000):
        pass

@execution_time
def suma(a: int, b: int )->int:          # si no declaramos en la funcion wrapper los parametros (*arg, **kwards) no los podria leer
    return a + b 

@execution_time
def saludo(nombre = "Cesar"): #esto seria el parametro nombrado. 
    print("Hola "+ nombre)

if __name__ == "__main__":
    random_func()
    suma(5,5)
    saludo("Facundo")


