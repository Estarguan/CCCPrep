#include <iostream>
using namespace std;

bool rising(int h2, int h3, int h4){
	if (h2>h3 || h3 > h4 || h2 == h3 || h3 == h4){
		return false;
	}else{
		return true;
	}
}

bool sinking(int h2, int h3, int h4){
	if (h2 < h3 || h3 < h4 || h2 == h3 || h3 == h4){
		return false;
	}else{
		return true;
	}
}
int main(){
	int h1,h2,h3,h4; cin >> h1 >> h2 >> h3 >> h4;
	if (h2>h1){
		if(rising(h2,h3,h4)){
			cout << "Fish Rising";
		}else{
			cout << "No Fish";
		}
	}else if (h1 > h2){
		if(sinking(h2,h3,h4)){
			cout << "Fish Diving";
		}else{
			cout << "No Fish";
		}
	}else{
		if (h2 != h3 || h3 != h4){
			cout << "No Fish";
		}else{
			cout << "Fish At Constant Depth";
		}
	}
}
