# 1. Below The Arithmetical Mean
# When given a list, the program should return a list of all the elements below the original list’s arithmetical mean. The arithmetical mean is the sum of all elements divided by the number of elements.
# Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]

list = [1, 3, 5, 6, 4, 10, 2, 3]


def below_arithmetical_mean(list):

    new_list = []
    avg = sum(list)/len(list)

    for number in list:
        if number < avg:
            new_list.append(number)
    return new_list


print(below_arithmetical_mean(list))


#2. Two Lowest Elements
#When given a list of elements, find the two lowest elements.
#They can be equal to each other or different.
#Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3

lst = [198, 3, 4, 9, 10, 9, 2]


def two_lowest_elements(lst):

    lowest = lst[0]
    lowest2 = None

    for number in lst:
        if number < lowest:
            lowest2 = lowest
            lowest = number
        elif lowest2 is None or lowest2 > number:
            lowest2 = number

    return lowest, lowest2


print(two_lowest_elements(lst))