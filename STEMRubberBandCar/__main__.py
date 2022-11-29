from graphing.__main__ import *
# import my graphing functions to allow graphing

# Global Variables
x_variables = []
y_variables = []


def graph_current_buffer():
    """ sends the buffered information to the plot function """
    # set variables for the plot function
    elas_title = "Elastic Variables"
    elas_subtitle_m = "Change in Length (in)"
    elas_subtitle_d = "Mass (oz)"

    # plot data from the buffer
    plot(elas_title, elas_subtitle_m,  elas_subtitle_d, x_variables, y_variables)


def calculate_elastic_energy(spring_const, init_x, fin_x, spring_const_known=False):
    """ calculates the current elastic energy of the rubber band """
    # don't really have to worry about formating this input
    if spring_const_known:
        # if teh spring constant is known then all we have to do is calculate
        print("calculating elastic energy")
    else:
        print("spring constant and delta x of your rubber band isn't known please input the following")
        print("unit information for this calculation: length in meters, spring constant in N/m")
        # gonna do this later
    
    # calculate the elastic potential energy
    # U=(1/2) k (d_x)^2
    elastic_potential_energy = (1/2) * spring_const * ((fin_x - init_x)**2)
    print("The elastic potential energy in current system is: " + str(elastic_potential_energy) + " Joules")


def calculate_spring_const():
    """ calculates the spring constant value for a rubber band or spring """
    # notify user about the correct units to use
    print("in order for calculations to work, you will have to use correct units")
    print("length in inches, and mass in ounces.")
    # collect information from the user
    init_x = float(input("what is the length of your rubber band when relaxed? (x_i): "))
    mass_obj = float(input("how heavy is the object used to put rubber band under weight? (m): "))
    fin_x = float(input("what is the length of your rubber band when being pulled by the weight? (x_f): "))
   
    # notify user to wait
    print("calculating...")

    # consts go here
    # define gravitational acceleration
    GRAV_ACC = 9.81
    # ounces to kg goes here
    CONV_OZ_TO_KG = 0.02834952
    # inches to meters goes here
    CONV_IN_TO_M = 0.0254

    # add results to the lists "buffer"
    x_variables.append(int(fin_x - init_x))
    y_variables.append(int(mass_obj))

    # convert numbers given by the user
    init_x = init_x * CONV_IN_TO_M
    fin_x = fin_x * CONV_IN_TO_M
    mass_obj = mass_obj * CONV_OZ_TO_KG

    # calculate spring const 
    # k = (mg)/x
    spring_const = (mass_obj * GRAV_ACC) / (fin_x - init_x)

    # print results
    print("The spring constant of your spring is: " + str(spring_const) + " N/m.")
    
    # calculate the elastic energy now
    calculate_elastic_energy(spring_const, init_x, fin_x, True)


def interface():
    """ prints the interface until they quit """
    # create the x and y variable buffer

    # create hte input variable outside of loop scope
    user_in = 0
    while user_in != 'q':
        print("==============RUBBERBAND SPRING CONSTANT CALCULATOR=====================")
        print("options:")
        print("========================================================================")
        print("\"a\"- to start calculating")
        print("\"q\"- to quit program")
        print("\"w\"- to write current data in buffer to csv file")
        print("\"c\"- to clear the buffer")
        print("\"p\"- to print current buffer")
        print("\"r\"- to read csv file to current buffer (overwrites)")
        print("\"g\"- to begin graphing mode (note: requires csv file)")
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
        elif user_in == 'w':
            print("writing your current buffer into a csv file...")
            print("what would you like to call the csv file?")
            name = input("name: ")
            write_csv_file(name, x_variables, y_variables)
            # call the csv write function
        elif user_in == 'c':
            print("clearing the current buffer...")
            # make the x and y variable list empty
            x_variables.clear()
            y_variables.clear()
        elif user_in == 'p':
            print("the current buffer is:")
            # print out the contents of the two lists
            print(str(x_variables))
            print(str(y_variables))
        elif user_in == 'g':
            print("you have selected to graph the data in the buffer")
            graph_current_buffer()
            # call the graphing function
        elif user_in == 'r':
            # ask user what file to read from
            print("please give the name of the file that you would like to read from.")
            file_n = input("name: ")
            # make sure to clear the lists before adding to them
            x_variables.clear()
            y_variables.clear()
            # call the read csv file function
            read_csv_file(file_n, x_variables, y_variables)
        else:
            print("you have selected an option that is not available sorry,")
            print("try again!")


def main():
    interface()


if __name__ == "__main__":
    main()
