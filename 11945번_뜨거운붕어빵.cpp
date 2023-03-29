#include <iostream>
using namespace std;


int main(){
    int x, y;
    cin >> x >> y;
    char s[10][10];

    for (int i = 0; i < x; i++){  
        for (int j = 0; j < y; j++){
            cin >> s[i][j];
        }
    }
    for (int i = 0; i < x; i++){  
        for (int j = y-1; j >= 0; j--){
            cout << s[i][j];
        }
        cout << "\n";
    }

}