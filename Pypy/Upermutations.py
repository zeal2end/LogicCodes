
from copy import copy
from itertools import permutations

def Upermutations(mset,i=0):
    ans = set([a for a in permutations(mset)])
    print(len(ans))
    for a in ans:
        print(a)


def main():
    mset = [int(a) for a in input().split()]
    Upermutations(mset)


if __name__ == "__main__":
    main()
