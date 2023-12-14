# File Encoder/Decoder
And a training to mix **Python** with **C/C++**

---

First, you need to build the **DLLs** as follows (for Windows):

``gcc -shared -o lib/<name_file>.dll src/c/<name_file>.c``

For Linux:

``gcc -fPIC -shared -o lib/<name_file>.so src/c/<name_file>.c``

---

List of C/C++ files to build:
+ encoder_decoder.c