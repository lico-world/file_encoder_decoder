#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const char alphabet[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890";
const size_t alphabetLength = strlen(alphabet);

static int findInAlphabet(char c)
{
    for(int idx = 0; idx < alphabetLength ; idx++)
    {
        if(c == alphabet[idx]) return idx;
    }
    return -1;
}

char* encode(char* MSG, char* KEY, int MSG_LENGTH, int KEY_LENGTH)
{
    char* encoded = (char*)malloc(MSG_LENGTH * sizeof(char));
    for(int idx=0 ; idx<MSG_LENGTH ; idx++)
    {
        int newCharIndex = findInAlphabet(MSG[idx]) + findInAlphabet(KEY[idx % KEY_LENGTH]);
        encoded[idx] = alphabet[newCharIndex % alphabetLength];  // Avoid OOB
    }
    return encoded;
}

char* decode(char* MSG, char* KEY, int MSG_LENGTH, int KEY_LENGTH)
{
    char* decoded = (char*)malloc(MSG_LENGTH * sizeof(char));
    for(int idx=0 ; idx<MSG_LENGTH ; idx++)
    {
        int newCharIndex = findInAlphabet(MSG[idx]) - findInAlphabet(KEY[idx % KEY_LENGTH]);
        decoded[idx] = alphabet[(newCharIndex + alphabetLength) % alphabetLength];  // '+ alphabetLength' to avoid negative indexes
    }
    return decoded;
}