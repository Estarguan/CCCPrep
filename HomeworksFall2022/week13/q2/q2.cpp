#include <iostream>

using namespace std;

string input()
{
    string temp;
    cin >> temp;
    return temp;
}

#define done cout << endl;
int main()
{
    int n = stoi(input()), cnt = 0;
    string guess[n], ans[n];
    for (int i = 0; i < n; ++i)
    {
        guess[i] = input();
    }
    for (int i = 0; i < n; ++i)
    {
        ans[i] = input();
    }
    for (int i = 0; i < n; ++i)
    {
        if (guess[i] == ans[i])
        {
            cnt++;
        }
    }
    cout << cnt;
    done
}
