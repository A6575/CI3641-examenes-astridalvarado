/*
    Archivo de cabecera "vector3D.h" con las declaraciones necesarias para
    la creacion de una libreria para el manejo del tipo de vectores de tres dimensiones
*/

#ifndef VECTOR3D_H_ 
#define VECTOR3D

// librerias necesarias para el funcionamiento del codigo
#include<iostream>
#include<math.h>

class vector3D{
// se define la clase vector3D con los siguientes atributos publicos
public:
    /* 
    variables del tipo double para almacenar las coordenadas del vector.
    Se tiene:
        i -> representa la coordenada x del vector
        j -> representa la coordenada y del vector
        k -> representa la coordenada z del vector
    */
    double i, j, k;
    
    /*
    constructores de la clase.
        vector3D() -> Constructor para vector nulo. Cualquier variable declarada 
                      como vector3D sin especificar sus coordenadas es de la forma (0,0,0)
        
        vector3D(i, j, k) -> Constructor para un vector de la forma (i, j, k)
    */  
    vector3D(){
        this->i = 0;
        this->j = 0;
        this->k = 0;
    }
    vector3D(double _i, double _j, double _k){
        this->i = _i;
        this->j = _j;
        this->k = _k;
    };

    /* Definicion de operadores basicos de vectores */
    vector3D operator + (vector3D v2);      // operador suma entre dos vectores v1 y v2
    vector3D operator - (vector3D v2);      // operador resta entre dos vectores v1 y v2
    vector3D operator * (vector3D v2);      // operador producto-cruz entre dos vectores v1 y v2

    vector3D operator + (double n);         // operador suma entre un vector v1 y un numero n
    vector3D operator - (double n);         // operador resta entre un vector v1 y un numero n
    vector3D operator * (double n);         // operador multiplicacion entre un vector v1 y un numero n

    double operator % (vector3D v2);        // operador producto-punto entre dos vectores v1 y v2
    double operator & ();                   // operador norma de un vector 

    // funcion asociada a la clase. Esto permite la impresion directa de
    // los vectores en la forma (i, j, k)
    friend std::ostream& operator << (std::ostream &o, vector3D v);
};

#endif
