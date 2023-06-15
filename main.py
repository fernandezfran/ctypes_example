import ctypes as ct
import numpy as np

lib_core = ct.CDLL("./core.so")

lib_core.add_arrays.argtypes = [
    ct.c_int,
    ct.POINTER(ct.c_double),
    ct.POINTER(ct.c_double),
    ct.POINTER(ct.c_double),
]

arr1 = np.array([1.0, 2.0, 3.0])
arr2 = np.array([3.0, 2.0, 1.0])

n = len(arr1)

res_arr = (ct.c_double * n)()

lib_core.add_arrays(
    n,
    arr1.ctypes.data_as(ct.POINTER(ct.c_double)),
    arr2.ctypes.data_as(ct.POINTER(ct.c_double)),
    res_arr,
)

result = np.frombuffer(res_arr, dtype=np.double, count=n)
print(result)
