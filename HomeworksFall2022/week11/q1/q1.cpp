#include <iostream>
using namespace std;
int main(){
	int lim; cin>>lim;
	int speed; cin>>speed;
	if (speed > lim){
		int f;
		if (speed-lim <= 20){
			f = 100;
		}else if (20 < speed-lim && speed-lim <= 30){
			f = 270;
		}else{
			f = 500;
		}
		cout << "You are speeding and your fine is $" << f << ".";
	}else{
		cout << "Congratulations, you are within the speed limit!";
	}
}
