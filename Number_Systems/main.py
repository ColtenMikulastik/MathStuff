
def convert_from_decimal():



def convert_to_dec( base, word ):
    """ Convert from a given base number system to decimal """
    # base should be an int, and work should be a list of numbers
    sum = 0
    invert = 0
    for i in range((len(word) - 1), -1, -1):
        radix = base**invert
        digit = word[i]
        sum = sum + (radix * digit)
        invert = invert + 1

    print(sum)
    return sum


def main():
    print("hello")
    print("passing to the convert to dec function")
    
    thing1 = [ 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1 ]
    thing2 = [ 3, 2, 0 ]
    convert_to_dec(4, thing2)


    return 0


if __name__ == "__main__":
    main()
