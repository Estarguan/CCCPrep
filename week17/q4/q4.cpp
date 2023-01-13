#include <iostream>
using namespace std;

int main()
{
	int hunger, apples, wait, bar = 0; cin >> hunger >> apples >> wait;
	bar = (apples>hunger) ? hunger : apples;
	bar = (bar - wait < 0) ? 0 : bar - wait;
	cout << bar;
}
