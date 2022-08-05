'''
Si una cadena de caracteres es un palindromo o no 

'''

def is_palidrome (string:str)-> bool:
    string = string.replace(" ","").lower() #quito espacios y dejo en minusculas. 
    return string == string[::-1] 

def run():
    print(is_palidrome(1000))

if __name__ == '__main__':
    run()

