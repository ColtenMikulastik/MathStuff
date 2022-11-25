
from matplotlib import pyplot as plt


def plot(t_title, t_x_name, t_y_name, list_x, list_y):
    """this will plot from arguments "title", "x_name", "y_name", list_x, list_y """
    plt.title(t_title)
    plt.xlabel(t_x_name)
    plt.ylabel(t_y_name)
    plt.scatter(list_x, list_y)
    plt.show()


def main():
    """this wont do anything rn, but might allow use to call plot with input"""
    title = input("what is the title of the graph? ")
    x_label = input("what is the label for the x axis?: ")
    y_label = input("what is the label for the y axis?: ")
    in_file = input("which file has the csv for the values to graph?: ")


if __name__ == "__main__":
    main()