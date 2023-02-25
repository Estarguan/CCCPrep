#include <iostream>
#include <vector>
using namespace std;

int main(){
  string t, s; cin >> t >> s;
  string cyclic[s.size()];
  for (int i = 0; i < s.size(); ++i){
    cyclic[i] = s;
    s = s.substr(1) + s[0];
  }
  for (string i : cyclic){
    if (t.find(i) != string::npos){
      cout << "yes" << endl;
      return 0;
    }
  }
  cout << "no" << endl;
}
