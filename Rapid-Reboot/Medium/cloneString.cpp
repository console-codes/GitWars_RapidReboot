#include <iostream>
#include <cstring>
#include <cstdlib>
using namespace std;

char* clone(const char* src) {
    char* buffer = (char*)malloc(strlen(src));
    strcpy(buffer, src);
    return buffer;
}

int main() {
    const char* text = "Hello World";
    char* copy = clone(text);
    cout << copy << endl;
    free(copy);
    return 0;
}
