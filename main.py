import ctypes
import os


lib = ctypes.CDLL(os.path.abspath('dlls/encoder_decoder.dll'))
lib.encode.restype = ctypes.c_char_p
lib.decode.restype = ctypes.c_char_p

msg = b'hello world how are you'
key = b'encryption key'
print('Initial message\t: ', msg.decode('utf-8'))

encoded = lib.encode(msg, key, int(len(msg)), int(len(key)))
print('Message encoded\t: ', encoded.decode('utf-8'))

decoded = lib.decode(encoded, key, int(len(msg)), int(len(key)))
print('Message decoded\t: ', decoded.decode('utf-8'))
