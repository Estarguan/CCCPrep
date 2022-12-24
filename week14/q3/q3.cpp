#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<int> nums;
    for (int i = 0; i < n; ++i)
    {
        int temp;
        cin >> temp;
        nums.push_back(temp);
    }
    sort(nums.begin(), nums.end(), [](int x, int y){
         return x > y;
    });


    stable_sort(nums.begin(), nums.end(),  [](int x, int y){
         return x%10 < y%10;
    });
    for(auto i : nums)cout<<i<<" ";
}
