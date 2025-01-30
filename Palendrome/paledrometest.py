


def palendrome():
    """ largest palidrome made from the product of two 3-digit numbers """
    # think this might be a bad way to solve but brute force
    # need every possible combination of two three digit numbers
    list_o_nums = list()
    for i in range(100, 999):
        for j in range(100, 999):
            if (is_same_backwards(str(i * j))):
                print(i * j)
                list_o_nums.append(i * j)
            # need to check if the answer is same forward and back

    list_o_nums.sort()
    print(list_o_nums)



def is_same_backwards(in_str):
    """ takes an input string and returns true if it is a palendrome """
    i = len(in_str) - 1
    # loop through the string and return false if any don't match
    for j in in_str:
        # if they are not equal return false
        if in_str[i] != j:
            return False
        # step the inverse iterator
        i = i -1

    # if the function gets here then return true
    return True


def main():
    palendrome()




if __name__ == "__main__":
    main()
