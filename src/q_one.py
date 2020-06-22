"""Question 1"""

from math import floor


# linear search algorithm
def linear_search_alg(list_to_traverse, el):
    # loop through list
    for i in range(len(list_to_traverse)):
        # compare each element to the item of interest
        if list_to_traverse[i] == el:
            # return result if item is in list
            return print("Linear Search Alg found", el, "at position", i)
    #  otherwise, send response
    raise Exception("Could not find" + str(el) + " in this list")


def binary_search_alg(list_to_traverse, el):
    size_of_list = len(list_to_traverse)  #
    left = 0
    right = size_of_list - 1

    while left <= right:
        mid = floor((left + right) / 2)
        if list_to_traverse[mid] < el:
            left = mid + 1
        elif list_to_traverse[mid] > el:
            right = mid - 1
        else:
            return print("Binary Search Alg found", el, "at position", mid)
    raise Exception("Could not find" + str(el) + " in this list")


# todo: uncomment this to test result
if __name__ == '__main__':
    custom_list = [1, 2, 3, 4, 7, 9, 12, 14, 18, 9]
    print("List of interest ->", custom_list)
    linear_search_alg(custom_list, 9)
    binary_search_alg(custom_list, 9)
