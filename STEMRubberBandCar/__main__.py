
def calculate_spring_const():
    """ calculates the spring constant value for a rubber band or spring """
    # notify user about the correct units to use
    print("in order for calculations to work, you will have to use correct units")
    print("length in meters, and mass in kilograms.")
    # collect information from the user
    init_x = float(input("what is the length of your rubber band when relaxed? (x_i): "))
    mass_obj = float(input("how heavy is the object used to put rubber band under weight? (m): "))
    fin_x = float(input("what is the length of your rubber band when being pulled by the weight? (x_f): "))
   
    # notify user to wait
    print("calculating...")

    # define gravitational acceleration
    GRAV_ACC = 9.81

    # calculate spring const 
    # k = (mg)/x
    spring_const = (mass_obj * GRAV_ACC) / (fin_x - init_x)
    
    # print results
    print( "The spring constant of your spring is: " + str(spring_const) + " N/m.")



def interface():
    """ prints the interface until they quit """
    # create hte input variable outside of loop scope
    user_in = 0
    while user_in != 'q':
        print("==============RUBBERBAND SPRING CONSTANT CALCULATOR=====================")
        print("options:")
        print("========================================================================")
        print("\"a\"- to start calulating")
        print("\"q\"- to quit program")
        print("========================================================================")
        user_in = input("input here:")
        if user_in == 'q':
            print("you have quit, thank you!")
            print("good bye!")
            break
        elif user_in == 'a':
            print("you have selected to start calculating!")
            # call calculation function
            calculate_spring_const()
        else:
            print("you have selected an option that is not available sorry,")
            print("try again!")



def main():
    interface()


if __name__ == "__main__":
    main()
