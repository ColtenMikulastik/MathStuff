
def hyphenate(l_binary_num, r_binary_num, data_size):
    """ returns a str with hyphen where delta is """
    return_me = list()
    for i in range(0, data_size):
        if l_binary_num[i] != r_binary_num[i]:
            return_me.append("-")
        else:
            return_me.append(r_binary_num[i])

    return return_me


def is_one_off(l_binary_num, r_binary_num, data_size):
    """ returns if the difference between two binary numbers is only 1 """
    delta_counter = 0
    for i in range(0, data_size):
        if l_binary_num[i] != r_binary_num[i]:
            delta_counter += 1
        else:
            pass
    if delta_counter == 1:
        # success
        return 1
    else:
        return 0


def one_amount(binary_num):
    """ returns number of ones """
    counter = int()
    for i in binary_num:
        if i == '1':
            counter += 1
        else:
            pass
    return counter


def qmmethod(in_list, data_size):
    bin_list = list()
    for i in in_list:
        i = bin(i)[2:].zfill(data_size)
        print(i)
        bin_list.append(i)
    groups = list(list())

    for i in range(0, data_size):
        temp_list = list()
        for j in bin_list:
            if one_amount(j) == i:
                temp_list.append(j)
        groups.append(temp_list)
    print(groups)

    group_combinations = list(list())
    i = 0
    while i < (len(groups) - 1):
        temp_list = list()
        for j in groups[i]:
            for k in groups[i + 1]:
                if is_one_off(j, k, data_size):
                    temp_list.append(hyphenate(j, k, data_size))
        group_combinations.append(temp_list)
        i += 1

    counter = 0
    for i in group_combinations:
        print(str(counter) + ", " + str(counter + 1))
        for j in i:
            print(j)
        print("================")
        counter += 1


def main():
    minterms = [0, 2, 6, 7, 8, 10, 11, 12, 13, 14, 16, 18, 19, 29, 30]
    dont_cares = [4, 9, 21]
    minterms = minterms + dont_cares
    minterms.sort()
    qmmethod(minterms, 5)
    print(is_one_off("011", "110", 3))


if __name__ == "__main__":
    main()
