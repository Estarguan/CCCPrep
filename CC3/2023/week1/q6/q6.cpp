#include <bits/stdc++.h>/
using namespace std;

int adj[4][4], sum, connect = true;
int main(){
  cin.sync_with_stdio(0); cin.tie(0);cout.tie(0);
  for (int i = 0; i <4; i++){
    int row = 0;
    for (int j=0; j < 4; j++){
      cin >> adj[i][j];
      sum += adj[i][j];
      row += adj[i][j];
    }
    if (row==0){
      connect=false;
    }
  }
  if (connect && sum == 6){
    cout << "Yes\n";
  }else{
    cout << "No\n";
  }
  return 0;
}