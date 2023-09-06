

def trapazoid_approx(n_var, func, start_a, stop_b):
    """ using arguments: n, function, a, and b to approximate area under curve """
    # omg just found out that this function exists :^O eval()
    
    accumulate = float(0)

    x_sub_i = list()
    
    delta_x = (stop_b - start_a)/n_var

    # not only do we need to loop evaluating teh functions but we also need to loop our x vars
    for i in range(0, n_var + 1):
        print("xi variable for n=" + str(i) + " is :" + str(start_a + ( i * delta_x)))
        x_sub_i.append(float(start_a + ( i * delta_x)))

    # loop through our new x vaules
    for x in x_sub_i:
        # replace x in the loop with those values
        print(str(eval(func)))
        accumulate = accumulate + eval(func)
    
    # calculate the approximation 
    print(str((delta_x / 2) * accumulate))
    


def main():
    """ this function will drive the trapazoidal approximation function """
    # get the information that you want to approximate
    start_a = int(input("What is your starting pos (a): "))
    stop_b = int(input("What is your stopping pos (b): "))
    func = input("please give your function in some format: ")
    n_var = int(input("please give your n variable (how accurate your approximation is): "))
    # send it to the function
    trapazoid_approx(n_var, func, start_a, stop_b)


if __name__ == "__main__":
    main()
