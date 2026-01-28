#include <iostream>
using namespace std;

int* buildSquares(int n) {
    int arr[100];
    for(int i = 0; i < n; i++)
        arr[i] = i * i;
    return arr;
}

int main() {
    int* data = buildSquares(10);
    cout << data[5] << endl;
    return 0;
}
