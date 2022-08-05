import time
class FiboIterwvalue ():
    def __init__(self, max = None):
        self.max = max 

    def __iter__(self):
        self.num1 = 0
        self.num2 = 1
        self.contador = 0
        return self
    
    def __next__(self):
        if not self.max or self.contador <= self.max:
            if self.contador == 0:
                self.contador += 1 
                return self.num1

            elif self.contador == 1:
                self.contador += 1 
                return self.num2
            
            else: 
                self.sum = self.num1 + self.num2
                self.num1, self.num2 = self.num2, self.sum
                self.contador += 1
                return self.sum
        else:
            raise StopIteration


if __name__ == "__main__":
    max = int(input("Ingresa el numero maximo para encontrar la suseccion fibonacci:  "))
    fibonacci = FiboIterwvalue(max-1)
    for element in fibonacci:
        print(element, fibonacci.contador)
        time.sleep(0.5)