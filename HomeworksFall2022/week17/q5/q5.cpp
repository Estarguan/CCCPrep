#include <iostream>
using namespace std;

int main()
{
  int n, count = 0; string l1, l2; cin>>n>>l1>>l2;
  for (int i = 0; i < n; ++i){
    if (l1[i]=='S' && l2[i] == 'S'){count++;}
  }
  string ans = (count > 2) ? "NO": "YES";
  cout << ans;
}
