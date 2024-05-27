"""A Python library that does evil things to __xor__."""

from __future__ import annotations

import ctypes
import sys


try:
    nm_padding = {
        (3, 10): ((ctypes.c_void_p,) * 14),
    }[sys.version_info[:2]]

    pt_padding = {
        (3, 10): ((ctypes.c_ssize_t,) * 5 + (ctypes.c_void_p,) * 7)
    }[sys.version_info[:2]]
except KeyError as e:
    raise RuntimeError(f"Unsupported version {sys.version!r}.") from e


binary_func = ctypes.CFUNCTYPE(*((ctypes.py_object,) * 3))


class PyNumberMethods(ctypes.Structure):
    _fields_ = [
        *(("idc", t) for t in nm_padding),
        ("nb_xor", binary_func),
    ]


class PyTypeObject(ctypes.Structure):
    _fields_ = [
        *(("idc", t) for t in pt_padding),
        ("tp_as_number", ctypes.POINTER(PyNumberMethods)),
    ]


for t in (int, float):
    nbs = ctypes.cast(id(t), ctypes.POINTER(PyTypeObject)).contents.tp_as_number
    nbs.contents.nb_xor = binary_func(lambda x, y: x.__pow__(y))

two = 2
assert two ^ 3 == 8, "Failed to overwrite xor on int."

float_two = 2.0
assert float_two ^ 3.0 == 8.0, "Failed to overwrite xor on float."
