// librerias necesarias para el funcionamiento del programa
#include <iostream>
#include <stack>
#include <queue>
#include <vector>
#include<map>

using namespace std;

// definicion del tipo de datos Grafo
// la lista de adyacencia fue implementada como un mapa de int a vector de int
// esto con el fin de poder tener nodos con valores distintos y no necesariamente
// secuenciales
struct Grafo{
    map<int, vector<int> > lista_adyacencia;
};

// definicion de la clase Busqueda
class Busqueda{
    public:
        // Destructor por defecto
        virtual ~Busqueda() = default;
        // Metodo que debe ser implementado en las clases derivadas
        virtual int buscar(int H, int D, const Grafo &G) = 0;
};

// definicion de la clase derivada DFS
class DFS : public Busqueda {
public:
    // Metodo que implementa el algoritmo DFS iterativo mediante el uso de un stack
    int buscar(int H, int D, const Grafo &graph) override{
        stack<int> stack;
        map<int, bool> visitado;
        vector<int> camino;
        // Inicializar con false todos los nodos del grafo en el mapa visitado
        for(auto& par : graph.lista_adyacencia) {
         visitado[par.first] = false; 
        }
        
        stack.push(H);

        while (!stack.empty()) {
            int nodo = stack.top();
            stack.pop();

            // Si el nodo es el destino de busqueda, retornar la cantidad de nodos explorados
            // si contar el nodo de destino
            if (nodo == D) {
                return camino.size(); // Cantidad de nodos explorados
            }

            // Si el nodo no ha sido visitado, marcarlo como visitado y agregarlo al camino
            if (!visitado[nodo]) {
                visitado[nodo] = true;
                camino.push_back(nodo);
                for (auto vecino : graph.lista_adyacencia.at(nodo)) {
                    if (!visitado[vecino]) {
                        stack.push(vecino);
                    }
                }
            }
        }
        return -1; // Nodo D no alcanzable desde H
    }
};

// definicion de la clase derivada BFS
class BFS : public Busqueda {
public:
    // Metodo que implementa el algoritmo BFS iterativo mediante el uso de una cola
    int buscar(int H, int D, const Grafo& graph) override{ 
        queue<int> cola;
        map<int, bool> visitado;
        vector<int> camino;

        // Inicializar con false todos los nodos del grafo en el mapa visitado
        for(auto& par : graph.lista_adyacencia) {
         visitado[par.first] = false; 
        }
        
        cola.push(H);

        while (!cola.empty()) {
            int nodo = cola.front();
            cola.pop();

            // Si el nodo es el destino de busqueda, retornar la cantidad de nodos explorados
            // si contar el nodo de destino
            if (nodo == D) {
                return camino.size(); // Cantidad de nodos explorados
            }

            // Si el nodo no ha sido visitado, marcarlo como visitado y agregarlo al camino
            if (!visitado[nodo]) {
                visitado[nodo] = true;
                camino.push_back(nodo);
                for (auto vecino : graph.lista_adyacencia.at(nodo)) {
                    if (!visitado[vecino]) {
                        cola.push(vecino);
                    }
                }
            }
        }
        return -1; // Nodo D no alcanzable desde H
    }
};

/********** PROGRAMA PRINCIPAL **********/
int main(){
    // Ejemplo de grafo
    Grafo grafoEjemplo;
    grafoEjemplo.lista_adyacencia = {{7, {5, 21, 75}},{5, {}},{21, {5,25}},{75, {6}},{25,{9}},{6,{8}},{9,{6}}, {8, {25}}};
    DFS dfs;
    cout << "Cantidad de nodos visitados en DFS:\n" << dfs.buscar(7,9,grafoEjemplo)<<endl;
    BFS bfs;
    cout << "Cantidad de nodos visitados en BFS:\n" << bfs.buscar(7,9,grafoEjemplo)<<endl;
    return 0;
}