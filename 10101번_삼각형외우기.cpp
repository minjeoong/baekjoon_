#include <iostream>
using namespace std;

int main(){
    int x, y, z;
    cin >> x >> y >> z;
    if (x == y and y == z and x == 60) {
        cout <<"Equilateral" << endl;
    }
    else if (x+y+z == 180 and (x != y and y !=z and x !=z)) {
        cout << "Scalene" << endl;
    }
    else if (x+y+z == 180 and (x == y or y ==z or x ==z)) {
        cout << "Isosceles" <<endl;
        
    }
    else{
        cout << "Error" << endl;
    }
}