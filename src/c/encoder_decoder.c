#include <stdio.h>

void call(int nb)
{
    printf("Called with half of %d\n", nb*2);
}

int fibo(int n)
{
    if(n == 0 || n == 1) return n;
    return fibo(n-1) + fibo(n-2);
}