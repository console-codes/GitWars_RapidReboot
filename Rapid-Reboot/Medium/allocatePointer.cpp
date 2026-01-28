#include <iostream>
using namespace std;

int* allocate(int value) {
    int* ptr = new int(value);
    return ptr;
}
void release(int* ptr) {
    delete ptr;
}
int* createValue() {
    int* data = allocate(10);
    if (*data > 0) {
        release(data);
    }
    return data; 
}

int main() {
    int* x = createValue();
    cout << *x << endl;
    return 0;
}

