#include <iostream>
using namespace std;
int main(){
    int t1, t2; cin >> t1 >> t2;
    int diff = t1-t2, num = 2;
    while (diff >= 0){
        int temp = diff;
        diff = t2-diff;
        t2 = temp;
        num++;
    }
    cout << num;
}
