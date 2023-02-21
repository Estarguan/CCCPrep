#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int k, n, finans = 0;
    cin >> k >> n;
    int ranks[n][n];
    int ans[n][n];
    for (int i = 0; i < k; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            int temp;
            cin >> temp;
            ranks[i][j] = temp;
        }
    }
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            ans[i][j] = 0;
        }
    }
    for (int x = 0; x < k; ++x)
    {
        for (int y = 0; y < n; ++y)
        {
            for (int z = y + 1; z < n; ++z)
            {
                int temp = ranks[x][y];

                ans[temp - 1][ranks[x][z] - 1]++;
            }
        }
    }

    int N = sizeof(ans) / sizeof(ans[0]);
    for (int i = 0; i < n; ++i)
    {
        finans += count(ans[i], ans[i] + N, k);
    }
    cout << finans << endl;
}
