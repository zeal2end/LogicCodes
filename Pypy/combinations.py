from itertools import combinations

def backtrack(arr,i,n,cur=[]):
    if i==n:
        print(cur)
    else:
        backtrack(arr,i+1,n,cur);
        cur.append(arr[i])
        backtrack(arr,i+1,n,cur)
        cur.pop()

def main():
    Array = [int(a) for a in input("Enter the Array here: ").split()]
    length = len(Array)
    print("Combinations Using Recursion :")
    backtrack(Array,0,length)
    print("Combinations Using Itertools :")
    combi(Array)

def combi(arr):
    for i in range(1,len(arr)+1):
        comb = combinations(arr,i)
        for a in list(comb):
            print(a)

if __name__ == "__main__":
    main()
