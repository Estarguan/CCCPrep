#include <iostream>
using namespace std;

int n,r,s;
int main(){
    cin >> n>>r>>s;
    for (int x = 0; x < n; ++x){
        string mat[r];
        int max = -1, min = r+1;
        for (int y = 0; y < r; ++y){
            string temp; cin >> temp;
            mat[y] = temp;
        }
        for (int i = 0; i < s; ++i){
            for (int j = 0; j < r; ++j){
                if (mat[j][i] == '#'){
                    if (j+1 > max){
                        max = j+1;
                    }
                    if (j+1 < min){
                        min = j+1;
                    }
                }
            }
        }
        cout << max-min << endl;

    }
    cout << endl;
}
