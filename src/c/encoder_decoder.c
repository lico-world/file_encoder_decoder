#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const unsigned char alphabet[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890";
const size_t alphabetLength = strlen(alphabet);

static int findInAlphabet(char c)
{
    for(int idx = 0; idx < alphabetLength ; idx++)
    {
        if(c == alphabet[idx]) return idx%16;
    }
    return 0;
}

void encode(char** MSG, char* KEY, int MSG_LENGTH, int KEY_LENGTH)
{
    for(int idx=0 ; idx<MSG_LENGTH ; idx++)
        (*MSG)[idx] = ((*MSG)[idx] + findInAlphabet(KEY[idx%KEY_LENGTH])) % 255;
}

void decode(char** MSG, char* KEY, int MSG_LENGTH, int KEY_LENGTH)
{
    for(int idx=0 ; idx<MSG_LENGTH ; idx++)
        (*MSG)[idx] = (*MSG)[idx] - findInAlphabet(KEY[idx%KEY_LENGTH]);
}