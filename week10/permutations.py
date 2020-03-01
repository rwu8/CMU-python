# returns a list of all permutations of the list l
def permutations(l, depth=0):
    print('  ' * depth + 'permutations(', l, ')')

    if len(l) == 0:
        return [[]]
    else:
        allPerms = []
        for subPermutation in permutations(l[1:], depth+1):
            print('  ' * depth + "-->", 'subPerm:', subPermutation)
            for i in range(len(subPermutation)+1):
                allPerms += [subPermutation[:i] + [l[0]] + subPermutation[i:]]
                print('  ' * depth + "-->", 'allPerms', allPerms)

        return allPerms

def main():
    print(permutations([1,2]))


if __name__ == '__main__':
    main()