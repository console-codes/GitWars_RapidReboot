#include <iostream>
using namespace std;

int square(int x) {
    return x * x;
}

int main() {
    int value = 50000;
    cout << square(value) << endl;
    return 0;
}
