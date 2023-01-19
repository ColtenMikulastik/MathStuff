
import math

def calculate_quadratic(a_var, b_var, c_var):
    """calculates the roots for a quadratic formula"""

    # print all teh values that are input into the function
    print("a: " + str(a_var)) 
    print("b: " + str(b_var)) 
    print("c: " + str(c_var)) 

    sqrt_prt = ((b_var ** 2) - (4 * a_var * c_var))
    hanging_b =(b_var * -1)
    denom = 2 * a_var
   
    img = ""

    if sqrt_prt < 0:
        sqrt_prt = sqrt_prt * -1
        img = "i"
    
    print( "x= " + str(hanging_b) + " +- " + str(math.sqrt(sqrt_prt)) + " " + img +  " / " + str(denom))



def main():
    print( "hello!")
    calculate_quadratic(1,2,3)


if __name__ == "__main__":
    main()
