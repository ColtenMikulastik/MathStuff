# Colten (Luca) Vance Mikulastik
import math


def calc_pi(sides):
    """ calculates pie, for a given amount of sides of an inscribed shape """
    print("for " + str(sides) + " sides")

    # theta represtents the inside angle
    theta = 360 / (sides * 2)
    print("theta: " + str(theta))
    # then I need to calculate the legs of the triangle
    # sin function takes in radians, so....
    leg_one = math.sin((theta * math.pi) / 180)
    print("leg_one: " + str(leg_one))

    leg_two = math.cos((theta * math.pi) / 180)
    print("leg_two: " + str(leg_two))
    
    # calculuate the area of the rectangle for each side
    rectangle_area = leg_one * leg_two
    
    print("pi is at least: " + str(rectangle_area * sides))


def main():
    """ drives function with gui """
    calc_pi(1000)



if __name__ == "__main__":
    main()

