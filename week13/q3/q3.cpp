#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int t, n;
    cin >> t >> n;
    vector<int> cords = {0};
    for (int i = 0; i < n; ++i)
    {
        int temp;
        cin >> temp;
        cords.push_back(temp);
    }
    sort(cords.begin(), cords.end(), [](int x, int y)
         { return abs(x) < abs(y); });
    int cnt = 0, cord = 0;
    for (int i = 1; i < n; ++i)
    {
        t -= abs(cords[i] - cords[i - 1]);
        if (t >= 0)
        {
            cnt += 1;
        }
        else
        {
            break;
        }
    }
    cout << cnt;
}