#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int main(){
	int n; cin >> n;
	string cows = "";
	if (n >= 1000){
		for (int i = 0; i < 1000; ++i){
			cows += "moo";
		}
	}else{
		for (int i = 0; i < n; ++i){
			cows += "moo";
		}
	}
	string sub; cin >> sub;
	if (cows.find(sub)!= string::npos){
		cout << "yes";
	}else{
		cout << "no";
	}
}