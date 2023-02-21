#include <iostream>
using namespace std;

int main()
{
    int n, m, x;
    cin >> n >> m >> x;
    if (x < n * m)
    {
        cout << ":blobsob:\n"
             << n * m - x;
    }
    else
    {
        cout << ":poggies:";
    }
}