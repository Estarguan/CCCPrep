#include<bits/stdc++.h>
typedef long long ll ;
#define int ll

#define inf 1000000000000000000
#define N 40

using namespace std ;
int dp[N];
//---------------------------------------------------------------------------------------
string f = "Good writing is good writing is good writing." ;
string s = "Good writing is good ";
string m = " writing is good " ;
string e = " is good writing." ;
int fl = f.length() , sl = s.length() , ml = m.length(), el = e.length();
//---------------------------------------------------------------------------------------
char query(int n , int k)
{
	if(n == 0 && k < fl)
	{
		return f[k] ;
	}
	else if(n == 0)
	{
		return '.' ;
	}
	if(k < sl)
	{
		return s[k] ;
	}
	else if(k < sl + dp[n-1])
	{
		return query(n - 1 , k - sl) ;
	}
	else if(k < sl + ml + dp[n - 1])
	{
		return m[k - sl - dp[n - 1]] ;
	}
	else if(k < sl + ml + 2*dp[n-1])
	{
		return query(n - 1 , k - sl - ml - dp[n-1]) ;
	}
	return e[k - sl - ml - 2*dp[n -1]] ;
}

signed main( )
{
    ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
	int q ;
	cin >> q ;
	dp[0] = fl ;
	for(int i = 1 ; i <= 30 ; i++)
	{
	    if(dp[i - 1]*2 + sl + ml + el < inf){
            dp[i] = dp[i - 1]*2 + sl + ml + el;
	    }
	    else{
            dp[i] = inf;
	    }
 	}
	while(q--)
	{
		int n , k ;
		cin >> n >> k ;
		if(k <= dp[n])
		{
			cout << query(n , k - 1) ;
		}
		else
		{
			cout << "." ;
		}
		cout<<endl;
	}

}