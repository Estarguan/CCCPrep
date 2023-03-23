#include <iostream>
#include <vector>
using namespace std;
typedef pair<int,int> pi;
int g[9][9]; bool row[9][10], col[9][10],blk[9][10];char c; vector<pi>vec;
bool fun(int idx){
	if(idx == vec.size()) return true;
	int r = vec[idx].first, c = vec[idx].second;
	for (int k=1; k<= 9; ++k){
		if (!row[r][k] && !col[c][k] && !blk[3*(r/3)+(c/3)][k]){
			g[r][c] = k; row[r][k]=col[c][k]=blk[3*(r/3)+(c/3)][k] = true;
			if (fun(idx + 1)) return true;
			row[r][k] = col[c][k]= blk[3*(r/3)+(c/3)][k] = false;
		}
	}
	return false;
}

int main(){
	for(int i = 0; i < 9; i++){
		for(int j = 0; j < 9; j++){
			cin >> c;
			if (c!= '.'){
				g[i][j] = c-'0';
				row[i][g[i][j]] = col[j][g[i][j]] = blk[3*(i/3)+(j/3)][g[i][j]] = true;
			}else{
				vec.push_back({i,j});
			}
		}
	}
	fun(0);
	for(int i =0; i <9; i++){
		for (int j = 0; j < 9; j++){
			cout << g[i][j];
		}
		cout << endl;
	}
}