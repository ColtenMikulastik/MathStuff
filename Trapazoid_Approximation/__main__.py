

def trapazoid_approx(n_var, func):
    """ using your n and func to calculate a trapazoid approximation """
    # get the information that you want to approximate
    start_a = int(input("What is your starting pos (a): "))
    stop_b = int(input("What is your stopping pos (b): "))
    # omg just found out that this function exists :^O eval()

    # loop from a to b, with i
    for x in range(start_a, stop_b + 1):
        # replace x in the loop with those values
        print(str(eval(func)))
    


def main():
    """ this function will drive the trapazoidal approximation function """
    print("test")
    func = input("please give your function in some format: ")
    n_var = input("please give your n variable (how accurate your approximation is): ")
    trapazoid_approx(n_var, func)


if __name__ == "__main__":
    main()
