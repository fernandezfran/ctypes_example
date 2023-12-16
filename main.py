import ctypes as ct

import numpy as np


def add_arrays_c(arr1, arr2):
    size = arr1.size

    lib_core = ct.CDLL("./core.so")
    lib_core.add_arrays.argtypes = [
        ct.c_int,
        ct.POINTER(ct.c_double),
        ct.POINTER(ct.c_double),
        ct.POINTER(ct.c_double),
    ]
    res = (ct.c_double * size)()

    lib_core.add_arrays(
        size,
        arr1.ctypes.data_as(ct.POINTER(ct.c_double)),
        arr2.ctypes.data_as(ct.POINTER(ct.c_double)),
        res,
    )

    return np.frombuffer(res, dtype=np.double, count=size)
