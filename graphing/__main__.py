
from matplotlib import pyplot as plt
import csv


def write_csv_file(output_file, x_values, y_values):
    """writes x and y values from two lists to a csv file"""
    # will create the file if not already exist, and will write over existing data
    # open file and begin context handler
    with open(output_file, 'w', newline='') as csvfile:
        csv_write = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in range(len(x_values)):
            csv_write.writerow([x_values[row], y_values[row]])


def read_csv_file(input_file, x_values, y_values):
    """reads the input_file for the "x, y" in a comma seperated list file"""
    # open the file to be read from, setting newline as nothing
    with open(input_file, newline='') as csvfile:
        # create list with the correct delimiters
        csv_read = csv.reader(csvfile, delimiter=',', quotechar='|')
        # loop through the rows and copy the variables into the lists passed to the function via the arguments
        for row in csv_read:
            x_values.append(row[0])
            y_values.append(row[1])


def plot(t_title, t_x_name, t_y_name, list_x, list_y):
    """this will plot from arguments "title", "x_name", "y_name", list_x, list_y """
    plt.title(t_title)
    plt.xlabel(t_x_name)
    plt.ylabel(t_y_name)
    plt.plot(list_x, list_y)
    plt.show()


def main():
    """this allows the user to call plot with input from cmd line"""

    # ask for information that will be used in the graphing
    title = input("what is the title of the graph? ")
    x_label = input("what is the label for the x axis?: ")
    y_label = input("what is the label for the y axis?: ")
    in_file = input("which file has the csv for the values to graph?: ")

    # create the lists to store the x and y values early
    list_x = []
    list_y = []

    # use function to read the file
    read_csv_file(in_file, list_x, list_y)

    # for now print the results
    print(str(list_x))
    print(str(list_y))

    # call the plot function
    plot(title, x_label, y_label, list_x, list_y)


if __name__ == "__main__":
    main()
