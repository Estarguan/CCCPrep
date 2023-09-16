#include <bits/stdc++.h>
using namespace std;

int n,m;
int main()
{
  cin.sync_with_stdio(0); cin.tie(0);cout.tie(0);
  cin >> n >> m;
  for (int i = 2; i <= n; i++){
    cout << "1 " << i << "\n"; m--;
  }
  for (int i = 2; i <= n && m; i++){
    for (int j = i + 1; j <= n && m; j++){
      cout << i << " " << j << "\n"; m--;

    }
  }
}