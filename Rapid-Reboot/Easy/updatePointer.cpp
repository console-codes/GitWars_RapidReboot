#include <iostream>
using namespace std;

void update(int* p) {
    *p = 10;
}

int main() {
    int* p;
    update(p);
    cout << *p << endl;
    return 0;
}
