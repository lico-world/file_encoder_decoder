import ctypes
import os


lib = ctypes.CDLL(os.path.abspath('lib/encoder_decoder.dll'))

lib.encode.argtypes = [ctypes.POINTER(ctypes.c_char_p), ctypes.c_char_p, ctypes.c_int, ctypes.c_int]
lib.encode.restype = None
lib.decode.argtypes = [ctypes.POINTER(ctypes.c_char_p), ctypes.c_char_p, ctypes.c_int, ctypes.c_int]
lib.decode.restype = None


def fileEncode(fileName: str, startExtension: str, key: bytes):
    with open('files/' + fileName + '.' + startExtension, 'rb') as inputFile:
        data = inputFile.read()

        lib.encode(ctypes.byref(ctypes.c_char_p(data)), key, len(data), len(key))
        with open('files/' + fileName + '-locked.secure', 'wb') as outputFile:
            outputFile.write(data)

    return data


def fileDecode(fileName: str, finalExtension: str, key: bytes):
    with open('files/' + fileName + '.secure', 'rb') as inputFile:
        data = inputFile.read()

        lib.decode(ctypes.byref(ctypes.c_char_p(data)), key, len(data), len(key))
        with open('files/' + fileName + '-unlocked.' + finalExtension, 'wb') as outputFile:
            outputFile.write(data)

    return data


def main():
    msg = b'hello world how are you'
    key = b'key 89'
    print('Initial message\t: ', msg)

    lib.encode(ctypes.byref(ctypes.c_char_p(msg)), key, len(msg), len(key))
    print('Message encoded\t: ', msg)

    lib.decode(ctypes.byref(ctypes.c_char_p(msg)), key, len(msg), len(key))
    print('Message decoded\t: ', msg, '\n', '-' * 100)

    fileEncode(fileName='image', startExtension='jpg', key=key)
    fileDecode(fileName='image-locked', finalExtension='jpg', key=key)

    fileEncode(fileName='video', startExtension='mp4', key=key)
    fileDecode(fileName='video-locked', finalExtension='mp4', key=key)


if __name__ == '__main__':
    main()
