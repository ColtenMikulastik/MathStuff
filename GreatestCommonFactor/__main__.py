# Colten (Luca) Vance Mikulastik
# 1/11/2023


def find_gcf(first_number, second_number):
    """ this is a function that will find the greatest common factor (denominator) between two numbers """

    # check and make sure that the first number is the largest
    if first_number > second_number:
        pass
    elif second_number > first_number:
        # just swap the two numbers
        temp = second_number
        second_number = first_number
        first_number = temp
    else:
        # if the two numbers are the same value or etc return first num
        return first_number

    # loop doing euclideans algorythm
    while second_number != 0:
        # then first number will be divided into first
        # first get remainder of division
        remainder = first_number % second_number
        # then get actual quotient rounded to nearest int
        quotient = round(first_number / second_number)
    
        # the second number becomes the first number
        first_number = second_number
        # the remainder becomes the second number
        second_number = remainder

    # return the result
    return first_number


def main():
    # get numbers
    first_number = int(input("What is your first number?"))
    second_number = int(input("what is your second number?"))
    gcf = find_gcf(first_number, second_number)
    print(str(gcf))


if __name__ == "__main__":
    main()
