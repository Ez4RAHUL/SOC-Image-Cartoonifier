import numpy as np
inilist = [[1,5,3,4],[12,3,9,1],[51,21,33,1],[9,76,4,11]]
arr = np.array(inilist)

#trace of matrix :
tr = np.trace(arr)
print(tr)

#printing diagonal elements :
print(arr[[0,1,2,3],[0,1,2,3]])

#max min of each row :
for i in range (4):
    print(np.max(arr[i,:]))

for i in range (4):
    print(np.min(arr[i,:]))

#creating another numpy array of shape(4,5) :

secondarr =np.random.uniform(0,1,[4,5])
print(secondarr)

print("\n")
#multiplying both matrices
print(np.matmul(arr,secondarr))

