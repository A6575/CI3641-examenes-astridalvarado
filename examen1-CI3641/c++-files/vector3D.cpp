/*
    Archivo cuerpo "vector3D.cpp" que implementa las funcionalidades asociadas a la libreria
    que permite el manejo de vectores de tres dimensiones.
*/

#include "vector3D.h"

/* Operaciones binarias con ambos operandos del tipo vector3D.
   Estas operaciones dan como resultado un vector nuevo cuyas
   componentes son de la forma (v1.i [op] v2.i, v1.j [op] v2.j, v1.k [op] v2.k)

   Para el caso de la operacion producto-cruz, se aplica la formula correspondiente
*/
vector3D vector3D::operator + (vector3D v2){
    return vector3D(this->i + v2.i, this->j + v2.j, this->k + v2.k);
};
vector3D vector3D::operator - (vector3D v2){
    return vector3D(this->i - v2.i, this->j - v2.j, this->k - v2.k);
};
vector3D vector3D::operator * (vector3D v2){
    return vector3D(this->j * v2.k - this->k * v2.j,
                    -(this->i * v2.k - this->k * v2.i),
                    this->i * v2.j - this->j * v2.i);
};


/* Operaciones binarias con ambos operandos del tipo vector3D.
   Estas operaciones dan como resultado un vector nuevo cuyas
   componentes son de la forma (v1.i [op] m, v1.j [op] m, v1.k [op] m)
*/
vector3D vector3D::operator + (double n){
    return vector3D(this->i + n, this->j + n, this->k + n);
};
vector3D vector3D::operator - (double n){
    return vector3D(this->i - n, this->j - n, this->k - n);
};
vector3D vector3D::operator * (double n){
    return vector3D(this->i * n, this->j * n, this->k * n);
};

/* Operacion binaria con ambos operandos del tipo vector3D.
    Da como resultado el producto-punto de dos vectores
*/
double vector3D::operator % (vector3D v2){
    return (this->i * v2.i + this->j * v2.j + this->k * v2.k);
};

/* Operacion unaria de un vector.
   Retorna la norma del vector dado
*/
double vector3D::operator & (){
    return sqrt(this->i*this->i + this->j*this->j + this->k*this->k );
};

/* Implementacion de << para la salida estandar de la clase
*/
std::ostream& operator << (std::ostream &o, vector3D v){
    o << "(" << v.i << ", " << v.j << ", " << v.k << ")";
    return o;
};