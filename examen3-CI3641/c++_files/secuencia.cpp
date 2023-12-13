// librerias necesarias para el funcionamiento del programa
#include <iostream>
#include <stack>
#include <queue>
#include <vector>
#include<string>
using namespace std;

// definicion de la clase generica Secuencia
template <class T>
class Secuencia{
    // por defecto, una secuencia es un vector de tipo T
    vector<T> coleccion;
    public:
        // Constructor
        Secuencia(){
            this->coleccion = vector<T>();
        };
        // funcion que agrega un elemento a la secuencia. Se declara como virtual
        // para que se sobreescriba esta funcion en las subclases de Secuencia
        virtual void agregar(T elemento){
            this->coleccion.push_back(elemento);
        };
        // funcion que remueve el ultimo elemento de la secuencia. Se declara como virtual
        // para que se sobreescriba esta funcion en las subclases de Secuencia
        virtual T remover(){
            if (! this->coleccion.empty()){
                T elemento = this->coleccion.back();
                this->coleccion.pop_back();
                return elemento;
            };
            throw "No se puede eliminar un elemento que no existe";
        };
        // funcion que determina si la secuencia esta vacia. Se declara como virtual
        // para que se sobreescriba esta funcion en las subclases de Secuencia
        virtual bool vacio(){
            return this->coleccion.empty();
        };
        // funcion que imprime la secuencia
        virtual void imprimir(){
            for(auto elem : this->coleccion){
                cout << elem << " ";
            }
            cout << endl;
        }
};

// definicion de la clase derivada Pila
template <class T>
class Pila: public Secuencia<T>{
    // por defecto, una pila es un stack de tipo T
    stack<T> coleccion;
    public:
        // Constructor
        Pila(){
            this->coleccion = stack<T>();
        }
        // Metodo que agrega un elemento a la pila.
        void agregar(T elemento){
            this->coleccion.push(elemento);
        };
        // Metodo que remueve el ultimo elemento de la pila.
        T remover(){
            if (! this->coleccion.empty()){
                T elemento = this->coleccion.top();
                this->coleccion.pop();
                return elemento;
            };
            throw "No se puede eliminar un elemento que no existe";
        };
        // Metodo que determina si la pila esta vacia.
        bool vacio(){
            return this->coleccion.empty();
        };

        void imprimir(){
            stack<T> copia = this->coleccion;

            while (!copia.empty()){
                T elem = copia.top();
                copia.pop();

                cout << elem << " ";
            }
            cout << endl;
        }
};

// definicion de la clase derivada Cola
template <class T>
class Cola: public Secuencia<T>{
    // por defecto, una cola es un queue de tipo T
    queue<T> coleccion;
    public:
        // Constructor
        Cola(){
            this->coleccion = queue<T>();
        }
        // Metodo que agrega un elemento a la cola.
        void agregar(T elemento){
            this->coleccion.push(elemento);
        };
        // Metodo que remueve el primer elemento de la cola.
        T remover(){
            if (! this->coleccion.empty()){
                T elemento = this->coleccion.front();
                this->coleccion.pop();
                return elemento;
            };
            throw "No se puede eliminar un elemento que no existe";
        };
        // Metodo que determina si la cola esta vacia.
        bool vacio(){
            return this->coleccion.empty();
        };

        void imprimir(){
            queue<T> copia = this->coleccion;

            while (!copia.empty()){
                T elem = copia.front();
                copia.pop();
                
                cout << elem << " ";
            }
            cout << endl;
        }
};

/********** PROGRAMA PRINCIPAL **********/
int main(){
    // Declacaciones de Secuencia
    Secuencia<int> S1;
    Secuencia<string> S2;
    Secuencia<float> S3;

    // Declaraciones de Pila
    Pila<int> P1;
    Pila<string> P2;
    Pila<float> P3;

    // Declaraciones de Cola
    Cola<int> C1;
    Cola<string> C2;
    Cola<float> C3;

    cout<<"DEFINIENDO SECUENCIAS\n"<<endl;

    // agregar elementos a las secuencias
    S1.agregar(1);
    S1.agregar(2);
    S1.agregar(3);
    S1.agregar(4);
    cout<<"Secuencia S1: ";
    S1.imprimir();

    S2.agregar("uno");
    S2.agregar("dos");
    S2.agregar("tres");
    S2.agregar("cuatro");
    cout<<"Secuencia S2: ";
    S2.imprimir();

    S3.agregar(1.1);
    S3.agregar(2.2);
    S3.agregar(3.3);
    S3.agregar(4.4);
    cout<<"Secuencia S3: ";
    S3.imprimir();

    cout<<"\nELIMINANDO EL ULTIMO ELEMENTO DE LAS SECUENCIAS\n"<<endl;
    // eliminar el ultimo elemento de las secuencias
    cout<<"Para S1: "<<S1.remover()<<"\n"<<"S1: ";
    S1.imprimir();
    cout<<"Para S2: "<<S2.remover()<<"\n"<<"S2: ";
    S2.imprimir();
    cout<<"Para S3: "<<S3.remover()<<"\n"<<"S3: ";
    S3.imprimir();

    cout<<"\nDEFINIENDO PILAS\n"<<endl;
    // agregar elementos a la pilas
    P1.agregar(1);
    P1.agregar(2);
    P1.agregar(3);
    P1.agregar(4);
    cout<<"Pila P1: ";
    P1.imprimir();

    P2.agregar("uno");
    P2.agregar("dos");
    P2.agregar("tres");
    P2.agregar("cuatro");
    cout<<"Pila P2: ";
    P2.imprimir();

    P3.agregar(1.1);
    P3.agregar(2.2);
    P3.agregar(3.3);
    P3.agregar(4.4);
    cout<<"Pila P3: ";
    P3.imprimir();

    cout<<"\nELIMINANDO EL ULTIMO ELEMENTO DE LAS PILAS\n"<<endl;
    // eliminar el ultimo elemento de las pilas
    cout<<"Para P1: "<<P1.remover()<<"\n"<<"P1: ";
    P1.imprimir();
    cout<<"Para P2: "<<P2.remover()<<"\n"<<"P2: ";
    P2.imprimir();
    cout<<"Para P3: "<<P3.remover()<<"\n"<<"P3: ";
    P3.imprimir();

    cout<<"\nDEFINIENDO COLAS\n"<<endl;
    // agregar elementos a las colas
    C1.agregar(1);
    C1.agregar(2);
    C1.agregar(3);
    C1.agregar(4);
    cout<<"Cola C1: ";
    C1.imprimir();

    C2.agregar("uno");
    C2.agregar("dos");
    C2.agregar("tres");
    C2.agregar("cuatro");
    cout<<"Cola C2: ";
    C2.imprimir();

    C3.agregar(1.1);
    C3.agregar(2.2);
    C3.agregar(3.3);
    C3.agregar(4.4);
    cout<<"Cola C3: ";
    C3.imprimir();

    cout<<"\nELIMINANDO EL PRIMER ELEMENTO DE LAS COLAS\n"<<endl;
    // eliminar el primer elemento de las colas
    cout<<"Para C1: "<<C1.remover()<<"\n"<<"C1: ";
    C1.imprimir();
    cout<<"Para C2: "<<C2.remover()<<"\n"<<"C2: ";
    C2.imprimir();
    cout<<"Para C3: "<<C3.remover()<<"\n"<<"C3: ";
    C3.imprimir();

    return 0;
}