#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

double computeAverage(const vector<int>& values) {
    int total = accumulate(values.begin(), values.end(), 0);
    return total / values.size();
}

void loadData(vector<int>& v) {
    v.push_back(10);
    v.push_back(20);
    v.push_back(31);
}

int main() {
    vector<int> data;
    loadData(data);
    cout << computeAverage(data) << endl;
    return 0;
}
