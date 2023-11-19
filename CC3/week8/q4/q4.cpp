#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int MM = 1e5+2;
int N, M; bool vis[MM]; vector<int> adj[MM];
int main(){
  ios::sync_with_stdio(0); cin.tie(0);
  cin >> N >> M;
  for (int i = 1,x ,y; i <= M; i++){
    cin >> x >> y; adj[y].push_back(x);
  }
  queue<int> q; q.push(1);
  while(!q.empty()){
    int u = q.front(); q.pop();
    for (int v : adj[u]){
      if (!vis[v]){
        q.push(v); vis[v] = 1;
      }
    }
    if (adj[1].empty()) vis[1]= 1;
    for (int i = 1; i <= N; ++i){cout << vis[i];}
    cout << "\n";
  }
}