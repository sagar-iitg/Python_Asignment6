import numpy as np
outcomes = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
a = np.random.choice(outcomes,size=(12,12))
b = np.zeros((12,12,12))


for i in range(0,12):
    for j in range(0,12):
        k = outcomes.index(a[i][j])
        b[i][j][k] = 1


print(a)
print("\n output 3d matrix\n")
print(b)
c=0
for i in range(0,12):
    for j in range(0,12):
        k=a[i][j]
        c=c+1
        print(k,b[i][j])

#print(c)

