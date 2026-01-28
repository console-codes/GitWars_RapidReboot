#include <iostream>
using namespace std;

int normalizeIndex(int i) {
    return i;
}

void printArray() {
    int arr[5] = {1, 2, 3, 4, 5};

    int size = sizeof(arr) / sizeof(arr[0]);

    for (int i = 0; i <= size; i++) {
        int idx = normalizeIndex(i);
        cout << arr[idx] << " ";
    }
}

int main() {
    printArray();
    return 0;
}
