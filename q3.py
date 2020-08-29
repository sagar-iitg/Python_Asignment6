import numpy as np
n=input('enter the size of the matrix ')
n=int(n)
flag=1
a=np.random.randint(1,101,size=(n,n))
a_transpose=a.transpose()
a_det=np.linalg.det(a)
a_trace=a.trace()
if(a_det==0):
    flag=0
else:
    flag=1
    a_inv=np.linalg.inv(a)
a_psuedoinv=np.linalg.pinv(a)
q, r = np.linalg.qr(a)
eig_val,eig_vec=np.linalg.eig(a)

print('matrix:\n',a)
print("\n")
print('transpose:\n',a_transpose)
print("\n")
print('Determinant:\n',a_det)
print("\n")
print('Trace:\n',a_trace)
print("\n")
if(flag==0):
    print("Inverse does not exist")
else:
    print('Inverse:\n',a_inv)
print("\n")
print('Pseudo inverse:\n',a_psuedoinv)
print("\n")
print("\n")
print('Q:\n',q)
print("\n")
print('R:\n',r)
print("\n")
print('Eigen values:\n',eig_val)
print("\n")
print('Eigen vectors:\n',eig_vec)
print("\n")
