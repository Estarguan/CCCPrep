#include <iostream>
using namespace std;

int main(){
  int n; cin >> n;
  int t1[n];int t2[n];
  for (int i = 0; i < n; ++i){
    cin >> t1[i];
  }
  for (int i=0; i<n; ++i){
    cin >> t2[i];
  }
  int c1=0, c2=0, ans=0;
  for (int i=0; i<n; ++i){
    c1 += t1[i];
    c2 += t2[i];
    if (c1==c2){
      ans = i+1;
    }
  }
  cout << ans << endl;
}