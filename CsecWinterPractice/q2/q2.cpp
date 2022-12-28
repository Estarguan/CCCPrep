#include <iostream>
#include <string>
using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int z = 0; z < t; ++z)
    {
        string s;
        cin >> s;
        for (int i = 0; i < s.length() - 1; ++i)
        {
            if (s[i] == s[i + 1])
            {
                s = s.replace(i, 1, ".");
            }
        }
        int count = 0;
        for (char i : s)
        {
            if (i == 'A' || i == 'B')
            {
                count++;
            }
        }
        cout << s.length() - count;
    }
}