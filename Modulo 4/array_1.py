import numpy as np

my_array = np.array([1,2,3,4,5,6])
# print(type(my_array))

my_array2 = np.array([[1,2,3],[4,5,6],[4,5,6]], dtype=np.int8)
# print(my_array2.shape)

my_array3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]], dtype=np.int8)
# print(my_array3)
# print(my_array3.shape)
# print(my_array3.ndim)

my_array4 = np.array([[1,2,3],[4,5,6]], dtype=np.int8)
# print("array 4:")
# print(my_array4)
# print(my_array4.shape)
# print(my_array4.ndim)

my_array5 = my_array4.reshape((3,2))
# print("array 5:")
# print(my_array5)
# print(my_array5.shape)

my_array6 = np.arange(8)
print("array 6:")
print(my_array6)
print(my_array6.shape)

# start
my_array7 = np.arange(1, 8)
print("array 7:")
print(my_array7)
print(my_array7.shape)

# step
my_array8 = np.arange(1, 8, 2)
print("array 8:")
print(my_array8)
print(my_array8.shape)

# step
my_array9 = np.arange(1, 8, 0.5)
print("array 9:")
print(my_array9)
print(my_array9.shape)

# zero
my_array10 = np.zeros((2,3))
print("array 10:")
print(my_array10)
print(my_array10.shape)

# ones
my_array11 = np.ones((2,3))
print("array 11:")
print(my_array11)
print(my_array11.shape)

# empty
my_array12 = np.empty((1,3))
print("my_array12:")
print(my_array12)
print(my_array12.shape)

# eye
my_array13 = np.eye(3)
print("my_array13:")
print(my_array13)
print(my_array13.shape)

my_array13 = np.eye(3, k=-1)
print("my_array13:")
print(my_array13)
print(my_array13.shape)

my_array13 = np.eye(3, k=-1)
my_array13[my_array13 ==0] = 2
print("my_array13:")
print(my_array13)
print(my_array13.shape)

y_array13 = np.eye(3, k=-1)
my_array13[my_array13 <=1] = 3
print("my_array13:")
print(my_array13)
print(my_array13.shape)

y_array13 = np.eye(3, k=-1)
my_array13[0] = 4
print("my_array13:")
print(my_array13)
print(my_array13.shape)

y_array13 = np.eye(3, k=-1)
my_array13[:2] = 6
print("my_array13:")
print(my_array13)
print(my_array13.shape)

y_array13 = np.eye(3, k=-1)
my_array13[1:] = 7
print("my_array13:")
print(my_array13)
print(my_array13.shape)

y_array13 = np.eye(3, k=-1)
my_array13[1:, 2:] = 8
print("my_array13:")
print(my_array13)
print(my_array13.shape)

y_array13 = np.eye(3, k=-1)
my_array13[1:, 2:] = 8
my_array13_sort = np.sort(my_array13)
print("my_array13:")
print(my_array13_sort)
print(my_array13_sort.shape)

y_array13 = np.eye(3, k=-1)
my_array13[1:, 2:] = 8
my_array13_sort = np.sort(my_array13, axis=0)
print("my_array13:")
print(my_array13_sort)
print(my_array13_sort.shape)

# quicksort => Ordenamiento por defecto, kind = heapsort, mergsort
y_array13 = np.eye(3, k=-1)
my_array13[1:, 2:] = 8
my_array13_sort = np.sort(my_array13, axis=0, kind = 'heapsort')
print("my_array13:")
print(my_array13_sort)
print(my_array13_sort.shape)

# copy
y_array13 = np.eye(3, k=-1)
my_array13[1:, 2:] = 8
my_array13_sort = np.sort(my_array13)
array_view = my_array13_sort.view()
print("my_array13:")
print(array_view)
print(my_array13_sort)

# copy
y_array13 = np.eye(3, k=-1)
my_array13[1:, 2:] = 8
my_array13_sort = np.sort(my_array13)
array_view = my_array13_sort.copy()
print("my_array13:")
print(array_view)
print(my_array13_sort)