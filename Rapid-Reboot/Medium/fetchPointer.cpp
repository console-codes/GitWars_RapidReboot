#include <iostream>
using namespace std;

int* fetchPointer(bool valid) {
    int* ptr = nullptr;
    if (valid) {
        static int value = 42;
        ptr = &value;
    }
    return ptr;
}

int main() {
    bool condition = false;
    int* p = fetchPointer(condition);
    if (p == nullptr) {
        cout << "Using default value\n";
    }
    cout << *p << endl;
    return 0;
}
