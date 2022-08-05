'''
Esta funcion retornara el retorno de la division de X entre un numero n. 
'''
def make_division_by(n):
    assert type(n) == int, "Solo puedes utilizar numeros"
    def num_to_divite(x):
        assert type(x) == int, "Solo puedes utilizar numeros enteros"
        return x/n
    
    return num_to_divite


def main():
    div_4 = make_division_by(4)
    div_2 = make_division_by(2)
    div_8 = make_division_by(8)

    print(div_4(400))
    print(div_2(1))
    print(div_8(160))

if __name__ == "__main__":
    main()