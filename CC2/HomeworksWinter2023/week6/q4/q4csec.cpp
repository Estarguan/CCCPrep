#include <bits/stdc++.h>
 
using namespace std;
typedef long long ll;
 
const int MM = 5001;
 
int N, h[MM];
int asym[MM][MM];
 
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    cin >> N;
    for(int i = 0; i < N; i++){
        cin >> h[i];
    }
    // Odds
    for(int len = 1; len <= N; len += 2){
        for(int l = 0; l + len - 1 < N; l++){
            if(len == 1){
                asym[l][l + len - 1] = 0;
            } else {
                asym[l][l + len - 1] = asym[l + 1][l + len - 2] + abs(h[l] - h[l + len - 1]);
            }
        }
    }
    // Evens
    for(int len = 2; len <= N; len += 2){
        for(int l = 0; l + len - 1 < N; l++){
            if(len == 2){
                asym[l][l + len - 1] = abs(h[l] - h[l + len - 1]);
            } else {
                asym[l][l + len - 1] = asym[l + 1][l + len - 2] + abs(h[l] - h[l + len - 1]);
            }
        }
    }
    for(int len = 1; len <= N; len++){
        int ans = 0x3f3f3f3f;
        for(int i = 0; i + len - 1 < N; i++){
            ans = min(ans, asym[i][i + len - 1]);
        }
        cout << ans << (len == N ? "\n" : " ");
    }
}