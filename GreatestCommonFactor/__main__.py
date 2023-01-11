# Colten (Luca) Vance Mikulastik
# 1/11/2023


def find_gcf(first_number, second_number):
    """ this is a function that will find the greatest common factor (denominator) between two numbers """
    if first_number > second_number:
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

    elif second_number > first_number:
        # second number will be divided into first
        pass

    return second_number


def main():
    # get numbers
    first_number = input("What is your first number?")
    second_number = input("what is your second number?")
    find_gcf(first_number, second_number)



if __name__ == "__main__":
    main()
