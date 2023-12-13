# File Encoder/Decoder
And a training to mix **Python** with **C/C++**

If you want to modify any **C/C++** file, you then need to build the corresponding **DLL** as follows (for Windows):

``gcc -fPIC -shared -o dlls/<name_file>.dll src/c/<name_file>.c``