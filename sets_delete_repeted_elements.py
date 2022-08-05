def repeted_element_inlist(any_list):
    my_set = set(any_list)

    return my_set


def run():
    list = [1, 1, 2, 2, 3, 4, 5, 6, "hola","hola","mundo"]
    print(repeted_element_inlist(list))


if __name__ == "__main__":
    run()
