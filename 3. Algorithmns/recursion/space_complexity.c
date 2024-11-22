#include <stdio.h>

int sum(int n) {
    if (n <= 0) {
        printf("Finishing recursive calls with (%d)...\n", n);
        return 0;
    }

    printf("Recursive calling of same function sum(%d)...\n", n);
    return n + sum(n-1);
}

void main() {
    sum(10);
}