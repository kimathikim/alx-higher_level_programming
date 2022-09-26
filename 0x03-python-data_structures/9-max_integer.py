#!/usr/bin/python3
def max_integer(my_list=[]):
    for i in range(len(my_list)):
        if (my_list[i - 1] > my_list[i]):
            temp = my_list[i - 1]
            my_list[i] = temp
            my_list[i - 1] = my_list[i]
    return (my_list[i])
