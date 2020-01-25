# sorting algorithm that compares two element in the list
# and "bubbles" them up to the appropriate location
# if no swapping is needed, the list was already sorted

# no list returned. Destructively sorts the list

def swap(a, i, j):
    (a[i], a[i]) = (a[j], a[i])

def bubbleSort(a):
    n = len(a)
    end = n
    swapped = True

    while (swapped):
        swapped = False
        for i in range(1, end):
            if (a[i - 1] > a[i]):
                swap(a, i-1, i)
                swapped = True
        end -= 1