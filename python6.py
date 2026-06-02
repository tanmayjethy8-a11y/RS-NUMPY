arr1=[[1,2,3],
   [4,5,6]]
arr2=[[7,8,9],
   [10,11,12]]
r=[]
for i in range(len(arr1)):
    row=[]
    for j in range(len(arr1[0])):
        row.append(arr1[i][j]+arr2[i][j])
    r.append(row)
print(r)