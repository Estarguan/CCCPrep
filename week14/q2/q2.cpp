#include <iostream>
using namespace std;
int main()
{
    int count = 0;
    int temp;
    cin >> temp;
    for (int i = 0; i < temp; ++i)
    {
        int m, o;
        cin >> m >> o;
        if (m > o)
        {
            count++;
        }
    }
    cout << count;
}