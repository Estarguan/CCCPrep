#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <map>
using namespace std;

int main()
{
	unordered_map<int, int> dic;
	int n;
	cin >> n;
	int nums[n];
	for (int i = 0; i < n; ++i)
	{
		cin >> nums[i];
	}
	for (int i = 0; i < n; ++i)
	{
		if (dic.count(nums[i]))
		{
			dic[nums[i]]++;
		}
		else
		{
			dic[nums[i]] = 1;
		}
	}

	int ans = 0;
	int max = *max_element(nums, nums + n);
	int min = *min_element(nums, nums + n);
	int tut = max + 1;

	for (int i = max; i > min - 1; --i)
	{
		if (dic.count(i))
		{
			int count = 0;
			for (auto pair : dic)
			{
				if (pair.first >= i)
				{
					count += dic[pair.first];
				}
			}
			if (count * i >= ans)
			{
				if (i < tut)
				{
					ans = count * i;
					tut = i;
				}
			}
			if (count == n)
			{
				break;
			}
		}
	}
	cout << ans << " " << tut;
}