#include <iostream>
using namespace std;
#include <string>

int main(){

    cin.tie(0);

    bool T = true;

    while (T)
    {
        string s;
        getline(cin, s);

        if (s =="END"){
            T = false;
            break;
        }
        for (int i = s.length()-1 ; i >= 0 ; i-- ){
            cout << s[i];
        }
        cout << "\n" ;
    }
    

}