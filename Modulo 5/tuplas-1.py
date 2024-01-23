import sys, timeit
tupla = (1, "string", True)
# tupla[1] = "data" Inmutable
print (type(tupla))
print (tupla[1])
print (sys.getsizeof(tupla), 'bytex')
print (timeit.timeit(stmt="1, 'string', True", number= 1000000))
