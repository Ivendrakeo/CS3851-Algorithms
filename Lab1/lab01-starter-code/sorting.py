def insertion_sort(lst):
    """
    Sorts the list lst in place using insertion_sort.
    """
    for j in range(1, len(lst)):
        key = lst[j]
        # shift elements in sorted sequence
        i = j-1
        while i>=0 and lst[i] > key:
            lst[i+1] = lst[i]
            i = i-1
        # inset lst[j] into the sorted sequence
        lst[i+1] = key