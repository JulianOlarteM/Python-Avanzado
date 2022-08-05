'''
hola 3 --> holaholahola
facundo 2 --> facundofacundo
platzi 4 --> PlatziPlatziPlatzi

'''

def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Solo puedes utilizar cadenas"
        return string*n
    
    return repeater

def main():
    repeat_5= make_repeater_of(5)
    repeat_10=make_repeater_of(10)

    print(repeat_5("Hola"))
    print(repeat_10("Facundo"))

if __name__ == "__main__":
    main()