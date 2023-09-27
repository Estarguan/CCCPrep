#include <iostream>
#include <queue>
using namespace std;

const int MM = 2e5+2;
int X,Y, dis[MM]; bool vis[MM]; queue<int> q;
int main(){
  ios::sync_with_stdio(0);cin.tie(0);
  cin >> X >> Y;
  q.push(X); vis[X] = 1; dis[X] = 0;
  while (!q.empty()){
    int cur = q.front();q.pop();
    vector <int> vec = {cur-1,cur+1,cur*2};
    for (int nxt : vec){
      if (0 <= nxt && nxt < MM && !vis[nxt]){
        q.push(nxt);vis[nxt]=1;
        dis[nxt] = dis[cur] +1;
      }
    }
  }
  cout << dis[Y]<<"\n";
}
