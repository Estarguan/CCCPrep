#include <iostream>
#include <vector>
using namespace std;

int main(){
    string s, ex; vector<char> stk;
    cin >> s >> ex;
    for (int i = 0; i < s.size(); i++){
        stk.push_back(s[i]);
        if (stk.size() >= ex.size()){
            bool explosion = true;
            for (int k = 0; k < ex.size(); k++){
                if (stk[(int)stk.size()-1-k] != ex[(int)ex.size()-1-k]){
                    explosion = false; break;
                }
            }
            if (explosion){
                for (int k = 0; k < ex.size();k++){
                    stk.pop_back();
                }
            }
        }
    }
    if(stk.empty()) cout << "FRULA\n";
    else{
        for (char c :stk) cout << c;
        cout << '\n';
    }
}
