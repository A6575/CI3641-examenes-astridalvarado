#include "vector3D.h"

using namespace std;

int main(){
    vector3D A(1,2,3);
    vector3D B(-4,-5,-6);
    vector3D C(7.5, -8.2, 9.25);
    vector3D D;

    cout << B + C << endl;
    cout << A * B + C << endl;
    cout << (B + B) * (C - A) << endl;
    cout << A % (C * B) << endl;
    cout << B + 150 << endl;;
    cout << A * 3.7 + &B << endl;
    cout << C - 6 << endl;
    cout << (B + B) * (C % A) << endl;
    cout << D << endl;

    return 0;
}