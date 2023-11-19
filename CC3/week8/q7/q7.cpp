/* This code is in dfs*/

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> pi;
const int MM = 1e5+2;
int N, tot, mx; vector<pi> adj[MM];
void dfs(int cur, int pre, int dis){
  mx = max(mx,dis);
  for (auto [nxt,w] : adj[cur]){
    if (nxt != pre) dfs(nxt,cur,dis+w);
  }
}

int main(){
  ios::sync_with_stdio(0); cin.tie(0);
  cin >> N;
  for (int i = 1, a, b,c; i <= N; i++){
    cin >> a >> b >> c; tot += c;
    adj[a].push_back({b,c}); 
    adj[b].push_back({a,c});
  }
  dfs(0,-1,0);
  cout << 2* tot - mx << "\n";
}