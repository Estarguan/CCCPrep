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
    int n = stoi(input());
    int s = 0, t = 0;
    for (int i = 0; i <= n; ++i)
    {
        string line;
        getline(cin, line);
        for (char i : line)
        {
            if (i == 's' || i == 'S')
            {
                s++;
            }
            else if (i == 't' || i == 'T')
            {
                t++;
            }
        }
    }
    if (s > t)
    {
        cout << "French";
    }
    else if (s < t)
    {
        cout << "English";
    }
    else
    {
        cout << "French";
    }
    done
}
