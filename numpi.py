import numpy as np
#single dimentional numpy array
n1 = np.array([10,20,30,40])
print(n1)
print(type(n1))

n2 = np.zeros((1,2))
print(n2)
n3 = np.zeros((6,6))
print(n3)
n4 = np.full((3,4),9)
print(n4)
n5 = np.arange(10,21)
print(n5)
n6 = np.arange(100,200,20)
print(n6)
n7 = np.random.randint(100,150,5)
print(n7)

n8 = np.array([[1,2,3],[4,5,6]])
print(n8.shape)
n8.shape = (3,2)
print(n8)

a = np.array([10,20])
b = np.array([30,40])
c = np.sum([a,b])
print(c)
d = np.sum([a,b],axis=0)
print(d)
e = np.sum([a,b],axis=1)
print(e)

N1 = np.array([10,20,30])
N2 = np.array([30,40,50])
print(np.vstack([N1,N2]))
print(np.hstack([N1,N2]))
print(np.column_stack([N1,N2]))

