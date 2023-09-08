#include <iostream>

using namespace std;
int main(){
	string str1 = "*x*";
	string str2 = " xx";
	string str3 = "* *";
	int k; cin >> k;
	string ans1="", ans2="", ans3="";

	for (char chr : str1){
		ans1 += string(k,chr);
	}
	for (char chr : str2){
		ans2 += string(k,chr);
	}
	for (char chr : str3){
		ans3 += string(k, chr);
	}
	for (int i = 0; i < k; ++i){
		cout << ans1;
		cout << endl;
	}
	for (int i = 0; i < k; ++i){
		cout << ans2;
		cout << endl;
	}
	for (int i = 0; i < k; ++i){
		cout << ans3;
		cout << endl;
	}
}
