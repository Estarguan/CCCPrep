#include <iostream>
using namespace std;
int main(){
    int k; string str; cin>>k>>str;
    for (int i = 0; i < str.length(); ++i){
        int x = int(str[i]) - (3*(i+1)+k);
        if (x < 65){
            x = 90 - (65 - (x+1));
        }
        cout << (char)x;
    }
}
