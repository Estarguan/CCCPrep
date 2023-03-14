#include <iostream>

using namespace std;

int main()
{
  int n,x,y;cin>>n>>x>>y;
  int an = 0, tom = 0;
  for (int i = 0; i < n; ++i){
    int a, b; cin>>a>>b;
    if (a<x){
      an++;
    }else{
      an+=2;
    }
    if (b<y){
      tom++;
    }else{
      tom+=2;
    }
  }
  if (tom==an){
      cout << "Tie!" << endl;
    }else if (tom<an){
      cout << "Tommy wins!" << endl;
    }else{
      cout << "Andrew wins!" << endl;
    }
  
}