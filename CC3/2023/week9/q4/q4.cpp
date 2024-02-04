#include <bits/stdc++.h>
using namespace std;
const int MM = 2e5+2;
typedef pair<int,int> pi;

int n;vector<int> adj[MM],adj2[MM]; vector<pi> ans; 

void dfs1(int cur,int pre){
  for (int nxt: adj[cur]){
    if (nxt == pre){
      continue;
    }
    adj2[pre].push_back(nxt);
    dfs1(nxt,cur);
  }
}

void dfs2(int u, int pre){
  for (int v : adj2[u]){
    if (v==pre){
      continue;
    }ans.push_back({u,v});
    dfs2(v,u);
  }
}

void print(){
  cout << ans.size() + 1 << "\n";
  for (auto [u,v] : ans) cout << u << " " << v << "\n";
  ans.clear();
}
int main(){
  ios::sync_with_stdio(0);cin.tie(0);
  cin >> n;
  for (int i = 1, u,v; i < n;++i){
    cin >> u >> v;
    adj[u].push_back(v);adj[v].push_back(u);
  }
  cout << 1 + adj[1].size() << "\n";
  dfs1(1,0); dfs2(1,0); print();
  for (int u : adj[1]){
    dfs2(u,0); print();
  }
}