'''
hamming distance is the distance is defined as the number of bit positions that are different.

'''
def hamming_distance(x,y):
    dif = x^y
    count = 0
    print(dif)
    while dif!=0:
        count+=1
        dif &= dif-1
        print(dif)
    return count
x,y = map(int,input().split())
print(hamming_distance(x,y))
