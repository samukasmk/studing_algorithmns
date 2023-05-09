#include <stdio.h>

int pairSum(int a, int b) {
    printf("pairSum(a=%d, b=%d)\n", a, b);
    return a + b;
}

int pairSumSequence(int n) {

    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += pairSum(i, i+1);
        printf("pairSumSequence sum=%d\n", sum);
    }
    return sum;
}



void main() {
    pairSumSequence(10);
}