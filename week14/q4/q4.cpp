#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

#define done cout << endl;
int main()
{
    int n;
    cin >> n;
    vector<pair<string, int>> pc;
    for (int i = 0; i < n; ++i)
    {
        string name;
        long r, s, d;
        cin >> name >> r >> s >> d;
        pair<string, int> temp(name, 2 * r + 3 * s + d);
        pc.push_back(temp);
    }
    sort(pc.begin(), pc.end(), [](pair<string, int> x, pair<string, int> y)
         { return x.first < y.first; });
    /*for (pair<string, int> num : pc)
    {
        cout << num.first << " " << num.second << endl;
    }*/
    sort(pc.begin(), pc.end(), [](pair<string, int> x, pair<string, int> y)
                { return x.second > y.second; });
    /*for (pair<string, int> num : pc)
    {
        cout << num.first << " " << num.second << endl;
    }*/
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
/*n = int(input())
pc = []

for _ in range(n):
  pc.append(input().split())

pc = sorted(pc, key=lambda x: x[0])

pc = sorted(pc, key=lambda x : (2 * (int(x[1])) + 3 * (int(x[2])) + (int(x[3]))), reverse= True)

if len(pc) == 0:
  print(" ")
else:
  if len(pc) == 1:
      print(pc[0][0])
  else:
      print(pc[0][0])
      print(pc[1][0])
}*/
