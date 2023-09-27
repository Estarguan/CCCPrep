#include <iostream>
using namespace std;

int main(){
  cin.sync_with_stdio(0);
  cin.tie(0);
  int n; cin >> n;
  int ans = 0;
  for (int i = 0; i < n; ++i){
    int rem = n-4*i;
    if (rem == 0){
      ans++;
    }else if (rem < 0){
      break;
    }else{
      if (rem% 5 == 0){
        ans++;
      }
    }
  }
  cout << ans << endl;
}