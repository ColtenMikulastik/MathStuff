# Colten (Luca) Vance Mikulastik
import math

def calc_pi(sides):
    """ calls inside and outside shape functions """
    inside_shape(sides)
    outside_shape(sides)


def outside_shape(sides):
    """ calculuates area of the shape with sides outside circle """
    # represents the inside angle  
    theta = 360 / (sides * 2)

    # first leg is radius, and second leg is tangent so 1 * tangent
    rec_area = math.tan((theta * math.pi) / 180)

    # print output
    print("pi is less than: " + str(rec_area * sides))
    


def inside_shape(sides):
    """ calculates area, for a given amount of sides of an inscribed shape """
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
    rec_area = leg_one * leg_two
    
    print("pi is at least: " + str(rec_area * sides))


def main():
    """ drives function with gui """
    sides = input("please give \'n\' for a \'n\'-sided shape:") 
    calc_pi(int(sides))



if __name__ == "__main__":
    main()

