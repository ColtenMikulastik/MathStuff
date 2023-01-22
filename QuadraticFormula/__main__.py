
import math

def calculate_quadratic(a_var, b_var, c_var):
    """calculates the roots for a quadratic formula"""

    # print all teh values that are input into the function
    print("a: " + str(a_var)) 
    print("b: " + str(b_var)) 
    print("c: " + str(c_var)) 
    
    # start by squaring the b variable, and calc info inside the sqrt
    sqrt_prt = ((b_var ** 2) - (4 * a_var * c_var))
    # turn the outside b negative
    hanging_b =(b_var * -1)
    # calc denominator
    denom = 2 * a_var
   
    # create the imaginary number string
    img = ""

    # if the sqrt is of a negative, set the img string
    if sqrt_prt < 0:
        sqrt_prt = sqrt_prt * -1
        img = "i"
    
    # print the answer in an interesting way
    print( "x= " + str(hanging_b) + " +- " + str(math.sqrt(sqrt_prt)) + " " + img +  " / " + str(denom))



def main():
    # call the main function
    calculate_quadratic(1,2,3)


if __name__ == "__main__":
    main()
