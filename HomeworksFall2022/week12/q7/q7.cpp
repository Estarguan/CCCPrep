#include <iostream>
using namespace std;
string input()
{
    string temp;
    cin >> temp;
    return temp;
}

int main()
{
    int n = stoi(input()), a[n];
    for (int i = 0; i < n; ++i)
    {
        a[i] = stoi(input());
    }
    int ans = 0;
    for (int i = 0; i < n; ++i)
    {
        int sum = 0;
        for (int j = i; j < n; ++j)
        {
            sum += a[j];
            for (int k = i; k <= j; ++k)
            {
                if (a[k] * (j - i + 1) == sum)
                {
                    ans++;
                    break;
                }
            }
        }
    }
    cout << ans;
}