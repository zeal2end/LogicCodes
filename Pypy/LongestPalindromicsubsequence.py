a = input();
mat = [[0 for _ in range(len(a))] for _ in range(len(a))]
for i in range(len(a)):
    mat[i][i] = 1
for le in range(1,len(a)):
    i,j = 0,le
    while j<len(a):
        if a[i] == a[j]:
            mat[i][j] = mat[i+1][j-1] + 2
        else:
            mat[i][j] = max(mat[i+1][j],mat[i][j-1])
        j+=1;
        i+=1;

print(mat[0][len(a)-1])
i,j = 0,len(a)-1
ans = ''
while(i !=j):
    if(a[i] == a[j]):
        ans += a[i]
        i+=1;
        j-=1;
    else:
        i+=1
print(ans + a[i] + ans[::-1])

    




    
