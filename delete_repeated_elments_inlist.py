"""
Este programa elimina los elementos repetidos de cualquier lista. 
"""

def  repeated_elements_list(any_list):
    a = []
    for element in any_list:
        if element not in a:
            a.append(element)
    return a

def run():
    list = [1, 1, 2, 2, 3, 4, 5, 6, "hola","hola","mundo"]
    print(repeated_elements_list(list))


if __name__ == "__main__":
    run()