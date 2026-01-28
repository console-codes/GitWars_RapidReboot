#include <iostream>
#include <vector>
using namespace std;

bool skip(int v) {
    return v == 3;
}

void advance(int& i) {
    if(skip(i))
        return;
    i++;
}

int main() {
    vector<int> data;
    for(int i = 0; i < 10; i++)
        data.push_back(i);

    int index = 0;
    while(index < data.size()) {
        cout << data[index] << endl;
        advance(index);
    }
    return 0;
}
