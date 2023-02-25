#include <iostream>
using namespace std;

int main()
{
  int max,A,B,C; cin >> max >> A >> B >> C;
  if (A+4*B+7*C <= max){
    cout << "Time to go shopping!";
  }else{
    cout << "You cannot afford them all.";
  }
}
