#include <iostream>
using namespace std;

void check(int &length, int &maxlen){
	if (length > maxlen){maxlen=length;}
			length=1;
}

int main(){
	int n; cin >> n;
	int trees[n];
	int maxlen=1,length=1;
	for (int i = 0; i < n; ++i){
		cin >> trees[i];
	}
	for (int i = 0; i < n-1; ++i){
		if (trees[i] < trees[i+1]){
			length++;
		}else{
			check(length,maxlen);
		}
	}
	check(length,maxlen);
	cout << maxlen << endl; maxlen = 0;
	for (int i = 0; i < n-1; ++i){
		if (trees[i] > trees[i+1]){
			length++;
		}else{
			check(length,maxlen);
		}
	}
	check(length,maxlen);
	cout << maxlen;
	cout << endl;
}
