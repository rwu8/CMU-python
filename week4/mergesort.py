# sorting algorithm that selects the largest (or smallest) element in the list
# and places it in the appropriate location

def merge(a , start1, start2, end):
    index1 = start1
    index2 = start2
    length = end - start1
    aux = [None] * length

    for i in range(length):
        # case 1: first list is already sorted, and we just need to
        # append the second list
        # case 2: we are still merging the 2 lists, and index2 is
        # less than index 1

        if ((index1 == start2) or
                ((index2 != end) and (a[index1] > a[index2]))):
            aux[i] = a[index2]
            index2 += 1
        else:
            aux[i] = a[index1]
            index1 += 1

    # destructively modify our 'a' list with the aux list
    for i in range(start1, end):
        a[i] = aux[i - start1]

def mergeSort(a):
    n = len(a)
    step = 1 # tracks the size of the list we are merging together
    while step < n:
        # merge the list in place
        for start1 in range(0, n, 2*step):
            # min used for odd cases to prevent index error
            start2 = min(start1 + step, n)
            end = min(start1 + 2*step, n)
            merge(a, start1, start2, end)
        step *= 2