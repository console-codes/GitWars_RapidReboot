#include <stdio.h>

int sum(int* arr, int n) {
    int s = 0;
    for(int i=0;i<n;i++)
        s += arr[i];
    return s;
}

int main() {
    int* p = NULL;
    printf("%d\n", sum(p, 5));
    return 0;
}
