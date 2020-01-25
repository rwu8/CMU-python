# sorting algorithm that selects the largest (or smallest) element in the list
# and places it in the appropriate location

def swap(a, i, j):
    (a[i], a[i]) = (a[j], a[i])

def selectionsort(a):
    n = len(a)

    for i in range(n):
        minIndex = i
        for j in range(i + 1, n):
            if (a[j] < a[i]):
                minIndex = j
        swap(a, i, minIndex)
