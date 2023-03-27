// 국어 a 페이지, 수학 b 페이지 풀어야 함 
// 하루에 국어를 최대 c 페이지, 수학을 최대 d 페이지 풀 수 있다.
#include <iostream>
#include <math.h>

using namespace std;

int main(){
    int l , a,b,c,d,maxx;
    cin >> l >> a >> b >> c >> d;
    maxx = l - max( ceil(((float)a / c)), ceil(((float)b/d)));
    cout << maxx <<endl;
}