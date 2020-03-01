# returns a list of all subsets of the list l
def powerset(l, depth = 0):
    print('  ' * depth + 'powerset(', l, ')')
    if len(l) == 0:
        return [[]]
    else:
        allSubsets = []
        for subset in powerset(l[1:], depth + 1):
            print('  ' * depth + "-->", subset)
            allSubsets += [subset]
            allSubsets += [[l[0]] + subset]
            print('  ' * depth + "-->", 'allSubsets: ', allSubsets)
        return allSubsets

def main():
    print(powerset([1,2,3]))

if __name__ == '__main__':
    main()