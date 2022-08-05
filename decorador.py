def decorador(func):
    def envoltura():
        func()
        print('Esto se añade a mi funcion original')
        
    return envoltura

def saludos():
    print('Hola')

def main ():
    saludo = decorador(saludos)
    saludo()


if __name__ == "__main__":
    main()
       