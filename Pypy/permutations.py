#!/usr/bin/python3

from itertools import permutations

def main():
    arr = [int(a) for a in input("Enter the Array here: ").split()]
    n = len(arr)
    print("Permutations Using Backtracking :")
    backtrack(arr)
    print('Permutations Using the iteratools')
    permute(arr)

def permute(arr):
    perm = list(permutations(arr))
    for a in perm:
        print(a)

def backtrack(arr,cur=[]):
    if(len(cur) == len(arr)):
        print(cur);
    else:
        for a in arr:
            if a not in cur:
                cur.append(a)
                backtrack(arr)
                cur.pop()




if __name__ == "__main__":
    main()
