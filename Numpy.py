import numpy as np
a = np.arange(1,11)
print(a.ndim,a.size,a.dtype)
print(np.arange(1,13).reshape(3,4))
output:
(1, 10, dtype('int32'))
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
