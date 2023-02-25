#include <iostream>
#include <algorithm>
using namespace std;

int main(){
  string line; cin >> line;
  sort(line.begin(),line.end());
  do {
    for (char i : line){
      cout << i;
    }
    cout << "\n";
  }while(next_permutation(line.begin(),line.end()));
}
