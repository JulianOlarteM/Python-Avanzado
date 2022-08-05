import time


def fibo_gen2(max: int):

    n1 = 0
    n2 = 1 
    counter = 0 
    while counter <= max:
        if counter == 0 :
            counter += 1 
            yield (n1, counter) 
        elif counter == 1:
            counter += 1
            yield (n2, counter)
        else:
            aux = n1 + n2
            n1 , n2 = n2 , aux
            counter += 1
            yield (aux, counter)

if __name__ == "__main__":
    max = int(input('Ingrese el numero maximo a que quiere realizarle la suseccion fibonacci: '))
    fibonacci = fibo_gen2(max - 1)
    print("(fib, count)")
    for i in fibonacci:
        print(i) 
        time.sleep(0.5)
    



