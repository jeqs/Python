import numpy as np

# a = np.zeros((3,3), dtype=np.int32)
a = np.zeros((3,3))
a[:] = 10
# a.fill(8)
# a += 6
# a *= 6
a /= 2
# print(a)

b = a.sum()
# print(b)

c = a.sum(axis=0)
# print(c)

d = a.prod(axis=0)
# print(d)

d = a.mean()
# print(d)

d = a.max()
# print(d)

d = a.min(axis=0)
# print(d)

b = np.arange(1,10).reshape((3,3))
# plano = b.reshape(b.size)

# flatten - Copy
plano = b.flatten()
# print(plano)

# ravel - view
plano = b.ravel()
# print(plano)

# traspuesta swapaxes
c = np.arange(1,10).reshape((3,3))
tras = np.swapaxes(c, 0, 1)
# print(c)
# print(tras)

# transpose()
c2 = np.arange(1,10).reshape((3,3))
tras2 = c.transpose(1,0)
# print(c2)
# print(tras2)

# Matrices
m = np.zeros((3,3), dtype = np.int64)
m[:] = 2
mb = np.arange(1,10).reshape((3,3))
# print(m)
# print(mb)
# print('----')
# suma = m + mb
# suma = m - mb
suma = m + mb * 2
# print(suma)

# Multiplicacion Matrices
ml = np.zeros((3,3), dtype = np.int64)
ml[:] = 2
mlb = np.arange(1,10).reshape((3,3))
print(ml)
print(mlb)
print('----')
mm = np.matmul(ml,mlb)
# mm = ml.dot(mlb)
# mm = ml @ mlb
print(mm)
print(ml*mlb)
# suma = m + mb
# suma = m - mb
# suma = m + mb * 2
# print(suma)