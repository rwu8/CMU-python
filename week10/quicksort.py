def quicksort(L):
    if len(L) < 2:
        return L
    else:
        pivot = L[0]
        rest = L[1:]
        lo = [elem for elem in rest if elem < pivot]
        hi = [elem for elem in rest if elem >= pivot]
        return quicksort(lo) + [pivot] + quicksort(hi)


print(quicksort([9,3,9,7,3,1,5,8,0]))