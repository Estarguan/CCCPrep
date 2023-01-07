#include <iostream>
using namespace std;

int main()
{
	string stringa;
	cin >> stringa;
	string stringb;
	cin >> stringb;
	int maxcnt = 0;
	if (stringb.length() >= stringa.length())
	{
		int cnt = 0;
		for (int i = 0; i < stringb.length(); ++i)
		{
			for (int j = i + 1; j < stringb.length() + 1; ++j)
			{
				if (stringa.starts_with(stringb.substr(i, j)))
				{
					cnt = j - i;
					if (cnt > maxcnt)
					{
						maxcnt = cnt;
					}
				}
				else if (stringa.ends_with(stringb.substr(i, j)))
				{
					cnt = j - i;
					if (cnt > maxcnt)
					{
						maxcnt = cnt;
					}
				}
			}
		}
	}
	else
	{
		int cnt = 0;
		for (int i = 0; i < stringa.length(); ++i)
		{
			for (int j = i + 1; j < stringa.length() + 1; ++j)
			{
				if (stringb.starts_with(stringa.substr(i, j)))
				{
					cnt = j - i;
					if (cnt > maxcnt)
					{
						maxcnt = cnt;
					}
				}
				else if (stringb.ends_with(stringa.substr(i, j)))
				{
					cnt = j - i;
					if (cnt > maxcnt)
					{
						maxcnt = cnt;
					}
				}
			}
		}
	}
	cout << maxcnt;
}
