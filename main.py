import ctypes
import os

lib = ctypes.CDLL(os.path.abspath('dlls/encoder_decoder.dll'))
lib.call(17)
