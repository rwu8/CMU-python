# iterative, but performs much better for large lists
# def merge(A, B):
#     C = []
#     i = j = 0
#
#     while ((i < len(A)) or (j < len(B))):
#         # if list B is completely merged or list A is still incomplete
#         # and item in A is less than item in B:
#         if ((j == len(B)) or ((i < len(A)))
#                         and A[i] <= B[j]):
#             C.append(A[i])
#             i += 1
#         else:
#             C.append(B[j])
#             j += 1
#
#     return C

def merge(A, B):
    if len(A) == 0:
        return A
    if len(B) == 0:
        return B
    if A[0] < B[0]:
        return [A[0]] + merge(A[1:], B)
    else:
        return [B[0]] + merge(A, B[1:])

def mergesort(L):
    # a list of size 0 or 1 is already sorted
    if len(L) < 2:
        return L
    else:
        mid = len(L) // 2
        left = mergesort(L[:mid])
        right = mergesort(L[mid:])
        return merge(left, right)

print(mergesort([1,5,3,4,2,0]))