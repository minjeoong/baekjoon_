#include <iostream>

using namespace std;

int main() {
    int k; cin >> k;
    for (int i = 0; i < k ; i++) {
        int x; cin >> x;
        int a=0, b=0, c=0, d=0;
        while (x>0) {
            if (x >= 25) {
                a++;
                x -= 25;      
            }
            else if (x >= 10){
                b++;
                x -= 10;
            }
            else if (x >= 5) {
                c++;
                x -= 5;
            }
            else if(x < 5){
                d++;
                x -= 1;
            }
        } 
        cout << a << " "<< b << " "<< c << " "<< d <<endl;

    }
}