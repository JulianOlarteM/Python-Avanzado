"""Determina los numero primos
Un numero es primo cuando el residuo de la divicion es 0 solo cuando se 
divide entre uno, y entre el mismo numero. """

def es_primo(numero: int)->bool:
    contador=0
    for i in range (1, numero + 1):
        
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador = contador + 1

    if contador == 0:
        return True
    else:
        return False

def run (): 
    #numero: int = input('Escribe un número: ')
    numero: int = 64
    if es_primo(numero) == True:
        print('Es primo ')
    else:
        print('No es primo')
        

if __name__ == "__main__":
    run()