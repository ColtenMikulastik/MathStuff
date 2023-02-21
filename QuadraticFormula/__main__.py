
import math

def calculate_quadratic(a_var, b_var, c_var):
    """calculates the roots for a quadratic formula"""

    # print all teh values that are input into the function
    print("a: " + a_var) 
    print("b: " + b_var) 
    print("c: " + c_var) 
    
    # make them numbers and not strings
    a_var = float(a_var)
    b_var = float(b_var)
    c_var = float(c_var)
    # start by squaring the b variable, and calc info inside the sqrt
    sqrt_prt = ((b_var ** 2) - (4 * a_var * c_var))
    # turn the outside b negative
    hanging_b =(b_var * -1)
    # calc denominator
    denom = 2 * a_var
   
    # create the imaginary number string
    img = ""

    # I wanna make this give two real numbers if there are no imageinary 
    # if the sqrt is of a negative, set the img string
    if sqrt_prt < 0:
        sqrt_prt = sqrt_prt * -1
        img = "i" 
        # print the answer in an interesting way
        print( "x= " + str(hanging_b) + " +- " + str(math.sqrt(sqrt_prt)) + " " + img +  " / " + str(denom))



def main():
   
    quit = False
    while not(quit):
        print("======Quadriatic Calc=====")
        user_in = input("Would you like to calculate?")
        if user_in == 'y':
            # call the quadriatic calc function
            var_a = input("what is your 'a' value?: ")
            var_b = input("what is your 'a' value?: ")
            var_c =input("what is your 'a' value?: ")
            calculate_quadratic(var_a, var_b, var_c)
        else:
            quit = True


if __name__ == "__main__":
    main()
