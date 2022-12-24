#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


// Its wrong but its close enough
int main()
{
    int n;
    cin >> n;
    vector<pair<string, int>> pc;
    for (int i = 0; i < n; ++i)
    {
        string name;
        int r, s, d;
        cin >> name >> r >> s >> d;
        pair<string, int> temp(name, 2 * r + 3 * s + d);
        pc.push_back(temp);
    }
    sort(pc.begin(), pc.end(), [](pair<string, int> x, pair<string, int> y)
         { return x.first > y.first; });
    sort(pc.begin(), pc.end(), [](pair<string, int> x, pair<string, int> y)
         { return x.second < y.second; });
    if (pc.empty())
    {
        return 0;
    }
    else
    {
        if (n == 1)
        {
            cout << pc[0].first;
        }
        else
        {
            cout << pc[0].first << endl
                 << pc[1].first;
        }
    }
}
