#!/usr/bin/python3
"""
Program to show solution to numbered 100 jars problem
"""


import random


MAX = 10   # Change this line to 100 if you are so inclined
HALF = MAX//2


def main():
    """Self contained program. The definition of MAX above will determine
       how many jars/numbers to solve for. The output is obviously more
       easily read with 10.
    """
    random_list = random.sample(range(MAX), MAX)
    series_list = []

    print(random_list)

    # If populate_series_list returns a 1 then it has performed a swap
    # and will be called a second time on the adjusted list. This should
    # never require more than one retry
    if populate_series_list(random_list, series_list):
        populate_series_list(random_list, series_list)

    for i in series_list:
        print(i, len(i))


def populate_series_list(random_list, series_list):
    """Taking the list of randomized numbers (representing the
       number in a jar), and a series_list which can hold
       a list of lists. This will hold the series as they are
       traversed.

       Currently a series is made for every possible starting
       point. It would be more efficient to keep a running
       list of sorted indexes and choose the next starting
       point from the lowest value not in that list. This
       could complete when the result is == MAX. For the small
       scale of the problem scope this seemed like unnecessary
       complexity compared to the small increase in efficiency.

       As a series is traced, its length is calculated. As soon
       as a length is > HALF we have found a series that encompases
       more than HALF of the set. The last and HALF-1 (accounting
       for zero based list) and the last in series indexes are
       swapped. (This is the puzzle one time swap.) A text message
       will be output and a positive value is immediately returned
       from the function.

       If none is found to be too long, no indexes are swapped
       and the series_list is populated. A zero is returned in
       the success case that will indicate that all the series
       are less than HALF long.
    """
    # create a set from 0 to MAX inclusive
    idxset = set(range(MAX+1))

    # start at the bottom, but could be pretty much anywhere
    current = min(idxset)
    # the process will continue until the value is MAX proper
    # the list we are processing goes from 0 to MAX-1
    while current < MAX:
        tmp_list = []
        index = current

        # here is a while that might be better off as a
        # do-while but python doens't have one so there
        # is a following action that mimics doing the
        # action regardless of the while test. This is
        # necessary to get the len(1) chains, and to
        # actually include the last item when the list
        # is calculated
        while random_list[index] != current:
            tmp_list.append(index)
            index = random_list[index]
        tmp_list.append(index)
        index = random_list[index]

        # This if() performs logic that might better be
        # a separate function, leaving just the else()
        # would make this simply return the unmodified
        # chains. However, it is here because at this
        # point the goal is to solve the puzzle and
        # it adds a layer of efficiency.
        if len(tmp_list) > HALF:
            # This is short circuit logic for keeping the chains
            # shorter than HALF the total length

            # setup the values/positions to swap
            dest_index = tmp_list[HALF-1]
            src_index = tmp_list[-1]

            # here is where the swap occurs
            tmp = random_list[dest_index]
            random_list[dest_index] = random_list[src_index]
            random_list[src_index] = tmp

            del series_list[:]
            print("Swapping ", dest_index, " with ", src_index)
            print(random_list)
            return True

        idxset = idxset - set(tmp_list)
        current = min(idxset)
        series_list.append(tmp_list)

    return False


if __name__ == "__main__":
    main()
