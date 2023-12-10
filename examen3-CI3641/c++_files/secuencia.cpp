#include <iostream>
#include <stack>
#include <queue>
#include <vector>
#include<string>
using namespace std;

template <class T>
class Secuencia{
    vector<T> coleccion;
    public:
        Secuencia(){
            this->coleccion = vector<T>();
        };
        virtual void agregar(T elemento){
            this->coleccion.push_back(elemento);
        };
        virtual T remover(){
            if (! this->coleccion.empty()){
                T elemento = this->coleccion.back();
                this->coleccion.pop_back();
                return elemento;
            };
            throw "No se puede eliminar un elemento que no existe";
        };
        virtual bool vacio(){
            return this->coleccion.empty();
        };
        void imprimir(){
            for(auto elem : this->coleccion){
                cout << elem << " ";
            }
            cout << endl;
        }
};

template <class T>
class Pila: public Secuencia<T>{
    stack<T> coleccion;
    public:
        Pila(){
            this->coleccion = stack<T>();
        }
        void agregar(T elemento){
            this->coleccion.push(elemento);
        };
        T remover(){
            if (! this->coleccion.empty()){
                T elemento = this->coleccion.top();
                this->coleccion.pop();
                return elemento;
            };
            throw "No se puede eliminar un elemento que no existe";
        };
        bool vacio(){
            return this->coleccion.empty();
        };
};

template <class T>
class Cola: public Secuencia<T>{
    queue<T> coleccion;
    public:
        Cola(){
            this->coleccion = queue<T>();
        }
        void agregar(T elemento){
            this->coleccion.push(elemento);
        };
        T remover(){
            if (! this->coleccion.empty()){
                T elemento = this->coleccion.front();
                this->coleccion.pop();
                return elemento;
            };
            throw "No se puede eliminar un elemento que no existe";
        };
        bool vacio(){
            return this->coleccion.empty();
        };
};

int main(){
    Secuencia<int> S1;
    S1.agregar(1); S1.agregar(2); S1.agregar(3);
    S1.imprimir();
    cout << S1.remover() << endl;
    S1.imprimir();

    Secuencia<string> S2;
    S2.agregar("hola"); S2.agregar("uwu"); S2.agregar("wiiii");
    S2.imprimir();
    cout << S2.remover() << endl;
    S2.imprimir();
    
    cout << "Floats:\n";
    cout << "   Pila:\n";
    // Pila de floats
    Pila<float> pilaFloats;
    pilaFloats.agregar(1.5);
    pilaFloats.agregar(2.2); 
    pilaFloats.agregar(3.7);

    cout << "     " << pilaFloats.remover() << endl; // 3.7
    cout << "     " << pilaFloats.remover() << endl; // 2.2

    cout << "   Cola:\n";
    // Cola de floats
    Cola<float> colaFloats;
    colaFloats.agregar(1.5);
    colaFloats.agregar(2.2); 
    colaFloats.agregar(3.7);

    cout << "     " << colaFloats.remover() << endl; // 1.5
    cout << "     " << colaFloats.remover() << endl; // 2.2

    cout << "Enteros:\n";
    cout << "   Pila:\n";
    // Pila de enteros
    Pila<int> pilaEnteros;
    pilaEnteros.agregar(10);
    pilaEnteros.agregar(20);
    pilaEnteros.agregar(30);

    cout << "     " << pilaEnteros.remover() << endl; // 30
    cout << "     " << pilaEnteros.remover() << endl; // 20

    cout << "   Cola:\n";
    // Cola de enteros
    Cola<int> colaEnteros;
    colaEnteros.agregar(10);
    colaEnteros.agregar(20);
    colaEnteros.agregar(30);

    cout << "     " << colaEnteros.remover() << endl; // 10
    cout << "     " << colaEnteros.remover() << endl; // 20

    cout << "Strings:\n";
    cout << "   Pila:\n";
    // Pila de strings
    Pila<string> pilaStrings;
    pilaStrings.agregar("hola");
    pilaStrings.agregar("mundo");
    pilaStrings.agregar("!");  

    cout << "     " << pilaStrings.remover() << endl; // !
    cout << "     " << pilaStrings.remover() << endl; // mundo

    cout << "   Cola:\n";
    // Cola de strings
    Cola<string> colaStrings;
    colaStrings.agregar("hola");
    colaStrings.agregar("mundo");
    colaStrings.agregar("!");  

    cout << "     " << colaStrings.remover() << endl; // hola
    cout << "     " << colaStrings.remover() << endl; // mundo


    return 0;
}