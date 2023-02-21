#include <iostream>
using namespace std;

int main(){
  int start, end; cin >> start >> end;
  if (start < 20){
    cout << "Unhealthy" << endl;
  }else if (start > 23){
    cout << "Unhealthy" << endl;
  }else if (end < 6){
    cout << "Unhealthy" << endl;
  }else if (end > 9){
    cout << "Unhealthy" << endl;
  }else{
    if ((end + 24-start) < 8 || (end + 24-start) > 10 ){
      cout << "Unhealthy" << endl;
    }else{
      cout << "Healthy" << endl;
    }
  }
}