#include <bits/stdc++.h>
using namespace std;
const int MM = 5002;
int N, a[MM], ans[MM], memo[MM][MM];

int fun(int l, int r){
  if (l >= r) return 0;
  if (memo[l][r] != -1) return memo[l][r];
  return memo[l][r] = abs(a[l]-a[r]) + fun(l+1,r-1);
}

int main(){
  ios::sync_with_stdio(0); cin.tie(0);
  memset(memo,-1,sizeof(memo));
  fill(ans,ans+MM,1e9);
  cin >> N;
  for (int i=1; i<=N; i++) cin >> a[i];
  
  for (int i = 1; i <= N; i++){
    for (int j = i; j <= N; j++){
      ans[j-i+1] = min(ans[j-i+1],fun(i,j));
    }
  }
  for (int i = 1; i<= N; i++){
    cout << ans[i] << " ";
  }
}