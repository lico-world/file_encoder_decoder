import ctypes
import os
import time


lib = ctypes.CDLL(os.path.abspath('dlls/encoder_decoder.dll'))


def fibo(n):
    if n == 0 or n == 1:
        return n
    return fibo(n-1) + fibo(n-2)


START_C = time.perf_counter()
lib.fibo(37)
END_C = time.perf_counter()

START_PYTHON = time.perf_counter()
fibo(37)
END_PYTHON = time.perf_counter()

TIME_C = END_C-START_C
TIME_PYTHON = END_PYTHON-START_PYTHON
print('Python\t\t: ', TIME_PYTHON, 's\nC\t\t\t: ', TIME_C, 's\nDifference\t: ',
      100*(TIME_PYTHON-TIME_C)/TIME_PYTHON, '%')
