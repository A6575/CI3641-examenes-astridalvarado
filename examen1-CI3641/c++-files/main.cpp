#include "vector3D.h"

using namespace std;

// Pruebas a ejecutar en la libreria vector3d.h
int main(){
    vector3D A(1,2,3);
    vector3D B(-4,-5,-6);
    vector3D C(7.5, -8.2, 9.25);
    vector3D D;

    cout << B + C << endl;              // output: (3.5, -13.2, 3.25)
    cout << A * B + C << endl;          // output: (10.5, -14.2, 12.25)
    cout << (B + B) * (C - A) << endl;  // output: (-184.9, -28, 146.6)
    cout << A % (C * B) << endl;        // output: -99.45
    cout << B + 150 << endl;;           // output: (146, 145, 144)
    cout << A * 3.7 + &B << endl;       // output: (12.475, 16.175, 19.875)
    cout << C - 6 << endl;              // output: (1.5, -14.2, 3.25)
    cout << (B + B) * (C % A) << endl;  // output: (-150.8, -188.5, -226.2)
    cout << D << endl;                  // output: (0, 0, 0)

    return 0;
}