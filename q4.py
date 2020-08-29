import numpy as np
n=np.random.randint(low=2,high=10)
print('Number of equations :',n)
a=np.random.randint(low=-10, high=50, size=(n,n))
print('Matrix A:',a)
b=np.random.randint(low=-10, high=50, size=n)
print('b:',b)
print('x:')
print(np.linalg.solve(a,b))
