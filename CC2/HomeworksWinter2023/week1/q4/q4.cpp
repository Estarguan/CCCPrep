#include <iostream>
#include <vector>
using namespace std;

int main()
{
  int n; cin >> n;
  vector<int> trees;
  int prev = 0;
  for (int i = 0; i < n; ++i){
    int temp; cin >> temp;
    trees.push_back(temp+prev);
    prev = trees[i];
  }
  int q; cin >> q;
  for (int i = 0; i < q; ++i){

    int n1,n2; cin >> n1 >>n2;
    if (n1 != 0){
      cout << trees[n2]-trees[n1-1] << endl;
    }else{
      cout << trees[n2] << endl;
    }
  }
}
