#include <iostream>
using namespace std;

int offset(int base, int factor) {
    return base * factor;
}

int* advance(int* ptr, int steps) {
    return ptr + steps;
}

int main() {
    int arr[5] = {1, 2, 3, 4, 5};

    int* p = arr;

    int logicalIndex = offset(5, 20) / 10; 
    p = advance(p, logicalIndex);

    cout << *p << endl;   
    return 0;
}
