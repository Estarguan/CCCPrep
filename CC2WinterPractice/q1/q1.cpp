#include <iostream>

int main(){
	int n; std::cin>>n;
	for(int i = 0; i < n; ++i){
		std::string num; std::cin >> num;
		int sum = 0;
		for (char j : num){
			sum += (int)j;
		}
		if (sum % 3 == 0){
			std::cout << "yes"<<std::endl;
		}else{
			std::cout << "no" <<std::endl;
		}
	}
}