#!/usr/bin/python3
"""A module containing instruments for manipulating pascal triangles.
"""


def pascal_triangle(n):
    """
    A function to return a lists of lists for a
    pascal triangle based on the number given to it.
    """
    psl_trg = [[1]]
    if (n <= 0):
        return []
    for i in range(n):
        tmp_list = [1]
        prev_item = 1
        for idx, item in enumerate(psl_trg[i]):
            if len(psl_trg[i]) == 1:
                # if we have only 1 element in the main list,
                # we need not do anything in this loop
                break
            if idx == 0:
                # We don't want to touch the first element
                # of the inner list which will always be 1
                continue
            tmp_list.append(prev_item + item)
            prev_item = item
        tmp_list.append(1)
        psl_trg.append(tmp_list)
    return psl_trg
