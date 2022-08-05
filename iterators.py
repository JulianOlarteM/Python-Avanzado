'''
Suseccion fibonacci
'''
import time 
 
class FiboIter():

    def __init__(self) -> None:
        pass

    def __iter__(self):
        self.num1= 0 
        self.num2= 1 
        self.counter = 0 

        return self 

    def __next__(self) -> None:
        if self.counter == 0: 
            self.counter += 1 
            return self.num1
        elif self.counter == 1:
            self.counter += 1 
            return self.num2
        else:
            self.aux = self.num1 + self.num2
            #self.num1 = self.num2
            #self.num2 = self.aux
            self.num1, self.num2 = self.num2, self.aux
            self.counter += 1
            return self.aux



if __name__ == "__main__":
    fibonacci = FiboIter()
    for element in fibonacci:
        print(element)
        time.sleep(0.05) # para que los datos se vean con un espacio entre si. 

            



